from pathlib import Path
import csv, json, hashlib, re
from urllib.parse import urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'reports/P13_synthesis'
WORK = OUT / 'working'
ASOF = '2026-11-15'

def read(path):
    with Path(path).open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

def source_key(url):
    u = urlsplit(url.strip())
    host = u.netloc.lower()
    path = u.path
    # Only aliases inspected in CHEP's own live navigation are normalised.
    if host in ('www.histecon.fr', 'histecon.fr'):
        host = 'histecon.fr'
        if path == '/en/': path = '/en/index.html'
    return urlunsplit((u.scheme.lower(),host,path,u.query,''))

def stable_source(url):
    return 'P13-SRC-' + hashlib.sha256(source_key(url).encode()).hexdigest()[:12]

cross = read(WORK/'entity_crosswalk.csv')
cross_fields = list(cross[0])
fund = read(WORK/'funding_crosswalk.csv')
dirs = {p.name[:3]:p for p in (ROOT/'reports').iterdir() if p.is_dir() and re.match(r'P(0[1-9]|1[0-2])_',p.name)}
for r in fund:
    given=Path(r['input_file'])
    if str(given).startswith('reports/'):
        infile=str(given)
    elif given.parts[0].startswith('P') and len(given.parts)>1:
        infile=str(Path('reports')/given)
    else:
        infile=str(dirs[r['input_report_id']].relative_to(ROOT)/given)
    persistent='DOI 10.3030/819353; grant agreement 819353' if 'ERC819353' in r['synthesis_id'] else 'not_found_publicly'
    canonical=stable_source(r['canonical_url_or_identifier']) if r['entity_type']=='source' else r['synthesis_id']
    secondary='funding_review_alias' if r['entity_type']=='source' else 'not_applicable'
    cross.append(dict(zip(cross_fields,[r['entity_type'],canonical,'not_applicable',r['input_report_id'],infile,r['input_id'],secondary,r['notes'],r['canonical_url_or_identifier'],persistent,r['match_relationship'],'inferred',r['synthesis_source_ids'],r['notes'],ASOF])))

# Add five missing committee role assertions in the overlay only.
for n,pid,name in [(1,'P13-P009','David Todd'),(2,'P13-P004','Marie-Emmanuelle Chessel'),(3,'P13-P005','Thierry Mayer'),(4,'P13-P007','Emma Rothschild'),(5,'P13-P006','Paul-André Rosental')]:
    role = 'Executive committee President' if n==1 else 'Executive committee member'
    cross.append(dict(zip(cross_fields,['role','P13-R-COM%02d'%n,'not_applicable','P05','reports/P05_website/evidence/committee-en-ax.txt',name,pid,f'{name}: {role}','https://histecon.fr/en/executive_committee.html','not_found_publicly','Exact named listing in preserved live page; CHEP=P13-O001; committee=P13-O006','verified','P13-ES016;P13-ES017','Current-listing role as of capture; start/end date_unknown; no employment/reporting-line inference',ASOF])))

# Preserve every original source record. Group same-document chains without merging observations.
source_rows=[]
for rid,d in sorted(dirs.items()):
    path=d/'sources.csv'
    for ordinal,r in enumerate(read(path),1):
        url=r.get('url','').strip()
        sid=r.get('source_id','')
        if not url: raise ValueError((path,sid,'missing URL'))
        source_rows.append((rid,ordinal,r))
        cross.append(dict(zip(cross_fields,['source',stable_source(url),'not_applicable',rid,str(path.relative_to(ROOT)),sid,str(ordinal),r.get('title',''),source_key(url),'not_applicable','Same document URL; fragment removed; inspected CHEP home/www aliases only','inferred',sid,f"Original URL={url}; accessed={r.get('accessed_at','')}; retrieval={r.get('retrieval_status','')}. Identity group does not imply retrieval success or independent corroboration.",ASOF])))

source_fields=['source_id','url','title','publisher_or_owner','source_date','accessed_at','source_type','supports','retrieval_status']
sources=read(WORK/'entity_sources.csv')+read(WORK/'funding_sources.csv')
live=[
('P13-LIVE01','https://histecon.fr/en/list.html','CHEP News Registration','CHEP','date_unknown','official webpage','Registration embed exists; no archive or delivery claim','live browser read-only; web text route failed406; no form submitted'),
('P13-LIVE02','https://histecon.fr/en/index.html','CHEP English home','CHEP','date_unknown','official webpage','Current notices;2019 collaboration/2022 establishment; event list; shared social account','live browser read-only; older indexed /en/ representation not used for current notice claims'),
('P13-LIVE03','https://histecon.fr/fr/index.html','CHEP French home','CHEP','date_unknown','official webpage','Matching current notices and institutional chronology','live browser read-only'),
('P13-LIVE04','https://histecon.fr/en/research_grants.html','CHEP 2027 studentships','CHEP','date_unknown','official call','PhD years1–3;2027 expenses up to EUR1000;11Dec application/15Dec reference','live browser read-only; exact cutoff time/timezone absent; no portal transaction'),
('P13-LIVE05','https://histecon.fr/en/organisation.html','CHEP Organisation','CHEP','date_unknown','official webpage','Levy Coordinator; Cheadle coordination; Price web architect','live browser read-only; role start/end dates unstated'),
('P13-SS001','https://www.sciencespo.fr/histoire/fr/recherche/seminaires/seminaire-des-axes-et-des-domaines/histoires-de-la-vie-economique/','Histoires de la vie économique','Sciences Po CHSP','2026–2027 programme','official programme','Student/researcher access;CHEP support;announced current activities','opened indexed text; crawl six days old; no delivery/attendance inference')]
for sid,url,title,owner,date,typ,support,ret in live:
    sources.append(dict(zip(source_fields,[sid,url,title,owner,date,ASOF,typ,support,ret])))
for rid,d in sorted(dirs.items()):
    sources.append(dict(zip(source_fields,[f'P13-IN{rid[1:]}',f'../{d.name}/report.md',f'{rid} research report and linked artifacts','Local research workstream',ASOF,ASOF,'local research input','Findings/proposals/estimates; see original sources.csv and coverage.md','read locally; inherited scope and source limitations preserved'])))
sources += [dict(zip(source_fields,['P13-BRIEF','../../prompts_proposal.md','CHEP parallel research prompts: shared brief and P13','User workspace',ASOF,ASOF,'local brief','Scope,source map,five-hour/no-confirmed-budget scenario,deliverables','read locally'])),dict(zip(source_fields,['P13-SUMMARY','../../Summary.md','Summary source map','User workspace','date_unknown',ASOF,'local brief','Four institutional starting links','read locally']))]
for r in sources:
    if r['url'].startswith('https://'):
        cross.append(dict(zip(cross_fields,['source',stable_source(r['url']),'not_applicable','P13','reports/P13_synthesis/sources.csv',r['source_id'],'not_applicable',r['title'],source_key(r['url']),'not_applicable','Same-document source chain; observation retained separately','inferred',r['source_id'],r['retrieval_status'],ASOF])))

recon_fields=['reconciliation_id','topic','input_record_ids','conflicting_claims_or_duplicates','underlying_evidence','resolution_or_retained_alternatives','evidence_status','practical_implication','affected_outputs','as_of_date']
recon=[]
for r in read(WORK/'entity_conflicts.csv'):
    recon.append(dict(zip(recon_fields,[r['reconciliation_id'],r['topic'],'see id_crosswalk.csv and underlying evidence',r['conflicting_claims_or_duplicates'],r['underlying_evidence'],r['resolution'],r['status'],r['practical_implication'],r['affected_outputs'],ASOF])))
for r in read(WORK/'funding_conflicts.csv'):
    recon.append(dict(zip(recon_fields,[r['reconciliation_id'],r['issue'],r['input_record_ids'],r['conflicting_claims_or_duplicates'],r['synthesis_source_ids'],r['resolution_or_retained_alternatives'],r['evidence_status'],r['practical_implication'],r['affected_outputs'],ASOF])))
extras=[
('P13-RS01','Live content versus cached copies','P01;P05;P06;P10;P12','Some tools failed to retrieve current pages or returned old French content; P05/P13 live views show current notices and registration embed.','P13-LIVE01;P13-LIVE02;P13-LIVE03;P05 evidence/inspection_notes.md','Current bilingual notices and registration embed verified; issue archive and mailing frequency remain not_found_publicly. No broken-page or absent-newsletter conclusion from a406.','verified','Service improvement should connect maintained content; test archive need with communications function.','meeting_brief.md;report.md;portfolio_options.md'),
('P13-RS02','Observed access defect versus general demand','P05;P06;P07;P08;P12','Measured mobile overflow is evidence of a defect; comparator formats and repeated proposals do not measure unmet demand.','P05-V02;P13-SS001;P12 needs_assessment.md','Prioritise bounded access/correction service; peer sessions and new digest remain hypotheses; no absence-of-provision claim.','inferred','Require fit/overlap/interest checks before new programmes.','proposal_comparison.csv;meeting_brief.md;90_day_plan.md'),
('P13-RS03','Independent plans cannot all fit capacity','P05;P06;P07;P08;P09;P10;P11;P12','Each report proposes work against the same five-hour scenario; summing commitments exceeds capacity and duplicates maintenance.','working/inventory_portfolios.md;portfolio_options.md','Three mutually alternative portfolios:37/52/52.5 student hours over12weeks. No shared-work saving assumed. Technical and institutional labour separately stated.','inferred','Choose one, explicitly defer the others; spare hours are not approval for extra projects.','meeting_brief.md;proposal_comparison.csv;90_day_plan.md'),
('P13-RS04','Source completeness versus file completeness','P01–P12','All named required artifacts exist, but partial bibliographic/financial/history coverage persists.','input_inventory.csv;input_manifest.md;original coverage.md files','12/12 report packs present; no missing named required files. Research completeness is unestablished outside each defined checked corpus.','verified','No centre-wide membership, output, expenditure or demand dashboard.','report.md;coverage.md'),
('P13-RS05','Synthesis recheck scope for opportunities','P09-O001;O003;O005;O009;O018;O021','P09 snapshot lists24 opportunities, but synthesis only reopened6 priority records.','working/funding_review.md;P13-FS01–17','Six records rechecked;remaining18 retain original snapshot. Do not repeat open-status total as newly verified.','verified','Recheck exact official cycle immediately before any future publication/application advice.','report.md;coverage.md;90_day_plan.md')]
for row in extras: recon.append(dict(zip(recon_fields,list(row)+[ASOF])))

comparison_fields=['proposal','supporting_report_ids','evidence_strength','benefit','setup_hours','recurring_hours','estimated_cash','dependencies','maintenance_owner_function','recommended_status']
proposals=[
['A: entry guide + capped fact register + tested handover','P01;P02;P04;P05;P09;P12','verified service defect and source complexity; inferred usefulness; no audience-demand measurement','High immediate practical access/accuracy value; reversible short-page pilot',20,'17 total weeks5–12:14 upkeep/coordination +3 evaluation;1.75 h/week baseline','EUR0 conditional on existing tools and staff; technical repair separate','6 institutional review h; event/funding facts; academic/bilingual editor; publication route','Communications/web editor with academic and research-support inputs','recommend as sole initial portfolio;37 student h/12wk'],
['B: welcome guide + three peer sessions + bounded follow-up','P12;P04;P07;P08','verified existing provision and comparator mechanisms; unmet feedback demand unverified','Potentially high peer-feedback/community benefit; test rather than assume',14,'38 total delivery/upkeep/coordination/evaluation over12wk;52h incl setup','EUR0 only with in-kind room/platform/support; optional EUR36 excluded','11 institutional h; convenor; four interested people and one contributor; access approval','Academic convenor and administrative/event function','alternative replacing A; defer pending need and sponsorship'],
['C: digital reading edition + two six-weekly digest issues','P02;P06;P11','verified selection material; edition/affiliation limits; readership demand unverified','Medium-high research discovery value; reusable editorial output',33,'19.5 total over12wk:13 issues +3 checks +1.5 edition reviews +2 evaluation','EUR0 conditional on existing publishing tools and staff','7.5 institutional h; academic/bilingual editor; distributor; archive route; anniversary basis if used','Academic editor and communications/archive function','alternative replacing A;52.5 student h; no third issue in90days'],
['Responsive/mobile repair of existing website','P05','verified homepage overflow at390px; wider accessibility compliance untested','High access benefit; implementation needs technical owner',4,'Specification/retest only included in A; technical upkeep not_estimated','not_confirmed; illustrative external labour EUR600–1800, not quotation','8–14 developer +2–4 accessibility h separately; CMS access; technical scope and later authority','Web maintainer and accessibility function','include specification in A; implementation conditional and separately resourced'],
['Full24-entry funding-directory service','P09','verified scheme rules; need beyond school service untested;6/24 synthesis-rechecked','Useful degree-stage filtering; higher expiry/eligibility maintenance',5,'3.5 h per4-week month; excludes application writing','EUR0 conditional on existing tools/reviewer','Research-support reviewer; existing school service alignment; applicant-specific facts remain private','Research-support administration','defer full service; A uses one checked call card and responsible links'],
['Three-issue research digest as standalone project','P06','real channels and sample content verified; mailing frequency/archive/demand unresolved','Research discovery and participation signposts; recurring editorial obligation',8,'26 total over18wk:19.5 issue work +4.5 monitoring +2 evaluation','EUR0 conditional on existing distribution and archive','4.5 institutional h across18wk; list owner; reviewer; bilingual input','Communications/list administrator and academic editor','defer; C adapts to two issues, not additive'],
['Four external-source discussion sessions','P07','research fit inferred from sources; candidate availability and need unverified','Potential substantive cross-field exchange; larger coordination exposure',10,'32 total over12wk:24 session work +6 coordination +2 evaluation','not_confirmed; fees/travel unresolved; text-only version28 student h conditional EUR0','Academic host; candidates/reading/room; support hours unconfirmed; later outreach authority','Academic convenor with seminar support','defer; candidates are uncontacted proposals'],
['One local half-day paired-source workshop','P08','specific scholarly connection inferred; two usable dossiers and interest unverified','Potential junior contribution and methods feedback; one-off reversible until commitments',21,'8 per event:4.5 delivery +3.5 follow-up; no ongoing series','EUR0 only if essential facilities/fees supplied; optional EUR88–198 excluded; other charges unknown','33 other support/contributor h; two dossiers; convenor; room/access; separate permissions','Academic convenor and events administrator','defer until demand/support; not added to weekly service'],
['Six-page minimum annual research report','P10;P01;P02;P03;P04','bounded annual facts verified; total output/spending/impact unsupported','Useful annual narrative; concentrated editorial cycle',8,'32 per annual cycle:6 capture +24 production +2 archive;40 first-cycle student h','EUR0 conditional on existing text-only hosting','About10 institutional h plus contributor checks; period and editorial queries','Academic editor and administrative/web archive function','defer; optional replacement project, not extra C output'],
['Digital retrospective without digest','P11;P02;P04','14 displayed work identities supported; additional corpus partial; milestone basis explicit','Useful reading guide; bounded editorial alternative',25,'0.5 h/month until freeze; optional discussion adds5 h','EUR0 conditional digital; booklet EUR220–340 and 54h half-day option EUR250–500 excluded','About4 academic/web h; source/rights checks; exact establishment day unknown','Academic editor and web/archive function','contained in C; no separate additive commitment'],
['Full website redesign','P05','observed access problem; full rebuild need unvalidated','Potential access gains but major migration/maintenance dependencies','40–60','ongoing upkeep not_estimated; do not assume A estimate covers new system','Illustrative outside technical work EUR2280–6200 plus unknown tax/hosting; not quote','30–50 design/developer +8–12 accessibility h; CMS ownership; approved scope/budget','Institutional web owner','defer; narrow repair specification first']]

# Explicit inventory links to every available original file, without claiming every scratch file was read.
manifest=['# Input file manifest','',f'Inventory date: {ASOF}. All original files preserved. Links list availability, not a claim of exhaustive reading or successful source retrieval. The synthesis reads reports, coverage, source registers, relevant tables and prototypes; supporting scripts/raw notes are provenance assets.','', '## Shared instructions','', '- [Shared brief and prompt pack](../../prompts_proposal.md)', '- [Summary source map](../../Summary.md)','']
hashes={}
for rid,d in sorted(dirs.items()):
    manifest += [f'## {rid}', '']
    for p in sorted(d.rglob('*')):
        if p.is_file():
            rel=p.relative_to(ROOT)
            st=p.stat()
            hashes[str(rel)]={'size_bytes':st.st_size,'mtime_ns':st.st_mtime_ns}
            target='../'+str(p.relative_to(ROOT/'reports'))
            label=str(p.relative_to(d))
            manifest.append(f'- [{label}]({target})')
    manifest.append('')
(OUT/'input_manifest.md').write_text('\n'.join(manifest),encoding='utf-8')
(WORK/'input_metadata_snapshot.json').write_text(json.dumps(hashes,indent=2,ensure_ascii=False),encoding='utf-8')

tables={
'id_crosswalk.csv':{'columns':cross_fields,'rows':[[r.get(c,'not_found_publicly') for c in cross_fields] for r in cross]},
'reconciliation_log.csv':{'columns':recon_fields,'rows':[[r[c] for c in recon_fields] for r in recon]},
'proposal_comparison.csv':{'columns':comparison_fields,'rows':proposals},
'sources.csv':{'columns':source_fields,'rows':[[r[c] for c in source_fields] for r in sources]},
}
inv=read(OUT/'input_inventory.csv')
tables['input_inventory.csv']={'columns':list(inv[0]),'rows':[[r[c] for c in inv[0]] for r in inv]}
(WORK/'tables.json').write_text(json.dumps(tables,ensure_ascii=False),encoding='utf-8')
summary={'input_files':len(hashes),'input_source_records':len(source_rows),'distinct_input_url_chains':len({stable_source(r['url']) for _,_,r in source_rows}),'crosswalk_rows':len(cross),'reconciliations':len(recon),'synthesis_source_observations':len(sources),'proposals':len(proposals)}
(WORK/'build_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary))
