from pathlib import Path
import csv,json
p=Path('reports/P10_annual_report'); n=p/'research_notes'
def write(name,fields,rows):
 with (p/name).open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader()
  for r in rows:
   out={}
   for k in fields:
    v=r.get(k,'not_found_publicly' if k in ('doi','isbn') else 'not_applicable')
    if v is None or v=='':v='not_applicable'
    out[k]=';'.join(v) if isinstance(v,list) else v
   w.writerow(out)
sources=[]
for f in ['root_sources.csv','publications_sources.csv','activities_sources.csv','junior_support_sources.csv']:
 sources.extend(csv.DictReader((n/f).open(encoding='utf-8')))
assert len({r['source_id'] for r in sources})==len(sources)
write('sources.csv',['source_id','url','title','publisher_or_owner','source_date','accessed_at','source_type','supports','retrieval_status'],sources)
a=json.loads((n/'activities.json').read_text());r=json.loads((n/'roster_support.json').read_text());w=json.loads((n/'works.json').read_text())
write('activity_inventory.csv',list(a['events'][0]),a['events'])
write('project_resource_inventory.csv',list(a['resources'][0]),a['resources'])
write('roster_inventory.csv',list(r['people'][0]),r['people'])
write('support_inventory.csv',list(r['support'][0]),r['support'])
fields=list(dict.fromkeys(k for row in w for k in row))
write('publication_inventory.csv',fields,w)
period='2025-09-01/2026-08-31'
ind=[]
def indicator(num,title,definition,value,unit,rule,denom,status,ids,owner):
 ind.append(dict(indicator=f'P10-I{num:03d}: {title}',definition=definition,period=period,value=value,unit=unit,counting_rule=rule,denominator=denom,evidence_status=status,source_ids=ids,missing_data_owner_function=owner))
indicator(1,'Paris-linked activity listings','Dated occurrences explicitly supported by CHEP or listed as centre events',11,'unique event listings','P10-A001–A011; separate sessions count once; multi-day conference once; series not additional','11 extracted Paris-linked records; not all CHEP activity','verified','P10-S201;P10-S202;P10-S203;P10-S204;P10-S217','Academic convenor to confirm institutional categories and completeness')
indicator(2,'Shared online seminar listings','Joint online sessions with Paris contribution evidenced at series level',3,'unique event listings','P10-A012–A014; excluded from Paris-only count; institutional co-organisation inferred','3 in-period sessions on inspected joint archive','verified','P10-S209;P10-S210;P10-S211;P10-S212;P10-S213','Joint programme convenor')
indicator(3,'Explicitly held events within core/shared corpus','Occurrences with explicit retrospective delivery wording',4,'documented held events','P10-A001;P10-A012;P10-A013;P10-A014; exclude mere past calendar dates','14 core/shared listings P10-A001–A014; not a completion-rate denominator for all CHEP events','verified','P10-S201;P10-S211;P10-S212;P10-S213','Event convenors for additional delivery evidence')
indicator(4,'Delivery-unverified listings in core/shared corpus','Listed occurrences with no explicit held evidence retrieved',10,'listings with delivery unverified','P10-A002–A011; unknown delivery is not cancellation','14 core/shared listings; 10 plus 4 held equals 14','verified','P10-S201;P10-S202;P10-S203;P10-S204','Event convenors; final junior conference programme')
indicator(5,'Named 2026 doctoral grant recipients','Distinct names in Jan 28 2026 CHEP award announcement',4,'people','P10-F001–F004; merge EN/FR announcement; exclude 2025 and 2027 cohorts','4 names in 2026 cohort announcement; all-applicant and total-beneficiary denominators unknown','verified','P10-S312;P10-S313','Research grant administration for payment and full-year ledger')
indicator(6,'Selected journal contributions dated in period','Distinct editorial and published interview in focused former-fellow follow-up',2,'unique works','P10-W002 and W003 by DOI; issue container W004 excluded; publisher print date used with HAL corroboration','2 qualifying contributions in 8-record focused work inventory; not centre-wide publication denominator','verified','P10-S104;P10-S108;P10-S112','Academic editor and author to reconfirm publication status/date')
indicator(7,'Selected book publication announcements in period','Author-announced book appearance within academic-year boundary',1,'publication announcement for unique book','P10-W001 Sep12 announcement; NOT strict first-publication count; exact release boundary unverified','1 selected in-period book announcement; 18 CHEP entries screened only at listing level','verified','P10-S105;P10-S106;P10-S108','Author or publisher for first release date')
indicator(8,'Total annual CHEP membership','Unique people affiliated at any time in reporting period','not_found_publicly','people','Would deduplicate people and dated roles; current undated roster insufficient','not_found_publicly','unverified','P10-S004;P10-S302;P10-S303;P10-S305;P10-S306','CHEP coordination / research administration')
indicator(9,'Grant award value in reporting period','Awards attributable to CHEP and period; currencies and multi-year periods separated','not_found_publicly','currency-specific award value','Do not multiply 2026 recipients by 2027 call ceiling; no cross-currency total','not_found_publicly','unverified','P10-S307;P10-S312;P10-S313','Research grant administration')
indicator(10,'CHEP expenditure in reporting period','Approved actual spending for the twelve-month period','not_found_publicly','currency-specific expenditure','Awards acknowledgements and expense ceilings are not payments; no estimate','not_found_publicly','unverified','P10-S203;P10-S202;P10-S312','Finance / research administration')
indicator(11,'Attendance','Actual attendance at documented programme events','not_found_publicly','attendance instances','Never infer attendance from programme names or registration; unique people require separate agreed method','not_found_publicly','unverified','P10-S201;P10-S202;P10-S211;P10-S212;P10-S213','Event administration')
indicator(12,'Report readership','Readers of an authorised published annual report','not_found_publicly','readers under agreed measurement definition','Prototype unpublished; no traffic or unique-reader claims','not_applicable for this unpublished prototype','unverified','not_applicable','Web/communications owner')
indicator(13,'Formal training completions','Completed CHEP-attributable training with explicit completion evidence','not_found_publicly','completions','Seminar listings and ongoing PhDs are not training completions','not_found_publicly','unverified','P10-S202;P10-S302;P10-S314','Training convenor / research administration')
write('indicator_register.csv',['indicator','definition','period','value','unit','counting_rule','denominator','evidence_status','source_ids','missing_data_owner_function'],ind)
content=[]
def c(i,section,subject,relation,ids,status,query,rights='Text-only original paraphrase; no image or quotation reproduced; no reuse rights cleared'):
 content.append(dict(item_id=f'P10-C{i:03d}',section=section,subject=subject,CHEP_relationship=relation,source_ids=ids,image_or_quote_rights=rights,fact_check_status=status,editorial_query=query))
c(1,'Page 1 overview','Institutional origins and host','centre institutional context','P10-S002;P10-S004','verified','Q01: confirm reporting convention and institutional credits; no academic-year convention found publicly')
c(2,'Page 1 credit query','Jonathan Levy Coordinator; older FR David Todd','documented current title / older retrieved variant','P10-S001;P10-S004;P10-S006','conflicting','Q01: newer English and host wording used; historical transition date unknown')
c(3,'Page 2 feature','Génard prison history P10-W001','member achievement: former fellow 2021–2022; no CHEP funding established','P10-S104;P10-S105;P10-S106;P10-S108','inferred','Q02: existence and announcement verified; exact first-release boundary and period assignment unresolved; author review')
c(4,'Page 2 feature / page 7','Authority issue and two contributions P10-W002–W004','member achievement: former fellow; container not counted again','P10-S104;P10-S108;P10-S112','verified','Q07: verify online/print chronology and stale forthcoming flag; interview notice metadata only')
c(5,'Page 3 feature','Jessica Balguy colonial land project','CHEP fellow research in progress; dated affiliation established','P10-S016;P10-S020;P10-S303;P10-S320','verified','Q03: appointment interval and year-end milestones; profile may reflect later revisions')
c(6,'Page 3 / page 7 background','Balguy 2020 book and REPAIRS context','earlier member scholarship; not annual CHEP output','P10-S019;P10-S020','verified','Q03: preserve original project credits and confirm preferred reader link')
c(7,'Page 4 feature','Skoglund Landes working paper','visiting researcher connection in period; work in progress','P10-S015;P10-S202;P10-S314','verified','Q04: undated abstract version; confirm year-end findings and Jan27 delivery')
c(8,'Page 4 query','Skoglund career chronology','dated CHEP visit; role wording unresolved','P10-S015;P10-S314;P10-S323','conflicting','Q04: host postdoctoral role from Dec2025 versus author PhD May2026; use visiting researcher')
for i,name,s in [(9,'Francesco Giosuè','P10-S309;P10-S318'),(10,'Rébecca Mathiot','P10-S315'),(11,'Giulio Piumelli','P10-S316'),(12,'Aesa Virely','P10-S317')]:
 c(i,'Page 5 junior researcher',name,'centre-supported: named 2026 doctoral award recipient','P10-S302;P10-S312;P10-S313;'+s,'verified','Q05: confirm year-end description; one dated milestone and actual support use; no impact testimonial inferred')
c(13,'Page 6 programme','Histoires de la vie économique, eight calendar entries','centre-supported at series level; first dated notice gives co-organisation','P10-S202;P10-S320','verified','Q06: confirm each delivery; do not presume attendance or formal training credit')
c(14,'Page 6 programme','Invisible Actors conference P10-A011','centre-supported; cofunding acknowledged','P10-S203;P10-S204;P10-S205','conflicting','Q06: index Nov26–27 vs programme/event Nov27–28; final programme version and held status')
c(15,'Page 6 programme','JCHE/CHEP Workshop P10-A001','co-organised inferred; explicit joint participation','P10-S201;P10-S217','inferred','Q06: held verified; confirm institutional division of work; no claimed outcomes beyond discussion')
c(16,'Page 6 programme','Visualizing Economic Life P10-A002','centre-listed event; centre-organised category provisional','P10-S201;P10-S217','inferred','Q06: confirm institutional organising role and delivery')
c(17,'Page 6 partnership','Three Joint Online seminars P10-A012–A014','shared programme with Paris participation; co-organisation inferred','P10-S209;P10-S210;P10-S211;P10-S212;P10-S213','inferred','Q06: held verified; confirm institutional credit; no Paris attendance/funding inferred')
c(18,'Page 6 partnership','EHC and La matière du politique','shared initiative / wider-network news','P10-S012;P10-S206;P10-S207','verified','Q06: no general import of partner output; eight contextual listings outside core denominator')
c(19,'Page 6 resources','Archives Notariales P10-P002','centre-hosted resource; earlier origin','P10-S214;P10-S215','verified','Q06: no verified annual release or maintenance contribution; keep as standing resource')
c(20,'Page 6 exchange','Chiara Cordelli','Senior Research Fellow 2025–2027; visitor-page role','P10-S305;P10-S327','verified','Q06: exact visit dates and completed annual milestones unknown; no visitor-day metric')
c(21,'Page 7 reading','The Real Economy P10-W005','earlier participant publication highlighted by CHEP','P10-S101;P10-S113','verified','Q07: background only; both 2025 releases before Sep1')
c(22,'Page 8 support','Doctoral recipients, programme credits and joint donor acknowledgement','centre-supported / shared-programme support; distinguish scopes','P10-S312;P10-S313;P10-S202;P10-S203;P10-S012','verified','Q08: no monetary total or expenditure; administration to supply approved figures if desired')
c(23,'Page 8 postscript','2027 studentships call','future centre support opportunity; no award','P10-S307','verified','Q08: recheck before publication; no 2026 amount inferred and no Masters eligibility')
c(24,'Page 8 postscript','Joan Chaker current host listing','undated postdoctoral listing; annual affiliation unverified','P10-S004;P10-S303','unverified','Q08: appointment dates needed before annual inclusion; omission from fellows page not proof of absence')
c(25,'Whole draft','Three thematic conversations','editorial synthesis of selected work; not official programmes','P10-S105;P10-S016;P10-S015;P10-S112','inferred','Academic editor to approve themes; no presumed personal collaboration')
write('content_register.csv',['item_id','section','subject','CHEP_relationship','source_ids','image_or_quote_rights','fact_check_status','editorial_query'],content)
print(json.dumps({'source_records':len(sources),'unique_source_urls':len({s['url'] for s in sources}),'events':len(a['events']),'resources':len(a['resources']),'work_records':len(w),'role_records':len(r['people']),'unique_roster_people':len({x['name'] for x in r['people']}),'support_records':len(r['support']),'indicators':len(ind),'content_items':len(content)},indent=2))
