from pathlib import Path
import csv, json, re
from collections import Counter
P=Path(__file__).parent
def read(n):
    with (P/n).open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f))
def write(n,rows,fields=None):
    fields=fields or list(dict.fromkeys(k for row in rows for k in row))
    with (P/n).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows({k:r.get(k,'not_applicable') or 'not_found_publicly' for k in fields} for r in rows)
rows=read('bibliography_books.csv')+read('bibliography_featured.csv')+read('bibliography_junior.csv')
theme_map={'P11-BW001':'T3 Solidarity and social institutions','P11-BW002':'T1 Capitalism, credit and public power','P11-BW003':'T3 Solidarity and social institutions','P11-BW004':'T4 Evidence, lives and scales','P11-BW005':'T1 Capitalism, credit and public power','P11-BW006':'T2 Property, empire and environments','P11-BW007':'T1 Capitalism, credit and public power'}
for r in rows:
    r['edition_id']=r.get('edition_id',r['work_id']+'-E01')
    y=int(r['edition_date'][:4])
    r['scope']='establishment_era' if y>=2022 else ('collaboration_prehistory' if y>=2019 else 'preperiod_context')
    r['as_of_date']='2026-11-15'
    if r['work_id']=='P11-W006':
        r['first_publication_year']='date_unknown'
        r['notes']+='; 2018 is the verified English edition date, not a verified first-original-publication year.'
    r['original_theme']=r['theme']
    if r['work_id'].startswith('P11-JW'):
        n=int(r['work_id'][-3:]);r['theme']='T2 Property, empire and environments' if n<=5 else ('T1 Capitalism, credit and public power' if n<=10 else 'T4 Evidence, lives and scales')
    elif r['work_id'] in theme_map:r['theme']=theme_map[r['work_id']]
    r['relationship_evidence_status']='conflicting' if r['work_id']=='P11-BW003' else ('inferred' if r['work_id']=='P11-W008' else 'verified')
    r['edition_relationship_status']='inferred' if r['work_id'] in ['P11-W005','P11-W008'] else ('unverified' if r['work_id']=='P11-W006' else 'verified')
    r['affiliation_at_publication_status']='unverified'
    r['selection_rationale']='not_selected; retained in evidence inventory'
reasons={
'P11-BW001':'Full card: recent book by a former fellow; source practice and institutional daily life.',
'P11-BW002':'Full card: conceptual entry point; current coordinator relationship stated without backdating.',
'P11-BW003':'Full card: social institutions and early-career fellowship history; date conflict visibly retained.',
'P11-BW004':'Full card: microhistory and digital companion; English/French editions linked.',
'P11-BW005':'Full card: credit and exclusion; introduction read; translation and reception documented.',
'P11-BW006':'Full card: informal empire; French/English reading routes and edition distinction.',
'P11-BW007':'Short notice: journal response makes scholarly debate visible beyond monographs.',
'P11-W001':'Short notice: worker internationalism and collective action; original and translation one work.',
'P11-W002':'Short notice: concise research format connects property with global urban history.',
'P11-W003':'Short notice: coauthored French synthesis connects sociology and history.',
'P11-W004':'Short notice: edited volume and documented international research organisation; no CHEP funding claim.',
'P11-W005':'Short notice: practical methods for students; revised translation original link needs direct recheck.',
'P11-W007':'Context notice: environment and South Asia; 2020 reprint of 2018 work clearly marked.',
'P11-W008':'Short notice: North African transimperial history; French enriched-edition relation requires colophon check.',
'P11-W009':'Short notice: jointly authored chapter makes one actual research connection visible; parent-volume relation explicit.',
'P11-JW001':'Short notice: junior author and edition of historical debates; earlier work by later fellow.',
'P11-JW010':'Short notice: current junior author and recent article; publisher-time Harvard affiliation preserved.',
'P11-JW011':'Short notice: current student’s earlier public scholarly essay; publication before documented 2026 affiliation.'}
for r in rows:
    if r['work_id'] in reasons:r['selection_rationale']=reasons[r['work_id']]
write('bibliography.csv',rows)
selection=[]
for i,(wid,reason) in enumerate(reasons.items(),1):
    editions=[r for r in rows if r['work_id']==wid]
    r=editions[0].copy()
    r['selection_id']=f'P11-SEL{i:03}'
    r['edition_ids']=';'.join(x['edition_id'] for x in editions)
    r['linked_editions']=' | '.join(x['title']+' ('+x['edition_date']+')' for x in editions)
    r['selection_rationale']=reason
    r['source_ids']=';'.join(dict.fromkeys(s for x in editions for s in x['source_ids'].split(';')))
    r['showcase_format']='full_card' if wid in [f'P11-BW{x:03}' for x in range(1,7)] else 'short_notice'
    selection.append(r)
write('selection.csv',selection)
sources=[]
for name in ['sources_featured.csv','sources_books.csv','sources_junior.csv','sources_milestones.csv']:sources+=read(name)
write('sources.csv',sources,['source_id','url','title','publisher_or_owner','source_date','accessed_at','source_type','supports','retrieval_status'])
ids={r['source_id'] for r in sources}
missing=[(r['work_id'],s) for r in rows for s in r['source_ids'].split(';') if s.strip() not in ids]
assert not missing,missing
assert len({r['edition_id'] for r in rows})==len(rows)
assert len(selection)==18
assert len({r['source_id'] for r in sources})==len(sources)
assert all(r['edition_date'][:10]<='2026-11-15' for r in rows)
print(json.dumps({'rows':len(rows),'works':len({r['work_id'] for r in rows}),'sources':len(sources),'selection':len(selection),'scope':dict(Counter(r['scope'] for r in rows)),'languages':dict(Counter(r['language'] for r in rows)),'types':dict(Counter(r['type'] for r in rows))},ensure_ascii=False,indent=2))
