import csv
from pathlib import Path
p=Path(__file__).parent
def read(name):
 with (p/name).open(encoding='utf-8',newline='') as f: return list(csv.DictReader(f))
funding=read('support_funding.csv');sources=read('support_sources.csv');leads=read('support_leads.csv');coverage=read('support_coverage.csv')
def source(n,url,title,owner,date,supports,status='retrieved_indexed_HTML; crawl date is not publication date'):
 sources.append(dict(source_id=f'P03-S{n}',url=url,title=title,publisher_or_owner=owner,source_date=date,accessed_at='2026-11-15',source_type='official_webpage',supports=supports,retrieval_status=status))
source(442,'https://frenchcolonial.org/awards-prizes/','Awards and Prizes','French Colonial Historical Society','date_unknown','Lamotte2026 Boucher Book Prize and2025 article prize','retrieved_indexed_HTML; crawl2days ago')
source(443,'https://oieahc.wm.edu/publications/wmq/prizes/adair-winners/','Adair Prize Winners','Omohundro Institute of Early American History and Culture','date_unknown','Lamotte2024 Douglass Adair Memorial Award','retrieved_indexed_HTML; crawl5days ago')
source(444,'https://trinity.duke.edu/news/melanie-lamotte-wins-french-colonial-historical-societys-best-article-prize','Mélanie Lamotte Wins French Colonial Historical Society’s Best Article Prize','Duke University Trinity College','2025-09-15','Corroborates2025 FCHS and2024 Adair award to same article')
source(445,'https://www.manchester.ac.uk/about/news/modern-history-lecturers-awarded-prize-worth-100000/','Modern History Lecturers awarded prize worth £100,000','University of Manchester','2020-10-29','Indexed article names Yates and Hanß and£100000; amount retained only as lead','search_index_content_retrieved; underlying_open_failed503')
source(446,'https://www.leverhulme.ac.uk/philip-leverhulme-prizes-2020','Philip Leverhulme Prizes2020','Leverhulme Trust','date_unknown','Funder award-year page linked by Harvard; content unavailable','retrieval_failed403')
source(447,'https://histecon.fas.harvard.edu/news.html','News Archive','Harvard Center for History and Economics','date_unknown','Yates2020 Philip Leverhulme Prize explicitly awarded','retrieved_indexed_HTML; crawl5days ago')
source(448,'https://www.pantheonsorbonne.fr/actualite/elsa-genard-sorbonne-harvard-prison-comme-terrain-recherche','Elsa Génard, de la Sorbonne à Harvard : la prison comme terrain de recherche','Université Paris1 Panthéon-Sorbonne','2022-09-08','Joinet2022 winner;EHP fellowship3years;Paris first period;HarvardJan2022;planned endJan2024;prize-category wording inconsistent within page')
source(449,'https://www.alc.manchester.ac.uk/research/projects/','Our research projects','University of Manchester School of Arts Languages and Cultures','date_unknown','Yates Property and the Making and Unmaking of French Empire1870–1970 funded by Philip Leverhulme Prize')
def award(n,name,scheme,sids,**kw):
 r={k:'not_found_publicly' for k in funding[0]}
 r.update(funding_id=f'P03-F{n}',parent_award_id='not_applicable',relationship_category='individual_connected',instrument_type='prize',scheme=scheme,project='not_applicable',recipient=name,beneficiary=name,award_date='date_unknown',start_date='not_applicable',end_date='not_applicable',amount_basis='not_found_publicly; no cash receipt or expenditure evidenced',award_or_call_status='award_announced',evidence_status='verified',source_ids=';'.join(f'P03-S{x}' for x in sids))
 r.update(kw);funding.append(r)
for n,scheme,funder,start,end,kind in [
 (428,'Aix-Marseille School of Economics PhD fellowship','Aix-Marseille School of Economics','2024','2025','fellowship'),
 (429,'UNU-WIDER research grant2023','UNU-WIDER','2023','2023','research_grant'),
 (430,'Oppenheimer Memorial Trust Doctoral Scholarship','Oppenheimer Memorial Trust','2020','2023','doctoral_scholarship'),
 (431,'UNU-WIDER research grant2020','UNU-WIDER','2020','2020','research_grant'),
 (432,'Sciences Po Department of Economics Doctoral Contract','Sciences Po Department of Economics','2020','2023','doctoral_contract'),
 (433,'National Research Foundation Masters scholarship','National Research Foundation','2018','2018','masters_scholarship'),
 (434,'Embassy of France in South Africa Masters Scholarship','Embassy of France in South Africa','2016','2017','masters_scholarship'),
 (435,'University of Cape Town travel fund grant','University of Cape Town','2013','2013','travel_grant')]:
 award(n,'Leonard le Roux',scheme,[411,438],instrument_type=kind,project='not_found_publicly',funder=funder,administrator='not_found_publicly',CHEP_connection=('Earlier member award before Paris collaboration2019; later CHEP grant2022–23; not CHEP income' if n>=433 else 'CHEP student-grant holder2022–23; independent award; no CHEP funding attribution'),award_date='date_unknown',start_date=start,end_date=end,award_or_call_status='award_documented_in_author_CV')
award(436,'Elsa Génard','Prix de thèse Louis Joinet',[427,448,404],project='À la peine. Une histoire sociale des interactions carcérales (France années1910–1930)',funder='IFJD-Institut Louis Joinet',administrator='IFJD-Institut Louis Joinet',CHEP_connection='CHEP past fellow2021–22; independent thesis prize',award_date='2022')
award(437,'Alexia Yates','Philip Leverhulme Prize2020',[447,449,203],instrument_type='research_prize',project='Property and the Making and Unmaking of French Empire1870–1970',funder='Leverhulme Trust',CHEP_connection='CHEP research associate in accessed roster; independent Manchester research prize',award_date='2020',amount_basis='Personal award amount unverified;£100000 indexed Manchester announcement retained as separate lead')
award(438,'Mélanie Lamotte','Mary Alice and Philip Boucher Book Prize',[442,203],project='By Flesh & Toil: How Sex Race and Labor Shaped the Early French Empire',funder='French Colonial Historical Society',administrator='French Colonial Historical Society',CHEP_connection='CHEP research associate; independent award; no CHEP financing attribution',award_date='2026')
award(439,'Mélanie Lamotte','French Colonial Historical Society Article Prize',[442,444,203],project='Beyond the Atlantic: Unifying Racial Policies across the Early French Empire',funder='French Colonial Historical Society',administrator='French Colonial Historical Society',CHEP_connection='CHEP research associate; independent award; no CHEP financing attribution',award_date='2025')
award(440,'Mélanie Lamotte','Douglass Adair Memorial Award',[443,444,203],project='Beyond the Atlantic: Unifying Racial Policies across the Early French Empire',funder='Omohundro Institute of Early American History and Culture; William and Mary Quarterly',administrator='Omohundro Institute of Early American History and Culture',CHEP_connection='CHEP research associate; independent award; no CHEP financing attribution',award_date='2024')
leads.append(dict(lead_id='P03-L409',entity_or_scheme='Alexia Yates Philip Leverhulme Prize2020 — amount',lead_type='unverified_amount',award_or_call_status='award_verified_amount_pending',amount='100000',currency='GBP',evidence_status='unverified',source_ids='P03-S445;P03-S446;P03-S447;P03-S449',evidence_note='Award and research support verified. Indexed Manchester announcement gives£100000; underlying page503 and funder403. Exclude from comparable totals until full award-source verification.',next_step='Retrieve award-year notice or award letter establishing individual value and term'))
for r in funding[-13:]:
 coverage.append(dict(entity_or_scheme=r['beneficiary']+' — '+r['scheme'],entity_type='individual_award_or_support',person_id_if_applicable=r['beneficiary'],years_checked=(r['award_date'] if r['award_date']!='date_unknown' else r['start_date']+'–'+r['end_date']),sources_checked=r['source_ids'],findings_count=1,gaps='amount; legal payer; actual expenditure; recipient dates where unknown',completion_status='named_remaining_lead_processed'))
for fname,rows in [('support_funding.csv',funding),('support_sources.csv',sources),('support_leads.csv',leads),('support_coverage.csv',coverage)]:
 key={'support_funding.csv':'funding_id','support_sources.csv':'source_id','support_leads.csv':'lead_id'}.get(fname)
 if key: assert len({r[key] for r in rows})==len(rows)
 with (p/fname).open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print(len(funding),'awards;',len(sources),'sources;',len(leads),'leads;',len(coverage),'coverage rows')
