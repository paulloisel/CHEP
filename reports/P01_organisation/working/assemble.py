import csv,json,re,unicodedata
from pathlib import Path
D=Path(__file__).resolve().parent.parent
W=D/'working'
files=['root','history','partners','history_profiles','paris_roster','associate_profiles','previous_students','remaining_profiles']
data={n:json.loads((W/(n+'.json')).read_text()) for n in files if (W/(n+'.json')).exists()}
# Normalize the final profile supplement while preserving its raw notes.
if 'remaining_profiles' in data:
 sup=data['remaining_profiles']; supurls={z['source_id']:z['url'] for z in sup['sources']}
 owners={'sciencespo.fr':'Sciences Po Centre d’histoire','histecon.fr':'CHEP','eui.eu':'European University Institute','uvsq.fr':'Université de Versailles Saint-Quentin-en-Yvelines','upenn.edu':'University of Pennsylvania','manchester.ac.uk':'University of Manchester','ericmonnet.eu':'Eric Monnet','ehess.fr':'EHESS','parisschoolofeconomics.eu':'Paris School of Economics'}
 for z in sup['sources']:
  z['source_date']=z.get('source_date') or 'date_unknown';z['accessed_at']=z.get('accessed_at',z.get('access_date','2026-11-15'))
  z['publisher_or_owner']=next((owner for domain,owner in owners.items() if domain in z['url']),'not_found_publicly')
  z['source_type']='institutional profile or dated institutional notice' if 'ericmonnet.eu' not in z['url'] else 'author-controlled academic profile'
  z['supports']=z.get('notes') or 'Retrieval attempt; no additional factual claim'
  if z['retrieval_status']=='retrieved':z['retrieval_status']='retrieved via web tool; live HTTP state not independently established'
 preferred={'Anatole Le Bras':'P01-RS05','Marion Fontaine':'P01-RS09','Eric Monnet':'P01-RS11','M’Hamed Oualdi':'P01-RS15','Alexia Yates':'P01-RS18','Liane Hewitt':'P01-RS20'}
 for z in sup['people']:
  z['institution']=z['external_institution'];z['research_themes']='; '.join(z['themes']);z['profile_url']=supurls[preferred[z['name']]]
  z['category']='Paris research associate' if z['name']!='Liane Hewitt' else 'Paris former research fellow'
  z['source_ids']=list(dict.fromkeys(z['formal_role_source_ids']+z['external_role_source_ids']+z['theme_source_ids']))
  z['current_status']=z['profile_check_status']+'; '+z['notes'];z['evidence_status']='conflicting' if z['name']=='Anatole Le Bras' else 'verified'
S=[]; smap={}; byurl={}; notes=[]
def union(a,b):
 return list(dict.fromkeys(a+b))
def sl(x):
 if not x:return []
 return x if isinstance(x,list) else [s.strip() for s in x.split(';') if s.strip()]
def refs(x):return ';'.join(union([], [smap.get(i,i) for i in sl(x)]))
for pack in data.values():
 for s in pack.get('sources',[]):
  sid=s['source_id']; url=s['url']
  if url in byurl:
   z=byurl[url]; smap[sid]=z['source_id']
   for k in ['supports','retrieval_status']:
    if s.get(k) and s[k] not in z[k]:z[k]+=' | Additional observation: '+s[k]
  else:
   z={k:s.get(k,'date_unknown' if k=='source_date' else 'not_found_publicly') for k in ['source_id','url','title','publisher_or_owner','source_date','accessed_at','source_type','supports','retrieval_status']};S.append(z);byurl[url]=z;smap[sid]=sid
P=[]; pmap={}
def norm(n):
 return unicodedata.normalize('NFKC',n).casefold().replace('’',"'").replace('é','e').replace('m’hamed',"m'hamed")
def addperson(p):
 n=p['name']; key=norm(n)
 if key in pmap:
  old=pmap[key]
  for k in ['category','institution','research_themes']:
   nv=p.get(k,'not_found_publicly')
   if nv.startswith('not_'):continue
   if old[k].startswith('not_'):old[k]=nv
   elif nv not in old[k]:old[k]+='; '+nv
  if p.get('profile_url','').startswith('http') and '/annuaire/' in p['profile_url']:old['profile_url']=p['profile_url']
  old['source_ids']=refs(sl(old['source_ids'])+sl(p.get('source_ids')))
  if p.get('evidence_status')=='conflicting':old['evidence_status']='conflicting'
  if p.get('current_status') and p['current_status'] not in old['current_status']:old['current_status']+=' | '+p['current_status']
  return old['person_id']
 z={k:p.get(k,'not_found_publicly') for k in ['name','category','institution','research_themes','profile_url','current_status','evidence_status']};z['evidence_status']=p.get('evidence_status','verified');z['person_id']=f'P01-P{len(P)+1:03}';z['source_ids']=refs(p.get('source_ids',[]));P.append(z);pmap[key]=z
 return z['person_id']
for packname in ['root','history','partners','history_profiles','paris_roster','associate_profiles','previous_students','remaining_profiles']:
 for p in data.get(packname,{}).get('people',[]):addperson(p)
# Organisations resolve every role and edge endpoint; aliases are local keys only.
O=[]; omap={}
def org(key,name,short,location,kind,url,src,status='verified',aliases=()):
 z=dict(organisation_id=f'P01-O{len(O)+1:03}',official_name=name,short_name=short,location=location,institutional_type=kind,official_url=url,evidence_status=status,source_ids=refs(src));O.append(z)
 for a in [key,name,short,*aliases]:omap[a]=z['organisation_id']
 return z['organisation_id']
org('paris_che','Centre for History and Economics in Paris','CHEP','Paris, France','research centre','https://www.histecon.fr/en/',['P01-SR03','P01-SR04'],aliases=['Centre for History and Economics in Paris (CHEP)'])
org('chsp','Centre d’histoire de Sciences Po','CHSP','Paris, France','Sciences Po research centre / host unit','https://www.sciencespo.fr/histoire/',['P01-SR03','P01-SR08'],aliases=['Centre d’histoire de Sciences Po (CHSP)','Sciences Po Centre for History'])
org('sciencespo','Sciences Po','Sciences Po','Paris, France','higher education and research institution','https://www.sciencespo.fr/',['P01-SR03'])
org('cso','Centre de sociologie des organisations','CSO','Paris, France','research unit; historical CHEP base','https://www.sciencespo.fr/cso/',['P01-SR06','P01-SR10','P01-H003'],aliases=['Centre de sociologie des organisations (CSO)','Centre for the Sociology of Organisations (CSO)'])
org('economics','Department of Economics, Sciences Po','Sciences Po Economics','Paris, France','department','https://www.sciencespo.fr/department-economics/',['P01-SR11'])
org('paris_exec','Executive Committee — CHEP','CHEP Executive Committee','Paris, France','governance page/body label; current composition unverified','https://histecon.fr/en/executive_committee.html',['P01-SR02'])
org('paris_council','Conseil scientifique — Centre for History and Economics in Paris','CHEP scientific council','Paris, France; international participants','scientific advisory body; historical composition attested','https://www.sciencespo.fr/sites/default/files/cd_cp/cs/2020/2020_03_10_CSFR.pdf',['P01-H003','P01-SR09'])
for o in data.get('partners',{}).get('organisations',[]):org(o['key'],o['official_name'],o['short_name'],o['location'],o['institutional_type'],o['official_url'],o['source_ids'])
org('lviv','Center for Urban History','Center for Urban History, Lviv','Lviv, Ukraine','research centre; fellowship host','https://www.lvivcenter.org/',['P01-H013'],aliases=['Center for Urban History, Lviv'])
org('eui','European University Institute','EUI','Fiesole / Florence, Italy','higher education and research institution','https://www.eui.eu/',['P01-RS15','P01-RS16','P01-RS18'])
org('duke','Duke University','Duke','Durham, North Carolina, USA','university','https://www.duke.edu/',['P01-AS04'])
org('penn','University of Pennsylvania','Penn','Philadelphia, Pennsylvania, USA','university','https://www.upenn.edu/',['P01-RS20'])
org('uvsq','Université de Versailles Saint-Quentin-en-Yvelines','UVSQ','Versailles / Saint-Quentin-en-Yvelines, France','university','https://www.uvsq.fr/',['P01-RS06'])
R=[]
def role(name,title,orgkey,start='date_unknown',end='date_unknown',precision='undated listing accessed 2026-11-15; appointment dates unknown',status='verified',src=(),note=''):
 key=norm(name)
 if key not in pmap:
  addperson(dict(name=name,category='historical Paris governance',institution='not_found_publicly',research_themes='not_found_publicly',profile_url='not_found_publicly',current_status='historical role only; current CHEP membership unverified',evidence_status=status,source_ids=list(src)))
 oid=omap.get(orgkey,orgkey)
 for prev in R:
  if (prev['person_id'],prev['role_exact'],prev['organisation'],prev['start_date'],prev['end_date'])==(pmap[key]['person_id'],title,oid,start,end):
   prev['source_ids']=refs(sl(prev['source_ids'])+list(src))
   if precision not in prev['date_precision']:prev['date_precision']+=' | '+precision
   if note:notes.append(dict(record_id=prev['role_id'],evidence_note=note,source_ids=refs(src)))
   return prev['role_id']
 rid=f'P01-R{len(R)+1:03}'
 pmap[key]['source_ids']=refs(sl(pmap[key]['source_ids'])+list(src))
 if oid==omap.get('paris_council') and '2020' in precision and 'historical Paris scientific council' not in pmap[key]['category']:pmap[key]['category']+='; historical Paris scientific council'
 assert oid in {x['organisation_id'] for x in O},(name,orgkey)
 R.append(dict(role_id=rid,person_id=pmap[key]['person_id'],role_exact=title,organisation=oid,start_date=start,end_date=end,date_precision=precision,evidence_status=status,source_ids=refs(src)))
 if note:notes.append(dict(record_id=rid,evidence_note=note,source_ids=refs(src)))
 return rid
role('Jonathan Levy','COORDINATOR','paris_che',src=['P01-SR01','P01-SR03'],precision='listed current; effective start/end unknown')
role('Jonathan Levy','Professor','chsp',src=['P01-SR07'],precision='listed current; effective start/end unknown')
role('Mary-Rose Cheadle','Coordination with CHE-Cambridge and CHE-Harvard','paris_che',src=['P01-SR01'],precision='listed current; effective start/end unknown')
role('Amy Price','Web architect','paris_che',src=['P01-SR01'],precision='listed current; effective start/end unknown')
for name in ['Marie-Emmanuelle Chessel','Thierry Mayer','Paul-André Rosental','Emma Rothschild']:
 role(name,'avec le concours de','paris_che',src=['P01-SR06'],precision='named on current host overview; exact tenure unknown',note='Descriptive source wording for helping organise CHEP activities, not an executive-committee title or formal reporting line.')
role('Paul-André Rosental','Membre de Conseils scientifiques','paris_council',src=['P01-SR09'],precision='listed on current profile; exact tenure unknown',note='Profile explicitly includes Centre for History and Economics-Paris in the list.')
role('Paul-André Rosental','directeur du Centre d’histoire de Sciences Po','chsp','2022','2025','year','verified',['P01-SR09'])
role('Paul-André Rosental','Directeur scientifique de Sciences Po','sciencespo',src=['P01-SR09'],precision='listed current; exact tenure unknown')
for name,title in data['root']['host_support']:
 if norm(name) not in pmap:addperson(dict(name=name,category='host-unit function; not automatically CHEP staff',institution='Sciences Po Centre for History (CHSP)',research_themes='not_applicable' if name not in ['Guillaume Piketty','Marion Fontaine','David Todd','Nicolas Delalande'] else 'not_found_publicly',profile_url='https://www.sciencespo.fr/histoire/en/the-centre/research-directorate-and-support-team/',current_status='listed current CHSP function; CHEP-specific remit not established',evidence_status='verified',source_ids=['P01-SR08']))
 else:
  p=pmap[norm(name)];p['category']+='; host-unit function';p['source_ids']=refs(sl(p['source_ids'])+['P01-SR08'])
 role(name,title,'chsp',src=['P01-SR08'],precision='listed current host-unit function; CHEP-specific remit not established')
for r in data.get('history',{}).get('roles',[]):
 if r['role_exact']=='COORDINATEUR':continue # preserve conflicting evidence on dated coordination record/person; no duplicate undated appointment
 ok='paris_council' if ('conseil scientifique' in r['role_exact']) else r['organisation']
 title,status,note=r['role_exact'],r['evidence_status'],r.get('evidence_note','')
 if r['name']=='David Todd' and 'Coordinatrice' in title:
  note+=' Exact CV wording for Claire: Coordinatrice, avec David Todd. Todd co-coordination relationship is explicit; masculine title is editorial normalization.'
  title='co-coordinator [normalized label from CV entry]';status='inferred'
 role(r['name'],title,ok,r['start_date'],r['end_date'],r['date_precision'],status,r['source_ids'],note)
for r in data.get('partners',{}).get('roles',[]):
 if r['role_exact']=='Co-director':continue # wording variant of same Yang appointment
 role(r['person'],r['role_exact'],'harvard_executive' if r['role_exact']=='Executive Committee' else r['organisation'],r['start_date'],r['end_date'],r['date_precision'],r.get('evidence_status','verified'),r['source_ids'])
# Separate observed cohort dates from effective tenure bounds.
for packname in ['paris_roster','previous_students']:
 for r in data.get(packname,{}).get('roles',[]):
  start,end,precision=r['start_date'],r['end_date'],r['date_precision']
  if any(t in precision.lower() for t in ['cohort year','cohort_year','selection year','selection_year']):
   precision+='; observed cohort/selection='+start+'; effective appointment/award start and end unknown'
   start=end='date_unknown'
  role(r['name'],r['role_exact'],r['organisation'],start,end,precision,r.get('evidence_status','verified'),r['source_ids'],r.get('evidence_note',''))
# Explicit support recipients from announcement archive, without residency assumptions.
for name,cat,title,profile in [
 ('Jingyi Huang','historical EHP-CHEP fellow','EHP-CHEP fellow','https://histecon.fr/en/announcements_archive.html'),
 ('Ivanna Cherchovych','CHEP-supported non-residential fellow at Lviv','recipient [non-residential fellowship for scholars at risk]','https://histecon.fr/en/announcements_archive.html')]:
 addperson(dict(name=name,category=cat,institution='Center for Urban History, Lviv (fellowship host)' if name.startswith('Ivanna') else 'not_found_publicly',research_themes='not_found_publicly',profile_url=profile,current_status='historical or undated announcement; current CHEP membership not established',evidence_status='verified',source_ids=['P01-H013']))
 role(name,title,'paris_che',src=['P01-H013'],precision='undated archive attestation; effective tenure unknown',note='Support/participation is explicit; no Paris residence or permanent membership inferred.')
# Keep dated offer separately from undated recipient announcement: no invented award start date.
role('Ivanna Cherchovych','propose une bourse','paris_che',src=['P01-SR06'],precision='offer described as autumn 2022; individual award effective dates unknown',note='Host page offer wording is distinct from archive recipient announcement. The combination does not establish the award duration.')
# Named publication participants: all 15 author identities in checked page, not a bibliography census.
for item in data['history'].get('boundary_examples',[]):
 for name in item.get('publication_page_authors',[]):
  if norm(name) not in pmap:
   addperson(dict(name=name,category='publication participant only in checked corpus',institution='not_found_publicly',research_themes='not_found_publicly',profile_url='https://histecon.fr/en/publications.html',current_status='featured participant; Paris membership not established by publication appearance',evidence_status='verified',source_ids=['P01-H012']))
  else:
   p=pmap[norm(name)];p['category']+='; featured publication participant';p['source_ids']=refs(sl(p['source_ids'])+['P01-H012'])
  role(name,'participants [publication-page heading]','paris_che',src=['P01-H012'],precision='undated feature; not a membership tenure',note='This record establishes featured participation only; other membership needs separate evidence.')
addperson(dict(name='Angus Burgin',category='event participant only in checked corpus',institution='Johns Hopkins University (2023 event description)',research_themes='not_found_publicly',profile_url='https://www.sciencespo.fr/histoire/en/events/centre-for-history-and-economics-in-paris-chep/',current_status='2023 event speaker; current CHEP membership not established',evidence_status='verified',source_ids=['P01-H007']))
role('Angus Burgin','speaker [event participation, not appointment]','paris_che',src=['P01-H007'],precision='event date 2023-11-29; not a membership tenure',note='CHEP-labelled host event was at Harvard. No Paris appointment is inferred.')
# Material dated external affiliations are separate from Paris associate status.
role('Mélanie Lamotte','Assistant Professor of History','duke','2024','date_unknown','year; profile says 2024–present','verified',['P01-AS04'])
role('M’Hamed Oualdi','Full-time Professor','eui','2024-09','date_unknown','month; joining notice and current institutional profile','verified',['P01-RS15','P01-RS16'])
role('M’Hamed Oualdi','Professeur des universités (en détachement)','chsp','2024-09-01','date_unknown','day precision for start of secondment, not original professorial appointment','verified',['P01-RS14'])
role('Alexia Yates','Full-time Professor','eui','2024-09','date_unknown','month; joining notice and current institutional profile','verified',['P01-RS18','P01-RS16'])
role('Liane Hewitt','Assistant Professor of History','penn','2025-07-05','date_unknown','day; Sciences Po specifies recruitment effective date; Penn confirms current title','verified',['P01-RS06','P01-RS20'])
role('Anatole Le Bras','maître de conférences en histoire contemporaine','uvsq',src=['P01-RS06'],precision='attested under Automne 2024; exact appointment start/end unknown')
role('Anatole Le Bras','chercheur post-doctorant','paris_che','2023-09','date_unknown','month; 2024-01-23 event biography says joined September 2023','conflicting',['P01-RS07','P01-SA04'],note='Direct conflict with past-fellows roster 2021–2023; retain both claims pending institutional correction.')
# Clear misleading historical-only shorthand when a current associate listing was found.
assoc_names={norm(x['name']) for x in data.get('paris_roster',{}).get('people',[]) if 'associate' in x.get('category','')}
for p in P:
 if norm(p['name']) in assoc_names:
  extra=' Historical appointments/other functions are separately dated in roles.csv.'
  p['current_status']='Listed Research Associate on checked CHEP roster; effective appointment dates unknown.'+extra
 if p['name']=='Anatole Le Bras':
  p['evidence_status']='conflicting';p['current_status']+=' Former-fellow date conflict: past-fellows page 2021–2023; homepage since 2023.';p['source_ids']=refs(sl(p['source_ids'])+['P01-SR04'])
 if p['name']=='David Todd':p['current_status']='Historical co-coordinator 2019–2021; coordinator since 2022 attested 2025-07-21. Current CHEP/host listings name Levy; older profile wording conflicts; transition date unknown. Current CHSP doctoral-studies function separately listed.'
 if p['name']=='Jonathan Levy':p['current_status']='Listed current Coordinator and Research Associate; Professor at CHSP; effective CHEP appointment dates unknown.'
 # Collapse repetitive missing-value variants.
 if p['research_themes'].startswith('not_found_publicly'):p['research_themes']='not_found_publicly'
# Prefer newer explicitly sourced external affiliations while retaining roster discrepancies.
for z in data.get('remaining_profiles',{}).get('people',[]):
 p=pmap[norm(z['name'])];p['profile_url']=z['profile_url'];p['institution']=z['institution']
 if z['name']=='Alexia Yates':p['institution']+=' (joined September 2024; CHEP roster still says Manchester)'
 if z['name']=='M’Hamed Oualdi':p['institution']+=' (EUI September 2024; Sciences Po secondment from 2024-09-01; CHEP roster says Sciences Po)'
 if z['name']=='Anatole Le Bras':p['current_status']+=' Dated Sciences Po biography says joined CHEP September 2023, conflicting with former-fellows interval.'
 if z['name']=='Liane Hewitt':p['current_status']='Former CHEP fellow 2024–2025; current Penn Assistant Professor; not listed as current Paris associate.'
for packname in ['associate_profiles','history_profiles','remaining_profiles']:
 for p in data.get(packname,{}).get('people',[]):
  if p.get('notes') or p.get('evidence_note'):notes.append(dict(record_id=pmap[norm(p['name'])]['person_id'],evidence_note=p.get('notes',p.get('evidence_note','')),source_ids=refs(p['source_ids'])))
for n in data.get('history_profiles',{}).get('name_reconciliation',[]):notes.append(dict(record_id=pmap[norm(n['canonical_name'])]['person_id'],evidence_note='Identity reconciliation (inferred): '+n['source_name']+' -> '+n['canonical_name']+'. '+n['rationale'],source_ids=refs(n['source_ids'])))

E=[]
def edge(a,b,typ,dates,status,src):
 def endpoint(v):
  if v in omap:return omap[v]
  if norm(v) in pmap:return pmap[norm(v)]['person_id']
  return v
 E.append(dict(edge_id=f'P01-E{len(E)+1:03}',from_id=endpoint(a),to_id=endpoint(b),relationship_type=typ,valid_dates=dates,evidence_status=status,source_ids=refs(src)))
edge('paris_che','chsp','hosted at','current public overview; established 2022','verified',['P01-SR03','P01-SR04'])
edge('chsp','sciencespo','research centre of','observed 2026-11-15; effective dates unknown','verified',['P01-SR03','P01-SR08'])
edge('cso','sciencespo','research unit at','observed 2026-11-15','verified',['P01-SR10'])
edge('economics','sciencespo','department of','observed 2026-11-15','verified',['P01-SR11'])
edge('paris_exec','paris_che','listed People governance branch; membership unverified','observed 2026-11-15','verified',['P01-SR02'])
edge('paris_council','paris_che','scientific council of','historical composition attested 2020-03-10; current individual profile corroboration','verified',['P01-H003','P01-SR09'])
for e in data.get('history',{}).get('relationships',[]):edge(e['from_name'],e['to_name'],e['relationship_type'],e['valid_dates'],e['evidence_status'],e['source_ids'])
for e in data.get('partners',{}).get('relationships',[]):edge(e['from'],e['to'],e['relationship_type'],e['valid_dates'],e.get('evidence_status','verified'),e['source_ids'])
edge('Mary-Rose Cheadle','cambridge_che','coordinates with (CHEP remit)','listed current; exact dates unknown','verified',['P01-SR01'])
edge('Mary-Rose Cheadle','harvard_che','coordinates with (CHEP remit)','listed current; exact dates unknown','verified',['P01-SR01'])
# Keep semicolon categories and themes deduplicated.
for p in P:
 for k in ['category','research_themes']:
  p[k]='; '.join(dict.fromkeys(v.strip() for v in p[k].split(';') if v.strip()))
# All roles have graph counterparts; labels do not imply supervision.
for r in R:
 edge(r['person_id'],r['organisation'],'holds/listed role: '+r['role_exact'],r['date_precision']+'; start='+r['start_date']+'; end='+r['end_date'],r['evidence_status'],sl(r['source_ids']))

def write(name,fields,rows):
 with (D/name).open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
write('people.csv','person_id,name,category,institution,research_themes,profile_url,current_status,evidence_status,source_ids'.split(','),P)
write('organisations.csv','organisation_id,official_name,short_name,location,institutional_type,official_url,evidence_status,source_ids'.split(','),O)
write('roles.csv','role_id,person_id,role_exact,organisation,start_date,end_date,date_precision,evidence_status,source_ids'.split(','),R)
write('relationships.csv','edge_id,from_id,to_id,relationship_type,valid_dates,evidence_status,source_ids'.split(','),E)
write('sources.csv','source_id,url,title,publisher_or_owner,source_date,accessed_at,source_type,supports,retrieval_status'.split(','),S)
write('evidence_notes.csv',['record_id','evidence_note','source_ids'],notes)
write('source_id_crosswalk.csv',['input_source_id','canonical_source_id'],[dict(input_source_id=a,canonical_source_id=b) for a,b in smap.items()])
ids=[dict(person_id=p['person_id'],identifier_type='canonical_or_source_profile_url',identifier=p['profile_url'],source_ids=p['source_ids']) for p in P if p['profile_url'].startswith('http')]
for name,identifier,src in [('Marie-Emmanuelle Chessel','0000-0002-7501-834X',['P01-SR10']),('Thierry Mayer','0000-0003-2098-3887',['P01-SR11']),('Francesca Trivellato','0000-0001-6864-1451',['P01-PS13']),('Alexia Yates','0000-0002-0743-0658',['P01-SA28'])]:ids.append(dict(person_id=pmap[norm(name)]['person_id'],identifier_type='ORCID linked by institutional profile',identifier=identifier,source_ids=refs(src)))
write('identifiers.csv',['person_id','identifier_type','identifier','source_ids'],ids)
profile_rows=[]
for p in P:
 missing=p['research_themes'].startswith('not_')
 profile_rows.append(dict(person_id=p['person_id'],name=p['name'],profile_url=p['profile_url'],theme_status='not_applicable' if p['research_themes']=='not_applicable' else ('not_found_publicly' if missing else 'sourced'),coverage_note=('Selected profile URL: '+byurl[p['profile_url']]['retrieval_status']) if p['profile_url'] in byurl else 'Selected profile URL observed as a link; no separately retrieved body in source register. Other sourced themes/affiliations may come from roster or alternate profile.',source_ids=p['source_ids']))
write('profile_coverage.csv',['person_id','name','profile_url','theme_status','coverage_note','source_ids'],profile_rows)
(D/'working'/'entity_lookup.json').write_text(json.dumps(dict(people={p['name']:p['person_id'] for p in P},organisations=omap),ensure_ascii=False,indent=2))
print(json.dumps(dict(people=len(P),roles=len(R),organisations=len(O),relationships=len(E),sources=len(S)),indent=2))
