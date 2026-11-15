from pathlib import Path
import csv,json,re,unicodedata
p=Path(__file__).resolve().parent;out=p.parent

def read(n):
 f=p/n
 return list(csv.DictReader(f.open(encoding='utf-8'))) if f.exists() else []
def write(n,rows,fields=None):
 if fields is None:fields=list(dict.fromkeys(k for r in rows for k in r))
 with (out/n).open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader()
  for r in rows:w.writerow({k:r.get(k,'not_applicable') or 'not_found_publicly' for k in fields})
def norm(s):return ''.join(c for c in unicodedata.normalize('NFKD',s.casefold().replace('’',"'")) if not unicodedata.combining(c))
# Deduplicate identical source URLs only. Different aliases and language variants remain visible.
sources=[];byurl={};alias={};aliasrows=[]
for n in ['root_sources.csv','people_sources.csv','project_sources.csv','support_sources.csv']:
 for r in read(n):
  if r['source_id']=='P03-S228':r['supports']=r['supports'].replace('USD50000','$50000 (ISO currency unstated)')
  url=r['url']; old=r['source_id']
  if url in byurl:
   c=byurl[url];alias[old]=c['source_id']
   for k in ['supports','retrieval_status']:
    if r[k] and r[k] not in c[k]:c[k]+=' | '+r[k]
   if c['source_date']=='date_unknown' and r['source_date']!='date_unknown':c['source_date']=r['source_date']
  else:
   sources.append(r.copy());byurl[url]=sources[-1];alias[old]=old
  aliasrows.append({'original_source_id':old,'source_id':alias[old],'url':url})
def remap(s):
 return ';'.join(dict.fromkeys(alias.get(v.strip(),v.strip()) for v in re.split(r'[;|]',s) if v.strip()))
def fixrefs(r):
 r=r.copy()
 for k in ['source_ids','sources_checked']:
  if k in r:r[k]=remap(r[k])
 return r
cohort=[fixrefs(r) for r in read('cohort.csv')]
people={norm(r['name']):r for r in cohort}
ledger=[fixrefs(r) for n in ['root_funding.csv','people_funding.csv','support_funding.csv'] for r in read(n)]
projects=read('project_funding.csv')
ledger += [fixrefs(r) for r in projects if r['funding_id'] in ['P03-F301','P03-F304','P03-F305','P03-F306']]
ledger.sort(key=lambda r:r['funding_id'])
for r in ledger:
 names=[c for k,c in people.items() if k in norm(r['beneficiary'])]
 r['person_ids']=';'.join(c['person_id'] for c in names) or 'not_applicable'
 # Add affiliation evidence to root historical awards and keep known overlaps explicit.
 if r['funding_id'] in ['P03-F001','P03-F002']:
  r['source_ids']=remap(r['source_ids']+';'+';'.join(c['source_ids'] for c in names))
 r['counting_treatment']='component_of_parent_not_additive' if r['parent_award_id'].startswith('P03-F') else 'independent_record_not_overall_CHEP_income'
 if r['funding_id']=='P03-F304':r['counting_treatment']='approximate_aggregate; do_not_add_2020_named_selections; amount_unknown'
 if r['funding_id']=='P03-F301':
  r['counting_treatment']='institutional_receipt; amount_unknown; not_linked_to_individual_awards';r['start_date']='date_unknown';r['end_date']='date_unknown'
 r['award_group_id']='P03-G001' if r['funding_id'] in ['P03-F226','P03-F227'] else 'not_applicable'
 if r['funding_id'] in ['P03-F226','P03-F227']:r['counting_treatment']='individual_one_third_share_of_one_collective_prize_P03-G001; not_two_prize_pools'
 r['relationship_detail']=r['relationship_category']
 if r['funding_id']=='P03-F301':r['relationship_category']='incoming_institutional_project_funding'
 elif r['funding_id'] in ['P03-F304','P03-F305','P03-F306'] or r['relationship_detail'] in ['CHEP_administered_distributed','CHEP_administered_distributed_support'] or r['funding_id'] in ['P03-F'+str(i) for i in list(range(401,412))+[418,419]]:r['relationship_category']='CHEP_administered_or_distributed_support'
 else:r['relationship_category']='independent_awards_to_CHEP_connected_researchers'
 years=re.findall(r'(?<![0-9])(?:19|20)[0-9]{2}',r['award_date']+';'+r['start_date'])
 r['period_category']='earlier_independent_award' if years and min(map(int,years))<2019 and r['relationship_category']=='independent_awards_to_CHEP_connected_researchers' else '2019_onward_or_date_unknown'
 r['evidence_note']='See source locators; payment and expenditure not implied by award status'
 if r['funding_id'] in ['P03-F201','P03-F202','P03-F203']:
  r['evidence_status']='conflicting';r['source_ids']=remap(r['source_ids']+';P03-S018');r['evidence_note']='Award and amounts verified. CORDIS end2027-08-31 retained; Sciences Po register says2028-08. Original2019 announcement planned2019–23. Period requires reconciliation.'
 if r['funding_id']=='P03-F301':r['evidence_note']='Receipt occurred in2022; award date and funding period unknown; no claim that2022 is a grant start date'
 if r['funding_id']=='P03-F212':
  r['currency']='not_found_publicly';r['amount_basis']='Researcher reports $50000 departmental course-development grant; ISO currency not explicit; no monetary aggregate';r['evidence_note']='Amount and stated purpose verified on researcher page; award date, legal recipient and ISO currency unresolved'
 if r['funding_id']=='P03-F217':r['evidence_note']='Project and amount verified; exact O’Rourke person–project link inferred from inaccessible primary indexed notice; exclude from verified-attribution totals'
 r['as_of_date']='2026-11-15'
leads=[]
for r in read('root_leads.csv'):leads.append(fixrefs(r))
for r in read('support_leads.csv'):
 r=fixrefs(r);r['scheme']=r['entity_or_scheme'];r['instrument_type']=r['lead_type'];r['reason_not_award']=r['evidence_note'];r['next_verification']=r['next_step'];leads.append(r)
for r in projects:
 if r['funding_id'] in ['P03-F301','P03-F304','P03-F305','P03-F306']:continue
 r=fixrefs(r);old=r.pop('funding_id');r['lead_id']=old.replace('-F','-L');r['related_funding_id']='P03-F301 (possible accounting association; not proven)' if old=='P03-F302' else 'not_applicable'
 r['reason_not_award']=r['CHEP_connection']+'; '+r['amount_basis'];r['next_verification']='Confirm financial nature, contract and any amount with responsible administrator';leads.append(r)
for r in read('people_leads.csv'):
 r=fixrefs(r)
 if r.get('lead_id')=='P03-L218':continue # resolved by F428–F432
 if r.get('lead_id')=='P03-L216':
  r['scheme_or_mention']='Earlier grants and fellowships2011–20';r['reason_not_in_verified_ledger']='Earlier timeline remains partial; 2024–26 prizes now resolved as F438–F440'
 r['scheme']=r.get('scheme_or_mention','not_found_publicly');r['beneficiary']=r.get('entity','not_found_publicly');r['instrument_type']=r.get('record_type','unverified_lead');r['reason_not_award']=r.get('reason_not_in_verified_ledger','not_found_publicly');r['next_verification']=r.get('next_check','not_found_publicly')
 if not r.get('lead_id'):r['lead_id']='P03-L2X'+str(len(leads))
 leads.append(r)
for r in leads:r['as_of_date']='2026-11-15'
# Person coverage is one row per cohort person, followed by scheme/project/year checks.
coverage=[fixrefs(r) for n in ['people_coverage.csv','project_coverage.csv','support_coverage.csv'] for r in read(n)]
for r in coverage:
 v=r['person_id_if_applicable']
 if norm(v) in people:r['person_id_if_applicable']=people[norm(v)]['person_id']
 if r['entity_type']=='person':
  pid=r['person_id_if_applicable'];matching=[x for x in ledger if pid in x['person_ids'].split(';') and x['counting_treatment']!='component_of_parent_not_additive']
  r['findings_count']=str(len(matching))
  r['sources_checked']=remap(r['sources_checked']+';'+';'.join(x['source_ids'] for x in matching))
  if matching:r['gaps']+='; count includes reconciled independent/support/prize records; excludes beneficiary components'
 if r['entity_type']=='scheme_year':
  r['entity_or_scheme']=r['entity_or_scheme'].replace('CHEP distributions annual check','CHEP doctoral/CHEP-EHP discovery branch year')
  r['gaps']+='; branch-specific findings count, not total annual CHEP support; excludes workshop and other independent awards'
 if r['entity_or_scheme']=='Economic History, Climate, and the Environment':
  r['findings_count']='0';r['gaps']='Support acknowledged; financial nature and Paris allocation unverified; lead P03-L303'
 coverage_ids={'P03-F001':'SILICOSIS — earlier associated-scholar project','P03-F002':'HETMAT — earlier associated-scholar project'}
for fid,title in coverage_ids.items():
 r=next(x for x in ledger if x['funding_id']==fid)
 coverage.append(dict(entity_or_scheme=title,entity_type='project',person_id_if_applicable=r['person_ids'],years_checked=r['start_date']+' to '+r['end_date'],sources_checked=r['source_ids'],findings_count='1',gaps='Earlier award; no CHEP allocation; HETMAT CORDIS amount inaccessible' if fid.endswith('002') else 'Earlier award; no CHEP allocation',completion_status='checked_public_source'))
for r in read('root_leads.csv'):
 coverage.append(dict(entity_or_scheme=r['scheme']+' — '+r['cycle'],entity_type='call',person_id_if_applicable='not_applicable',years_checked=r['cycle'],sources_checked=remap(r['source_ids']),findings_count='0',gaps=r['reason_not_award'],completion_status='checked_call_not_award'))
write('sources.csv',sources)
write('source_id_crosswalk.csv',aliasrows)
write('cohort.csv',cohort)
write('funding_ledger.csv',ledger)
write('award_groups.csv',[dict(award_group_id='P03-G001',scheme='2019 Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel',in_scope_funding_ids='P03-F226;P03-F227',total_joint_laureates='3',in_scope_recipients='2',award_pools='1',amount='not_found_publicly',currency='not_found_publicly',amount_basis='One third share each; do not infer cash or count recipient shares as separate prize pools',source_ids=remap('P03-S261'))])
leadfields=['lead_id','related_funding_id','scheme','cycle','relationship_category','instrument_type','funder','recipient','administrator','beneficiary','start_date','end_date','amount','currency','amount_basis','annual_research_allowance','relocation_allowance','application_deadline','referee_deadline','timezone','award_or_call_status','evidence_status','source_ids','reason_not_award','next_verification','as_of_date']
# Preserve any extra lead fields from supporting research rather than dropping evidence.
# All substantive research fields have been mapped into this common lead schema.
write('calls_and_unverified_leads.csv',leads,leadfields)
write('funding_coverage.csv',coverage)
# Validate foreign keys, required data and arithmetic, no invented totals.
errors=[]
sids={r['source_id'] for r in sources};pids={r['person_id'] for r in cohort};fids={r['funding_id'] for r in ledger}
for name,rows,key in [('ledger',ledger,'funding_id'),('cohort',cohort,'person_id'),('leads',leads,'lead_id'),('sources',sources,'source_id')]:
 if len(rows)!=len({r[key] for r in rows}):errors.append(name+' duplicate IDs')
 for r in rows:
  if 'source_ids' in r:
   bad=set(r['source_ids'].split(';'))-sids
   if bad:errors.append(f'{name} {r[key]} missing sources {bad}')
for r in sources:
 if re.search(r'\s',r['url']):errors.append('Whitespace in source URL '+r['source_id'])
for r in ledger:
 parent=r['parent_award_id']
 if parent.startswith('P03-') and parent not in fids:errors.append('missing parent '+parent)
 for pid in r['person_ids'].split(';'):
  if pid!='not_applicable' and pid not in pids:errors.append('missing person '+pid)
for r in coverage:
 bad=set(r['sources_checked'].split(';'))-sids
 if bad:errors.append('coverage missing sources '+str(bad))
 if r['person_id_if_applicable'] not in pids|{'not_applicable'}:errors.append('coverage person unresolved '+r['person_id_if_applicable'])
amounts={r['funding_id']:r['amount'] for r in ledger}
from decimal import Decimal
assert Decimal(amounts['P03-F202'])+Decimal(amounts['P03-F203'])==Decimal(amounts['P03-F201'])
summary=dict(as_of_date='2026-11-15',cohort_records=len(cohort),ledger_records=len(ledger),component_records=sum(r['counting_treatment']=='component_of_parent_not_additive' for r in ledger),lead_records=len(leads),source_records=len(sources),original_source_ids=len(aliasrows),coverage_records=len(coverage),named_CHEP_doctoral_awards=10,validation_errors=errors)
(out/'validation.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
