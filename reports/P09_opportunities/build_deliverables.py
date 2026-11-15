"""Rebuild P09 research tables from the checked component records (stdlib only)."""
from pathlib import Path
import csv, json, collections

BASE = Path(__file__).resolve().parent
FILES = ['research_root.json','research_french_european.json','research_archives_libraries.json','research_societies_partners.json']
packs = [json.loads((BASE / f).read_text()) for f in FILES]
opps = [r.copy() for p in packs for r in p['opportunities']]
sources = [r.copy() for p in packs for r in p['sources']]
sources.append(dict(source_id='P09-SR20',url='https://www.sciencespo.fr/histoire/en/content/centre-history-and-economics-paris-chep/',title='Centre for History and Economics in Paris (CHEP) — alternate route',publisher_or_owner='Sciences Po Centre for History',source_date='date_unknown',accessed_at='2026-11-15',source_type='official institutional page',supports='Alternate route agrees on host and coordinator',retrieval_status='retrieved; indexed crawl two weeks ago; substantive text matches preferred route'))
opmap={r['opportunity_id']:f'P09-O{i:03}' for i,r in enumerate(opps,1)}
srcmap={}; unique=[]; seen={}
for s in sources:
    if s['url'] in seen:
        canonical=seen[s['url']]; srcmap[s['source_id']]=canonical['source_id']
        canonical['supports'] += '; ' + s['supports']
    else:
        seen[s['url']]=s; unique.append(s); srcmap[s['source_id']]=s['source_id']
for r in opps:
    r['opportunity_id']=opmap[r['opportunity_id']]
    r['source_ids']=';'.join(dict.fromkeys(srcmap[s] for s in r['source_ids'].split(';')))
    r['as_of_date']='2026-11-15'
for s in unique:
    for old,new in sorted(opmap.items(),key=lambda p:-len(p[0])):
        s['supports']=s['supports'].replace(old,new)
byid={r['opportunity_id']:r for r in opps}
byid['P09-O003']['combining_rules']='Sciences Po international mobility aid cannot be combined with Erasmus+ (P09-SF20); other overlapping award rules require checking'
byid['P09-O015']['eligible_profiles']="Master's student (graduate-category mapping; individual equivalence unverified); early doctoral student; advanced doctoral student; postdoctoral researcher; other affiliate"
byid['P09-O015']['unresolved_eligibility'] += '; French Master’s equivalence is inferred from graduate-student category, not explicitly named in call'
byid['P09-O020']['eligible_profiles']="other affiliate; doctoral/postdoctoral researchers with eligible RHS membership; Master's membership-category applicability unverified"
for n in range(5,9):
    r=byid[f'P09-O{n:03}']
    r['location_or_nationality_rules']='All nationalities; Germany/Austria/Switzerland: German-area topic/field OR explicitly justified scientific benefit of research-team integration; DAAD-centre route outside Paris still requires German-area topic'
    r['fit_rationale']='Prepare for announced round; opening date unverified. Fit depends on eligible destination and German-area research or explicitly justified research-team integration; verify full rules.'
    r['unresolved_eligibility'] += '; assess alternative research-team-integration route where applicable'
    if n in (6,7,8):
        r['amount_basis'] += '; renewal requires full new dossier and cannot immediately extend first stay'
byid['P09-O021']['location_or_nationality_rules']='International applicants contemplated; British university mentoring affiliation and IHR participation required; UK mobility or visa arrangements to assess individually where applicable'
readiness={
1:'prepare_now_verify_submission_route',2:'monitor_next_call',3:'confirm_individual_administrative_route',4:'closed_do_not_apply',
5:'prepare_for_announced_round_resolve_eligibility',6:'prepare_for_announced_round_resolve_eligibility',7:'prepare_for_announced_round_resolve_eligibility',8:'prepare_for_announced_round',9:'prepare_if_bilingual_project_ready',10:'closed_monitor_new_call',
11:'prepare_if_ABD_equivalent_and_collection_fit',12:'urgent_only_if_project_ready',13:'monitor_next_dated_round',14:'monitor_next_dated_round',15:'expires_tonight_only_if_dossier_and_reference_ready',16:'monitor_early_2027_announcement',17:'closed_future_round_not_confirmed',
18:'prepare_if_existing_paid_member',19:'prepare_if_existing_paid_member',20:'confirm_Paris_venue_and_membership_before_preparing',21:'prepare_if_British_affiliation_and_IHR_participation_feasible_resolve_cutoff',22:'poster_gate_open_confirm_bursary_details',23:'prepare_if_security_topic_and_residency_fit',24:'hold_until_opening_conflict_resolved'}
for i,r in enumerate(opps,1): r['readiness']=readiness[i]

FIELDS='opportunity_id scheme funder official_call_url cycle status eligible_profiles affiliation_rules location_or_nationality_rules eligible_costs amount currency amount_basis award_period application_deadline referee_deadline timezone materials nomination_needed fit_rationale unresolved_eligibility last_verified source_ids'.split()
FIELDS += ['evidence_status','combining_rules','readiness','as_of_date']
SFIELDS='source_id url title publisher_or_owner source_date accessed_at source_type supports retrieval_status'.split()
def write_csv(name, rows, fields):
    with (BASE/name).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
write_csv('opportunities.csv',opps,FIELDS)
write_csv('sources.csv',unique,SFIELDS)
write_csv('id_crosswalk.csv',[{'record_type':'opportunity','research_id':a,'final_id':b} for a,b in opmap.items()]+[{'record_type':'source_alias','research_id':a,'final_id':b} for a,b in srcmap.items() if a!=b],['record_type','research_id','final_id'])
rank_input=[
('Master\'s student',1,18,'Existing paid RHS postgraduate member; research Master in History; prepared project','Broad historical research','Research trip or access costs','3–5 hours','4 Dec; reference must precede submission','Ready to prepare only if existing member'),
('Master\'s student',2,9,'CIERA registration; French/German B1; suitable text','Methods discussion across disciplines','Subsidised training, limited reimbursements','3–6 hours with existing text','7 Dec; no reference listed','Ready to prepare conditionally'),
('Master\'s student',3,3,'Approved compulsory credited mobility >=2 months','Mobility must fit degree','Mobility living/travel support','2–4 administrative hours after approvals','Individual administrative dates','Confirm route; not a short archive-trip grant'),
('Master\'s student',4,5,'Residence/enrolment conflict; qualifying topic or research-team route','German-area sources or justified team integration','Research stay 1–3 months','8–15 hours','20 Apr2027 announced; opening unverified','Prepare for future round after resolving rules'),
('early doctoral student',1,1,'Sciences Po D1–D3; CHEP research connection','Direct institutional and thematic fit','Research, conference or language costs','4–6 hours','11 Dec application /15 Dec reference','Prepare now; check portal route'),
('early doctoral student',2,18,'Existing paid RHS postgraduate member; no previous award','Historical research','Small research expense','3–5 hours','4 Dec; reference first','Prepare if membership and stage fit'),
('early doctoral student',3,7,'Existing doctoral funding; CIERA French residence/enrolment rules','Eligible research or team-integration route','Supplementary research mobility','8–15 hours','20 Apr2027 announced','Prepare later; use O006 if qualifying unfunded status'),
('early doctoral student',4,22,'Poster-stage rules; accepted contribution; lack of institutional attendance funding','Economic/social history','Conference attendance excludes travel','3–5 proposal hours plus later poster work','18 Nov poster gate; bursary deadline unknown','Only prepared proposal; confirm funding separately'),
('advanced doctoral student',1,11,'ABD equivalent; indispensable collections','Collection-specific historical research','Short archival residency','8–15 hours','4 Dec /14 Dec reference','Prepare if collections and stage fit'),
('advanced doctoral student',2,18,'Existing paid RHS postgraduate member; no prior grant','Historical research','Small research expense','3–5 hours','4 Dec; reference first','Prepare conditionally'),
('advanced doctoral student',3,21,'Submit thesis by fellowship-year threshold; British mentor and IHR participation','Economic/social history','One-year research support','12–25 hours','31 Jan; time conflict','Prepare if British affiliation and IHR participation feasible'),
('advanced doctoral student',4,23,'Advanced relevant PhD; international security topic; residency','Narrow international/security focus','Maintenance plus research','12–25 hours','15 Jan /22 Jan references','Prepare only with strong thematic fit'),
('postdoctoral researcher',1,19,'Current paid RHS member; PhD-age/interruptions rule; no prior award','Historical research','Small research costs','3–5 hours','4 Dec; reference first','Prepare conditionally'),
('postdoctoral researcher',2,21,'Recent doctorate; British mentor and IHR participation feasible','Economic/social history','One-year stipend','12–25 hours','31 Jan; time conflict','Prepare conditionally'),
('postdoctoral researcher',3,11,'PhD; indispensable Newberry collections; residence feasible','Collection-specific research','Short archival residency','8–15 hours','4 Dec /14 Dec reference','Prepare if collection fit'),
('postdoctoral researcher',4,8,'PhD <=4 years; French PhD or contract; France residence','Research or justified team integration','Short research mobility','8–15 hours','20 Apr2027 announced','Prepare for future round'),
('other affiliate',1,11,'PhD or ABD equivalent; actual collections fit','Collection-specific historical research','Short archival residency','8–15 hours','4 Dec /14 Dec reference','Independent status permitted; degree still matters'),
('other affiliate',2,14,'Broad access; substantial Hagley collection need','Business/economic/labour history','Research residency','6–12 hours','Next dated round unknown','Monitor'),
('other affiliate',3,20,'Eligible paid RHS member leads; Paris venue unresolved','Collaborative historical research','One-day meeting costs','6–12 application hours; event delivery extra','15 Jan','Resolve venue/membership before claiming ready'),
('other affiliate',4,12,'PhD; collections; 4–9 month residence; no overlapping fellowship','Collection-specific history','Long residential fellowship','12–25 hours','20 Nov /30 Nov references','Only if proposal already developed')]
rankrows=[]
for profile,rank,n,gate,relevance,purpose,burden,deadline,verdict in rank_input:
    r=byid[f'P09-O{n:03}']
    rankrows.append(dict(profile=profile,conditional_check_order=rank,opportunity_id=r['opportunity_id'],eligibility_gate=gate,research_relevance=relevance,funding_purpose=purpose,estimated_applicant_preparation=burden,deadline_readiness=deadline,practical_verdict=verdict,evidence_status='inferred',source_ids=r['source_ids'],as_of_date='2026-11-15'))
write_csv('profile_shortlist.csv',rankrows,list(rankrows[0]))
allowed={'open','upcoming with an officially announced date','closed','recurring but next round unannounced','unverified'}
assert len(opps)==24 and len({r['opportunity_id'] for r in opps})==24
assert len({s['url'] for s in unique})==len(unique)
assert all(r['status'] in allowed for r in opps)
assert all(all(k in r and str(r[k]).strip() for k in FIELDS) for r in opps)
assert all(s in {x['source_id'] for x in unique} for r in opps for s in r['source_ids'].split(';'))
print(json.dumps({'opportunities':len(opps),'sources':len(unique),'statuses':dict(collections.Counter(r['status'] for r in opps)),'evidence_statuses':dict(collections.Counter(r['evidence_status'] for r in opps))},indent=2))
