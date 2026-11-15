"""Generate P05 CSV registers from the bounded audit's saved observations."""
import csv, io, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = '2026-11-15'
sources, pages, keys = [], [], {}

def write_csv(name, columns, rows):
    with (ROOT / name).open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=columns)
        w.writeheader()
        w.writerows(rows)

# Every item below has a full browser snapshot; duplicate keyboard evidence is not a page.
order = ['home-en','home-fr','home-en-index','organisation-en','organisation-fr',
 'people-en','participants-fr','fellows-en','fellows-fr','committee-en','committee-fr',
 'associates-en','associates-fr','students-en','students-fr','visitors-en','visitors-fr',
 'fellows-past-en','fellows-past-fr','students-past-en','visiting-students-en',
 'publications-en','publications-fr','projects-en','projects-fr','events-en','events-fr',
 'seminars-en','seminars-fr','events-sub-en','events-sub-fr','events-upcoming-en',
 'events-upcoming-supported-en','events-recent-en','events-recent-supported-en',
 'grants-en','grants-fr','announcements-en','announcements-fr','contacts-en','contacts-fr',
 'list-en','list-fr','host-en','host-fr','host-en-alias','levy-profile','event-nov17']

issues = {
 'home-en': ('Mobile overflow; homepage H4-only headings; four cover images lack alt; no canonical link in sampled DOM', 'Specify responsive and semantic repairs; preserve current notices'),
 'home-en-index': ('Indexed tool returned 406 but live page loaded; duplicate homepage route', 'Do not report broken; decide preferred URL with webmaster'),
 'home-fr': ('Live notices current; logo goes to English homepage', 'Preserve current content; retain language context'),
 'host-en': ('French language switch goes to host homepage; community scope differs from fellows page', 'Link equivalent CHEP page; reconcile roster scope'),
 'host-fr': ('2019 described as joint centre founding rather than collaboration start', 'Prepare chronology correction for host editor'),
 'host-en-alias': ('Browser resolves content alias to research route; redirect code untested', 'Retain observed mapping and test server behavior before migration'),
 'fellows-en': ('Only Jessica Balguy here; host community also lists Joan Chaker', 'Validate role/category dates and intended scope'),
 'fellows-fr': ('Only Jessica Balguy here; host community also lists Joan Chaker', 'Validate scope in both languages'),
 'people-en': ('Category-first index has no topic overview', 'Add short verified research-topic labels'),
 'participants-fr': ('Category-first index; some category labels retained in English', 'Agree bilingual labels; add topics'),
 'associates-en': ('Names and institutions; no consistent topic or role-date fields', 'Prepare short topics and dated affiliations; verify external profile destinations'),
 'associates-fr': ('Names and institutions; no consistent topic or role-date fields', 'Maintain paired topic and affiliation fields'),
 'students-en': ('2026 cohort clear; one linked path contains encoded space', 'Preserve exact URLs; add topics; test unusual route before migration'),
 'students-fr': ('2026 cohort clear; historical route available', 'Preserve cohort and prior-student links'),
 'visitors-en': ('Current 2025–2027 visitor separated from graduate visitor archive; application policy not given', 'Keep dates; do not imply open visitor applications'),
 'visitors-fr': ('French heading but English visitor biography', 'Translate or disclose language; validate affiliation dates'),
 'fellows-past-en': ('Le Bras 2021–2023 differs from archive since-2023 wording', 'Validate role chronology; preserve historical provenance'),
 'fellows-past-fr': ('Le Bras 2021–2023 differs from archive since-2023 wording', 'Validate alongside English record'),
 'publications-en': ('18 displayed title entries; year and output type not systematic', 'Add verified metadata; retain selected-participant scope'),
 'publications-fr': ('Same 18 title entries; some English auxiliary labels', 'Pair metadata and translate interface labels'),
 'projects-en': ('Resources and dated historical activity linked; project status fields sparse', 'Expose purpose, CHEP relationship and period'),
 'projects-fr': ('Mixed-language wording and titles', 'Translate interface prose; preserve original titles'),
 'events-en': ('Intermediate page points to seminars and conferences without next date', 'Add next-activity summary and clear branch links'),
 'events-fr': ('Intermediate page points to seminars and conferences without next date', 'Pair events overview copy'),
 'seminars-en': ('Three external series links; no dated next-session summary here', 'Link verified next session and series; identify destination language'),
 'seminars-fr': ('Three series links; online-series label English', 'Pair labels and show next confirmed session'),
 'events-sub-en': ('Already separates Centre/supported and Upcoming/Recent', 'Preserve attribution; connect to seminars and year archive'),
 'events-sub-fr': ('Already separates Centre/supported and Upcoming/Recent', 'Preserve attribution and pair archive labels'),
 'events-upcoming-en': ('Empty-state message without dated review or direct seminar return link', 'Date empty state and link seminar/current activity routes'),
 'events-upcoming-supported-en': ('Empty-state message without dated review or direct seminar return link', 'Date empty state; preserve support attribution'),
 'events-recent-en': ('Recent spans 2019–2026; Belonging chronology uncertain', 'Rename Archive with year headings; validate ambiguous event date'),
 'events-recent-supported-en': ('Supported archive includes 2022–2025 items', 'Use Archive and year headings; retain supporter distinction'),
 'grants-en': ('2027 call is clear but long prose; no deadline time/time zone', 'Add concise eligibility/both-deadline summary; request time clarification'),
 'grants-fr': ('Same main terms; accent/wording corrections needed; deadline time unknown', 'Pair summary and proofread French without changing eligibility'),
 'announcements-en': ('Mixed announcements lack systematic posting dates; historical role wording ambiguous', 'Date and type records; reconcile Le Bras role wording'),
 'announcements-fr': ('Mixed English/French archive text; some email-wrapped links', 'Translate interface/summary and use stable direct links after checking'),
 'contacts-en': ('Malformed concatenated Bluesky href; unlabelled map target differs from labelled Paris map', 'Correct href; inspect map target and link labels; verify address spelling'),
 'contacts-fr': ('Office apostrophe encoding artefact; unlabelled map target differs from labelled Paris map', 'Proofread address and inspect map links'),
 'list-en': ('Embedded bilingual registration form loads; no issue archive or submission success established', 'Add clear purpose and fallback contact; do not claim newsletter delivery tested'),
 'list-fr': ('Embedded form route loaded; submission not tested', 'Keep same form language support and context'),
}

def classify(key):
    if key.startswith('home'): return 'homepage','Understand remit; find next action'
    if key.startswith('host'): return 'host_landing','Discover CHEP via host institution'
    if key == 'levy-profile': return 'researcher_profile','Identify researcher and research topics'
    if key == 'event-nov17': return 'event_detail','Find next announced seminar details'
    if key.startswith('list'): return 'subscription_information','Receive notices; understand participation'
    if key.startswith('contacts'): return 'contact','Find public enquiry and location routes'
    if key.startswith('grants'): return 'funding_call','Determine eligibility and deadlines'
    if key.startswith('publications'): return 'selected_publications','Find scholarly outputs'
    if key.startswith('projects'): return 'project_index','Discover research resources and connections'
    if key.startswith('announcements'): return 'news_archive','Find dated institutional news'
    if key.startswith(('events','seminars')): return 'event_archive' if 'recent' in key else 'event_index','Find activities and archives'
    return ('people_archive' if 'past' in key or key=='visiting-students-en' else 'people_directory'),'Identify roles and relevant researchers'

for index,key in enumerate(order,1):
    raw=(ROOT/'evidence'/f'{key}-ax.txt').read_text()
    m=re.search(r'Title: "(.*?)", URL: "(.*?)"',raw)
    assert m, key
    title,url=m.groups()
    if key=='host-en-alias':
        url='https://www.sciencespo.fr/histoire/en/content/centre-history-and-economics-paris-chep/'
    heading=re.search(r'heading (.*?), Value:',raw)
    if heading and 'histecon.fr' in url: title=heading.group(1)
    if key.startswith('home'): title='CHEP homepage — '+('French' if key.endswith('fr') else 'English')
    if key.startswith('list'): title='CHEP news registration — '+('French route' if key.endswith('fr') else 'English route')
    owner='Sciences Po Centre for History' if 'sciencespo.fr' in url else 'CHEP; internal CMS owner unverified'
    sid=f'P05-S{index:03d}'
    keys[key]=(sid,url)
    issue,action=issues.get(key,('No additional issue established in this bounded check','Preserve source and date labels; apply reusable fields if approved'))
    typ,task=classify(key)
    date='date_unknown; copyright year excluded'
    if key.startswith('students') and 'past' not in key: date='Cohort label 2026; page update date unknown'
    if key=='students-past-en': date='Cohorts 2023–2025; page update date unknown'
    if key.startswith('visitors'): date='Visitor period 2025–2027; page update date unknown'
    if key=='visiting-students-en': date='Historical cohort 2021–2022; page update date unknown'
    if key.startswith('grants'): date='Award period 2027; deadlines 2026-12-11 and 2026-12-15; page update date unknown'
    if key=='event-nov17': date='Event date 2026-11-17; page publication date not separately established'
    if key=='events-recent-en': date='Dated entries 2019–2026; latest displayed 2026-07-06/07; undated item present'
    if key.startswith('home'): date='Live upcoming notices for November/December 2026; page update date unknown'
    status='conflicting' if key in ['host-fr','fellows-past-en','fellows-past-fr'] else 'verified'
    sources.append(dict(source_id=sid,url=url,title=title,publisher_or_owner=owner,source_date='date_unknown',accessed_at=DATE,source_type='official_webpage_live_browser',supports=f'{task}; {issue}; evidence/{key}-ax.txt',retrieval_status='retrieved_live_browser; '+('alias_resolved_to_research_route; HTTP_code_untested' if key=='host-en-alias' else 'snapshot_saved')))
    pages.append(dict(page_id=f'P05-P{index:03d}',URL=url,language='fr' if '/fr/' in url else 'en',page_type=typ,apparent_owner=owner,last_update_evidence=date,audience_task=task,issue=issue,evidence_status=status,proposed_action=action,source_ids=sid))

# Indexed observations are retained separately from live observations, even at the same URL.
memo=(ROOT/'research/comparators.md').read_text()
rows=list(csv.DictReader(io.StringIO(memo.split('```csv\n',1)[1].split('```',1)[0])))
sources.extend(rows)
jmemo=(ROOT/'research/journeys.md').read_text()
for line in jmemo.splitlines():
    if not line.startswith('| P05-J-S'): continue
    cells=[x.strip() for x in line.strip('|').split('|')]
    sid,url,title,owner,date,typ,support,status=cells
    sources.append(dict(source_id=sid,url=url,title=title,publisher_or_owner=owner,source_date=date,accessed_at=DATE,source_type=typ,supports=support,retrieval_status=status+'; indexed observation; see live record if available'))

for sid,url,title in [('P05-S049','https://histecon.fr/robots.txt','CHEP robots.txt'),('P05-S050','https://www.histecon.fr/robots.txt','CHEP www robots.txt'),('P05-S051','https://histecon.fr/sitemap.xml','CHEP sitemap.xml')]:
    sources.append(dict(source_id=sid,url=url,title=title,publisher_or_owner='CHEP',source_date='date_unknown',accessed_at=DATE,source_type='site_discovery_endpoint',supports='Attempted site-rules/sitemap discovery only',retrieval_status='local_request_failed_DNS; no crawl undertaken; not verified broken'))

# Expand page inventory to unique retrieved/attempted research and comparator endpoints.
seen={p['URL'] for p in pages}
for s in sources:
    if s['url'] in seen: continue
    seen.add(s['url'])
    failed='failed' in s['retrieval_status']
    pages.append(dict(page_id=f'P05-P{len(pages)+1:03d}',URL=s['url'],language='fr' if '/fr/' in s['url'] else 'en' if s['source_type']!='site_discovery_endpoint' else 'not_applicable',page_type='discovery_or_supporting_source',apparent_owner=s['publisher_or_owner'],last_update_evidence=s['source_date'],audience_task=s['supports'],issue='Tool retrieval failed; public availability unknown' if failed else 'Indexed representation inspected; live usability untested',evidence_status='unverified' if failed else 'verified',proposed_action='Retry through owner/browser if consequential' if failed else 'Use as bounded evidence; do not infer live defects or user impact',source_ids=s['source_id']))

backlog=[]
def item(n, keylist, problem, consequence, priority, fix, setup, recurring, role, dependency, verify, status='verified'):
    backlog.append(dict(issue_id=f'P05-I{n:02d}',affected_URLs=' | '.join(keys[k][1] for k in keylist),observed_problem=problem,user_consequence=consequence,priority_rationale=priority,proposed_fix=fix,setup_hours_estimate=setup,recurring_effort=recurring,required_role=role,dependency=dependency,verification_method=verify,evidence_status=status,source_ids=';'.join(keys[k][0] for k in keylist)))

item(1,['home-en'],'1402px document width at both 1280px and 390px viewports; clipping visible','Mobile visitor must pan to reach core information','P1: directly observed barrier across core journeys','Specify stacked responsive layout, flexible banner and usable navigation','2 student; 6–10 developer','Retest after template changes; about 15 min/month within QA allowance','Student specification; web maintainer implementation','Template/CSS access and staff capacity','Repeat 390px test; broaden 320/768/1280; no ordinary horizontal scrolling')
item(2,['home-en'],'Three H4 headings; no H1–H3; four book images missing alt attributes','Heading navigation and image understanding may be impaired','P1: directly observed semantic defects; impact requires specialist test','One page H1, logical H2s, deliberate informative/decorative alt; check skip/focus behavior','2 student retest; 2–4 developer; 2–4 accessibility reviewer','Check new media/templates in weekly QA','Web maintainer; accessibility reviewer','DOM/template edit permission; review resource','DOM inspection plus keyboard, zoom, contrast and screen-reader checks; no compliance claim')
item(3,['events-en','seminars-en','events-sub-en','events-upcoming-en','events-upcoming-supported-en'],'Current seminar notices and empty conference/workshop branches are separate','Visitor may mistake a narrow empty branch for no forthcoming activity','P1: next-activity task depends on clear scope','Add next verified activity, seminar cross-links, dated empty states; preserve Centre/supported attribution','3 student; publishing time separate','30 min/week event review','Student; event organiser; communications','Confirmed logistics and event access policy','Next dated activity or checked empty state reached within two links')
item(4,['home-en','list-en','contacts-en'],'Notices and contact exist; general participation rules not established','Newcomer may confuse subscription, event access and affiliation','P1: low-cost clarification without inventing services','Prepare participation panel with existing event/list/contact routes and no general admission promise','3 student including bilingual draft','15 min/week within event/participation review','Communications; academic coordinator','Confirm participation wording and mailbox purpose','Tester distinguishes notices, registration and formal affiliation; no form submitted in this audit')
item(5,['grants-en','grants-fr'],'Detailed current call; eligibility and two deadlines embedded in prose; deadline times unknown','Master’s student or other affiliate could misread suitability','P1: imminent 11/15 Dec 2026 deadlines','Eligibility-first bilingual summary; separate application/referee deadline and expiry state','1 student','15 min/week; daily check near deadline only if assigned','Funding administrator; communications','Confirm deadline time/time zone; approved full terms','Tester states first–third-year Sciences Po PhD restriction and both deadlines')
item(6,['host-fr','host-en','organisation-en','organisation-fr'],'Host FR attaches 2019 to joint centre founding; CHEP dates collaboration 2019 and establishment 2022','Reader may repeat incorrect institutional chronology','P1: substantive bilingual factual discrepancy','Prepare matched chronology for host editor; retain Coordinator title','1 student','On institutional change; quarterly check','Academic coordinator; Sciences Po editor','Institutional validation; host editorial access','Approved French/English milestones agree; distinguish collaboration from establishment','conflicting')
item(7,['fellows-en','host-en','fellows-past-en','announcements-en'],'Fellows/host community differ; Le Bras 2021–2023 versus since-2023 archive wording','Directory status or historical affiliation could be misinterpreted','P1: accuracy; scope difference is not proof of wrong role','Confirm roster scopes and periods; preserve dated announcement context','2 student for sample not entire roster','1 hour/month roster review within maintenance allowance','Academic coordinator; directory editor','Authoritative role periods and intended categories','Resolve or flag every sampled discrepancy without assigning unknown end dates','conflicting')
item(8,['people-en','associates-en','students-en','levy-profile'],'Categories/names more visible than comparable research topics','Prospective student needs extra profile reading to identify matches','P2: hypothesised task improvement; no user-test evidence','Pilot six short topic/date cards across categories using source profiles','2 student for limited sample','10–15 min per changed profile within record allowance','Student; academic/subject reviewer','Verified topics and current affiliation','Volunteer identifies two relevant researchers and status; no supervision promise')
item(9,['publications-en','publications-fr'],'18 selected title entries lack systematic year/type metadata','Scholar cannot quickly date or distinguish output types','P2: discoverability; not evidence of missing total output','Pilot verified metadata for six existing cards; clearly label selection','2 student for sample','10–15 min/new card within record allowance','Student; publications editor','Publisher/repository metadata; rights if covers retained','Each pilot card has author, year, type, source and relationship to CHEP')
item(10,['contacts-en','contacts-fr'],'Malformed English Bluesky href; unlabelled differing map link; French encoding artefact','Contact/social/location route can confuse visitors','P1 for social href; P2 for proofreading','Correct known href against FR/home route; inspect map target and address labels','0.5 student; 0.5–1 publisher','Link QA within weekly allowance','Web maintainer; communications','Confirm correct destination; inspect image map behavior','Read href and open corrected public destination; verify location label; do not send enquiry')
item(11,['home-fr','host-en','visitors-fr','projects-fr','announcements-fr'],'Language switches lose context; some French sections retain English prose','French reader may lose page or lack equivalent information','P2: observed parity/navigation differences','Equivalent-page switches; translate/disclose remaining English summaries','2 student for priority routes; 1–2 publisher','15 min/week paired QA shared with other items','Bilingual editor; host editor; web maintainer','Translation capacity and route mapping','Switch sampled pages both ways and preserve topic; critical fields agree')
item(12,['events-recent-en','events-recent-supported-en','students-past-en'],'Recent page spans 2019–2026; unclear Belonging chronology; historical cohorts useful','Readers may mistake archives for current provision','P2: archive clarity and historical preservation','Year labels/return links; refer ambiguous date to organiser; retain URLs','1 student','Monthly archive review shared with roster allowance','Student; event organiser; web maintainer','Programme/date verification; URL map','Current/archive navigation works; no historical record silently deleted','conflicting')
item(13,['home-en','home-en-index','host-en-alias'],'Multiple home aliases; no canonical link in sampled home DOM; host alias already resolves','Indexing/canonical consequences unknown; migration can damage links','P2: prevention; no measured search penalty','Choose canonical policy with owner; preserve exact legacy routes and test redirects if moved','1 student; 1–3 technical if required','After routing change','Web maintainer','Server configuration/CMS access not available','Inspect response chain and canonical metadata; ensure no loops or 404s after approved changes','inferred')

write_csv('sources.csv',['source_id','url','title','publisher_or_owner','source_date','accessed_at','source_type','supports','retrieval_status'],sources)
write_csv('page_inventory.csv',['page_id','URL','language','page_type','apparent_owner','last_update_evidence','audience_task','issue','evidence_status','proposed_action','source_ids'],pages)
write_csv('audit_backlog.csv',['issue_id','affected_URLs','observed_problem','user_consequence','priority_rationale','proposed_fix','setup_hours_estimate','recurring_effort','required_role','dependency','verification_method','evidence_status','source_ids'],backlog)
print({'live_page_observations':len(order),'sources':len(sources),'unique_inventory_URLs':len(pages),'backlog_items':len(backlog)})
