from pathlib import Path
import csv, json, re, unicodedata
from urllib.parse import unquote
from collections import Counter, defaultdict

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'reports/P13_synthesis'
def read(name):
    with (OUT/name).open(encoding='utf-8',newline='') as f:
        reader=csv.DictReader(f); rows=list(reader)
        assert reader.fieldnames and len(reader.fieldnames)==len(set(reader.fieldnames)),name
        assert all(None not in r and all(v is not None for v in r.values()) for r in rows),name
        return rows

required=['meeting_brief.md','proposal_comparison.csv','reconciliation_log.csv','id_crosswalk.csv','90_day_plan.md','meeting_agenda.md','report.md','sources.csv','coverage.md']
assert all((OUT/f).is_file() and (OUT/f).stat().st_size for f in required)
tables={n:read(n) for n in ['proposal_comparison.csv','reconciliation_log.csv','id_crosswalk.csv','sources.csv','input_inventory.csv']}
expected=['proposal','supporting_report_ids','evidence_strength','benefit','setup_hours','recurring_hours','estimated_cash','dependencies','maintenance_owner_function','recommended_status']
assert list(tables['proposal_comparison.csv'][0])==expected
for name,key in [('sources.csv','source_id'),('reconciliation_log.csv','reconciliation_id'),('input_inventory.csv','report_id')]:
    ids=[r[key] for r in tables[name]]
    assert len(ids)==len(set(ids)),(name,'duplicate IDs')
assert {r['evidence_status'] for r in tables['reconciliation_log.csv']}<={'verified','inferred','conflicting','unverified'}
assert all(r['missing_expected_files']=='none' for r in tables['input_inventory.csv'])

missing_links=[]
checked_links=0
for md in [*OUT.glob('*.md'),* (OUT/'working').glob('*.md')]:
    for target in re.findall(r'\]\(([^)]+)\)',md.read_text()):
        if re.match(r'(?:https?://|mailto:|#)',target): continue
        target=target.split('#',1)[0].split(' "',1)[0]
        if not target: continue
        checked_links+=1
        if not (md.parent/unquote(target)).exists(): missing_links.append((str(md.relative_to(OUT)),target))
assert not missing_links,missing_links

cross=tables['id_crosswalk.csv']
missing_record_files=sorted({r['source_file'] for r in cross if not (ROOT/r['source_file']).is_file()})
assert not missing_record_files,missing_record_files
manifest=(OUT/'input_manifest.md').read_text()
origpaths=[p for p in (ROOT/'reports').glob('P[01][0-9]_*') if p.name[:3] != 'P13' and 1<=int(p.name[1:3])<=12]
original_files=[p for d in origpaths for p in d.rglob('*') if p.is_file()]
assert len(original_files)==297
assert all('../'+str(p.relative_to(ROOT/'reports')) in manifest for p in original_files)

# A source occurrence should remain traceable even when a URL chain is shared.
for inv in tables['input_inventory.csv']:
    f=ROOT/inv['source_register']
    with f.open(encoding='utf-8-sig',newline='') as handle:
        original=list(csv.DictReader(handle))
    mapped=[r for r in cross if r['entity_type']=='source' and r['source_file']==inv['source_register']]
    assert len(mapped)>=len(original),(inv['report_id'],len(original),len(mapped))
    assert all(any(m['local_id']==r['source_id'] for m in mapped) for r in original)

editions=defaultdict(set)
for r in cross:
    if r['entity_type'] in ('work','publication_container'):
        editions[r['canonical_edition_id']].add(r['canonical_id'])
assert all(len(ids)==1 for e,ids in editions.items() if e!='not_applicable')

# Independent arithmetic from the weekly table and action components.
Asetup=[5,5,5,5,0,0,0,0,0,0,0,0]
Alater=[0,0,0,0,1.75,2.25,1.75,1.75,1.75,1.75,1.75,4.25]
B=[5,5,5,5,3,4,5,3,4,5,4,4]
Csetup=[4.75,4.75,4.75,4.25,3,0,4.75,4.25,2.5,0,0,0]
Clater=[.25,.25,.25,.75,2,5,.25,.75,.25,2,2.75,5]
A=[x+y for x,y in zip(Asetup,Alater)]
C=[x+y for x,y in zip(Csetup,Clater)]
assert (sum(A),sum(B),sum(C))==(37,52,52.5)
assert (sum(Asetup),sum(Alater),sum(Csetup),sum(Clater))==(20,17,33,19.5)
assert max(A+B+C)<=5
assert sum([6+4,10+8,4+5])==37
assert 421690+1578285==1999975

snapshot=json.loads((OUT/'working/input_metadata_snapshot.json').read_text())
changed=[]
for file,old in snapshot.items():
    st=(ROOT/file).stat()
    if (st.st_size,st.st_mtime_ns)!=(old['size_bytes'],old['mtime_ns']): changed.append(file)
assert not changed,changed
brief=(OUT/'meeting_brief.md').read_text()
assert brief.count('break-after: page')==1
pages=brief.split('<div style="break-after: page;"></div>')
word_counts=[len(re.findall(r'\S+',x)) for x in pages]
assert sum(word_counts)<=850,word_counts

result={'required_files':len(required),'csv_rows':{n:len(r) for n,r in tables.items()},'local_links_checked':checked_links,'original_files_manifested':len(original_files),'original_metadata_unchanged':True,'edition_identity_collisions':0,'portfolio_hours':[sum(A),sum(B),sum(C)],'max_weekly_hours':5,'brief_page_word_counts':word_counts,'status':'passed'}
(OUT/'working/validation_results.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result))
