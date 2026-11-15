import csv,json
from pathlib import Path
p=Path('reports/P04_timeline/research/partners')
A='2026-11-15'; base='https://histecon.fas.harvard.edu/seminars/'
sources=[]
def src(n,url,title,supports,status='retrieved via web open; indexed/cached crawl displayed; live origin not independently verified',owner='Joint Center for History and Economics / Harvard University',date='date_unknown'):
 s=dict(source_id=f'P04-N{n:03}',url=url,title=title,publisher_or_owner=owner,source_date=date,accessed_at=A,source_type='official institutional webpage',supports=supports,retrieval_status=status);sources.append(s);return s['source_id']
src(1,base+'past_seminars.html','Joint Center for History and Economics Online Seminar — Past seminars','31 dated seminar notices, 20 May 2020 to 1 April 2026; archive classification alone not proof held')
src(2,base+'index.html','Joint Center for History and Economics Online Seminar — Welcome and Introduction','Explicit Cambridge/Harvard/Paris audience and CHEP series footer; 28 October 2026 Adelman announcement. Open returned fall schedule whereas search index had older forthcoming-programme text.')
src(3,base+'organisers.html','Joint Center for History and Economics Online Seminar — Organisers','Current list Diana Kim, Ian Kumekawa, David Todd; appointment dates unknown; do not backdate to all events')
src(4,'https://histecon.fas.harvard.edu/seminars.htm','Center for History and Economics — Seminars','Navigation to online series; alternative organiser list also includes Surabhi Ranganathan; conflicting with dedicated current organisers page')
src(5,'https://histecon.fas.harvard.edu/ehc/activities_recent.html','Economic History, Climate, and the Environment — Events Archive','Held evidence: 26 June 2025 New Paths; 24 May 2024 Emotions climate environment, CHEP-funded; Paris Climate and Capitalism 2024–25; excludes wider network events lacking Paris link')
src(6,'https://histecon.fas.harvard.edu/ehc/','Economic History, Climate, and the Environment','Three-centre initiative; Paris seminar La matière du politique linked; no inference of Paris organisation of every item')
src(7,'https://histecon.fas.harvard.edu/recent_events.html','Center for History and Economics — Recent Events','Partner workshop branch 2004–26 inspected selectively for Paris-specific links; 2023 Delalande and 2025 Levy are Harvard talks with Sciences Po speakers, not evidence CHEP organised')
src(8,'https://www.sciencespo.fr/histoire/fr/les-formations/les-etudes-doctorales/le-colloque-junior/','Le Colloque junior','Explicit CHEP support for Valuing Empires 2022 and La vie matérielle des déplacés 2023. Sent to workshop researcher.',owner='Sciences Po Centre d’histoire')
src(9,'https://www.histecon.magd.cam.ac.uk/chep/','Historical CHEP project branch','Historical entry point inaccessible','failed web open: cache miss; non-www alias inaccessible',owner='Centre for History and Economics / University of Cambridge')
src(10,'https://www.histecon.magd.cam.ac.uk/','Centre for History and Economics — Cambridge home','Partner entry point inaccessible','failed web open: 403 Forbidden',owner='Centre for History and Economics / University of Cambridge')
src(11,'https://www.histecon.magd.cam.ac.uk/new_paths/','New Paths in Environmental History','Harvard-linked 2025 workshop page inaccessible; Harvard archive supplies retrospective held evidence','failed web open: error fetching',owner='Centre for History and Economics / University of Cambridge')
src(12,'https://histecon.fas.harvard.edu/robots.txt','robots.txt','Site rules probe; no automated bulk crawl performed','failed web open; shell network DNS unavailable')
src(13,'https://histecon.fas.harvard.edu/sitemap.xml','Sitemap probe','Sitemap unavailable','failed web open: inaccessible')
src(14,'https://histecon.fas.harvard.edu/events_main.html','Center for History and Economics — Events','Navigation mapping to workshops and seminars')
src(15,'https://histecon.fas.harvard.edu/events-sub.htm','Center for History and Economics — Conferences, Meetings and Workshops','Navigation mapping upcoming/recent workshop branches')
src(16,'https://histecon.fas.harvard.edu/events.htm','Center for History and Economics — Future Events','Upcoming branch inspected; no additional Paris-specific event established')
# Data from dated catalogue, checked against each linked detail where available. All title strings are event metadata.
data='''2020-05-20|Emma Rothschild|History and Distance: a Cholera Epidemic in 1855|archive|announced|epidemics; spatial history|Online joint seminar
2020-06-17|Paul-André Rosental|The First Thirty Days: The Covid Crisis and Public Health Policies|archive|announced|public health; Covid-19|Online joint seminar
2020-07-15|Rohit De|States of Emergency|archive|announced|law; emergencies|Online joint seminar
2020-09-23|Surabhi Ranganathan|Unmaking the Ocean|ranganathan|announced|ocean; legal history|Online joint seminar
2020-10-14|Esther Duflo|Every child counts: what children know, what they don’t know and what can be done about it|archive|announced|education; development economics|Online joint seminar
2020-11-18|Sunil Amrith|The Air as an Archive|amrith|announced|environment; archives|Online joint seminar
2021-01-27|Paul Warde|Strategy and Tactics in the Environmental Revolution|warde|announced|environmental history|Online joint seminar
2021-02-17|Francesca Trivellato|The Vagrancy of Economic Invisibility|trivellato|documented as held|credit; economic invisibility|Online joint seminar
2021-05-12|Jonathan Levy|Does Capital Flow?|levy|announced|capital; economic history|Online joint seminar
2021-06-16|Claire Zalc|Discretionary Power in the Hands of an Authoritarian State: Denaturalizations under the Vichy Regime, 1940-1944|zalc|documented as held|citizenship; state power|Online joint seminar
2021-07-14|Arunabh Ghosh|The Significance of Small Things: Towards a History of Dam Building in the Twentieth Century|ghosh|documented as held|dams; environment; China|Online joint seminar
2021-09-15|Nicolas Barreyre; Claire Lemercier|The Unexceptional State: Rethinking the State in the Nineteenth Century (France, United States)|barreyre_lemercier|documented as held|state formation; comparative history|Online joint seminar
2021-10-13|Vanessa Ogle|Histories of Capitalism: the View from Offshore|ogle|documented as held|capitalism; tax havens|Online joint seminar
2021-11-17|Nikolas Bowie|The Judicial Counterrevolution to Reconstruction|bowie|announced|law; Reconstruction|Online joint seminar
2022-01-12|Diana Kim|Colonial States and their Legacies across Southeast Asia: Through the Lens of Japan's Wartime Empire|kim|documented as held|colonial state; Southeast Asia|Online joint seminar
2022-02-16|Fei-Hsien Wang|Bicycle Thieves, Peanut Tenants, and a Disputed Temple: Reconfiguring Value and Economic Life in Post-World War II China (1945-1949)|wang|documented as held|law; value; China|Online joint seminar
2022-03-16|Debjani Bhattacharyya|Between Opacity and Precision: Underwriting Weather in the British Empire|bhattacharyya|documented as held|climate; insurance; empire|Online joint seminar
2023-02-08|Namrata Kala|Money (Not) to Burn: Payments for Ecosystem Services to Reduce Crop Residue Burning|kala|announced|environmental economics; payments|Online joint seminar; physical venue not_found_publicly
2023-03-08|Shane Bobrycki|Economic Welfare and Demographic Decline: The Case of the Early Middle Ages|bobrycki|documented as held|demography; welfare; medieval history|Harvard, Lee Gathering Room CGIS S030; Zoom
2023-04-26|Brandon Terry|Malcolm X and the Rhetoric of Black Populism|terry|documented as held|political thought; class; race|Harvard, Lee Gathering Room CGIS S030; Zoom
2023-10-18|Rana Mitter|Money, morale and mayhem: economic and emotional landscapes in Civil War era China, 1946-9|mitter|documented as held|China; economic life; emotions|Online joint seminar; physical venue not_found_publicly
2023-11-08|Julia Cagé|A History of Political Conflict: Elections and Social Inequalities in France, 1789-2022|cage|documented as held|elections; inequality; France|Online joint seminar; physical venue not_found_publicly
2023-11-29|Angus Burgin|The Information Superhighway, the Electronic Frontier, and the Political Economy of the Early Internet|burgin|documented as held|technology; political economy|Harvard, Lee Gathering Room CGIS S030, 1730 Cambridge Street; online series
2024-04-03|Richard Hornbeck|One Giant Leap: Emancipation and Aggregate Economic Gains|hornbeck|documented as held|slavery; emancipation; productivity|Online joint seminar; physical venue not_found_publicly
2024-04-10|M’hamed Oualdi|Freeing the last Muslim slaves in Europe: Moroccan Sultan Muhammad Ibn Abdallah’s social and economic policy from the 1750s to the late 1780s|oualdi|documented as held|slavery; abolition; Mediterranean|Online joint seminar; physical venue not_found_publicly
2024-04-29|Diana Kim|The Poet and the Partisan: On the Many Meanings of the State in Wartime Korea (1950-1953)|kim2|announced|state; Korea; war|Online joint seminar; physical venue not_found_publicly
2024-10-30|Giacomo Parrinello|Water for Growth: An Environmental History of the Po Valley, 1770-2003|parrinello|documented as held|water; environment; growth|Harvard, Lee Gathering Room S-030, 1730 Cambridge Street; Zoom
2025-04-08|Maya Jasanoff|The Birth of the Family Tree|jasanoff|documented as held|genealogy; property; power|Harvard, Lee Gathering Room S-030, CGIS South, 1730 Cambridge Street; Zoom
2025-11-21|Malick Ghachem|Bubble Colony: Saint-Domingue and the Debt of France|ghachem|documented as held|slavery; debt; colonial history|Harvard, Lee Gathering Room S-030, 1730 Cambridge Street; online series
2026-03-11|Mélanie Lamotte|By Flesh and Toil: How Sex, Race, and Labor Shaped the Early French Empire|lamotte|documented as held|race; labour; empire|Harvard, Lee Gathering Room CGIS S-030, 1730 Cambridge Street; online series
2026-04-01|Arne Westad|The Coming Storm|westad|documented as held|international history; great powers|Harvard, Bowie Vernon Room CGIS-K262, 1737 Cambridge Street; online series
2026-10-28|Jeremy Adelman|The Capitalist Era|adelman|announced|capitalism; interdependence; globalization|Harvard, Lee Gathering Room S-030, CGIS South, 1730 Cambridge Street; Zoom'''
failed={'ranganathan','amrith','warde','levy','bowie','kala','kim2'}
events=[]
for i,line in enumerate(data.splitlines(),1):
 date,sp,title,slug,status,topics,location=line.split('|')
 sid='P04-N001';url=base+'past_seminars.html';notes='Dated notice on Past seminars index; occurrence unconfirmed. Past index placement alone not treated as held evidence.'
 if slug!='archive':
  url=base+slug+'.html';n=100+i
  retrieval='retrieved via web open; indexed/cached crawl displayed; live origin not independently verified'
  if slug in failed: retrieval='detail retrieval failed; non-www and www attempts; metadata verified on opened past-seminars index'
  if slug=='ogle': retrieval='full indexed search text retrieved; direct opens failed; explicitly says seminar took place 13 October 2021'
  detailid=src(n,url,f'Joint Center Online Seminar — {sp}: {title}','Dated event metadata and '+('explicit retrospective took-place statement' if status=='documented as held' else 'announcement, not held confirmation'),retrieval)
  sid+=';'+detailid
  if status=='documented as held': notes='Detail page explicitly says this seminar took place; event held status verified. Publication date not stated.'
  elif slug=='adelman': notes='Detail remains future-tense announcement although scheduled date precedes as-of date; held status unconfirmed.';sid+=';P04-N002'
  else: notes='Detail fetch failed; dated past-seminars index verifies advertised title/date/speaker; held status unconfirmed.'
 if slug=='ogle': notes='Explicit held statement available only in full indexed search retrieval; live/direct retrieval failed. Historical occurrence supported, current page state unverified.'
 events.append(dict(event_id=f'P04-NE{i:03}',title=title,dates=date,status=status,format='Joint Center online seminar',speakers=sp,organisers='Joint Center for History and Economics; historical individual convenors not_found_publicly',partners='Cambridge CHE; Harvard CHE; CHEP / Sciences Po (series-level partnership)',CHEP_role='network programme involving Paris and promoted by CHEP; event-level Paris organisation unverified',topics=topics+' (editorial topic tags)',language='not_found_publicly',location_or_mode=location,programme_url=url,recording_url='not_found_publicly',source_ids=sid+';P04-N002',evidence_status='verified',evidence_notes=notes,date_precision='day',temporal_status='past scheduled date',as_of_date=A))
for fn,rows in [('partner_sources.csv',sources),('joint_seminars.csv',events)]:
 with (p/fn).open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
(p/'partner_data.json').write_text(json.dumps(dict(as_of_date=A,sources=sources,events=events),ensure_ascii=False,indent=2),encoding='utf-8')
from collections import Counter
print(len(events),Counter(e['dates'][:4] for e in events),Counter(e['status'] for e in events),len(sources))
