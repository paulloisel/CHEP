import csv
from pathlib import Path

OUT=Path(__file__).parent
DATE='2026-11-15'
sources=[]
def src(n,url,title,owner,supports,date='date_unknown',status='retrieved_indexed_cache; live state not independently established',typ='official_webpage'):
    sources.append(dict(source_id=f'P03-S{n}',url=url,title=title,publisher_or_owner=owner,source_date=date,accessed_at=DATE,source_type=typ,supports=supports,retrieval_status=status))
src(201,'https://histecon.fr/en/people.html','People','CHEP','Directory navigation; indexed crawl 6 months before access')
src(202,'https://histecon.fr/en/organisation.html','Organisation','CHEP','Levy coordinator; Cheadle coordination; Price web architect; indexed 2 weeks')
src(203,'https://histecon.fr/en/research_associates.html','Research associates','CHEP','20 associates; indexed today')
src(204,'https://histecon.fr/fr/chercheurs_associes.html','Chercheurs associés','CHEP','French associate list matches 20 English names; indexed 5 months')
src(205,'https://histecon.fr/en/research_fellows.html','Research fellows','CHEP','Jessica Balguy current displayed fellow; indexed 6 months')
src(206,'https://histecon.fr/en/research_fellows_past.html','Past research fellows','CHEP','Hewitt 2024–25; Le Bras 2021–23; Génard 2021–22; indexed today')
src(207,'https://histecon.fr/en/research_students.html','Research students 2026','CHEP','Four students, linked previous-students branch; indexed today')
src(208,'https://histecon.fr/en/research_visitors.html','Research visitors','CHEP','Chiara Cordelli 2025–27; indexed 3 months')
src(209,'https://histecon.fr/en/visiting_graduate_students.html','Visiting graduate students','CHEP','Dev Patel and Emma Prevignano 2021–22; indexed today')
src(210,'https://www.sciencespo.fr/histoire/en/research/centre-for-history-and-economics-in-paris-chep/','Centre for History and Economics in Paris (CHEP)','Sciences Po','Host roster includes Joan Chaker; scholarship holders; indexed 2 weeks')
src(211,'https://www.sciencespo.fr/histoire/fr/recherche/centre-for-history-and-economics-paris-chep/','Centre for History and Economics à Paris (CHEP)','Sciences Po','2020 selected exchange cohort; 2022 Lviv; governance contributors; Lola Zappi; indexed last month')
src(212,'https://www.sciencespo.fr/histoire/en/the-centre/faculty/visiting-scholars/','Visiting Scholars','Sciences Po','CHEP-specific Lina Skoglund 2025-12-01–2027-08-31 and Jingyi Huang 2021–22 section; indexed 5 days')
src(213,'https://histecon.fr/en/executive_committee.html','Executive committee','CHEP','Unretrieved branch; www alias also attempted',status='failed_inaccessible_or_cache_miss')
src(214,'https://histecon.fr/en/research_students_previous.html','Previous research students','CHEP','Unretrieved branch; www alias also attempted',status='failed_cache_miss')
src(215,'https://histecon.fr/fr/research_fellows.html','Research fellows — French route','CHEP','Language variant attempted',status='failed_406')
src(216,'https://histecon.fr/fr/doctorantes.html','Doctorantes — French route','CHEP','Language variant attempted',status='failed_406')
src(217,'https://cordis.europa.eu/project/id/819353','SlaveVoices — grant agreement 819353','European Commission CORDIS','EU contribution; legal beneficiaries; signature and duration; indexed 2 months')
src(218,'https://nes.princeton.edu/news/oualdi-awarded-european-research-council-consolidator-grant','Oualdi Awarded European Research Council Consolidator Grant','Princeton University','PI and original announced 2019–23 plan; indexed retrieved cache 2.2 years','2019-04-02')
src(219,'https://anr.fr/Projet-ANR-13-BSH1-0005','Les transformations de l’économie française par le prisme du commerce international, 1716-1821 — TOFLIT18','ANR','Daudin coordinator; EUR249950; December2013;48months; indexed last month')
src(220,'https://anr.fr/Projet-ANR-21-CE26-0022','Comportements prosociaux — le miroir à deux images — SOSELF','ANR','EUR355152;June2022;48months; Emeric Henry coordinator; indexed6months')
src(221,'https://www.sciencespo.fr/department-economics/news/our-latest-anr-projects-soself-and-joce/','Our latest ANR projects SOSELF and JOCE','Sciences Po','Roberto Galbiati collaborator in awarded grant; indexed2months','2022-02-03')
src(222,'https://giacomoparrinello.net/shifting-shores/','Shifting Shores','Giacomo Parrinello','2018 award; originally funded until2022; indexed1.6years',typ='researcher_project_webpage')
src(223,'https://www.sciencespo.fr/ecole-recherche/fr/actualites/retour-sur-le-projet-shifting-shores-giacomo-parrinello-2019-2024/','Retour sur le Projet SHIFTING SHORES — Giacomo Parrinello (2019–2024)','Sciences Po','Later project retrospective2019–24; funding Ville de Paris; indexed1.7years','2025-01-27')
src(224,'https://www.humanities.manchester.ac.uk/history/research/centres/centre-for-economic-cultures/projects/','Centre for Economic Cultures research projects','University of Manchester','Alexia Yates AHRC AH/S012680/1 2020–22; indexed yesterday')
src(225,'https://history.parisschoolofeconomics.eu/financements/','Financements — Histoire économique et sociale','Paris School of Economics','Monnet EHESS2020–21; other participated projects not personal awards; indexed4weeks')
src(226,'https://www.cmu.edu/dietrich/lcal/about-us/cvs/jessica-balguy-cv-compressed.pdf','Jessica Balguy — CV','Carnegie Mellon University / Jessica Balguy','p1 fellowships:2019 EHESS;2022 FME/MQB; ambiguous ANR2015/2020 entries; indexed10months',typ='institution_hosted_CV_PDF')
src(227,'https://www.radcliffe.harvard.edu/people/melanie-lamotte','Mélanie Lamotte — Radcliffe Fellow','Harvard Radcliffe Institute','2021–22 fellowship; indexed last month')
src(228,'https://melanielamotte.com/awards','Awards — Mélanie Lamotte','Mélanie Lamotte','USD50000 departmental enhancement;2022–23 excellence grant; historical/future leads; indexed2weeks',typ='researcher_webpage')
src(229,'https://anr.fr/en/latest-news/read/news/vers-une-cartographie-des-emissions-de-gaz-a-effet-de-serre-dune-ville-par-secteur-dactivite-le/','Vers une cartographie des émissions de gaz à effet de serre d’une ville par secteur d’activité : le projet CIUDAD','ANR','MOPGA PIA-funded project; Thomas Lauvaux coordinator; indexed4months','2019-11-07')
src(230,'https://anr.fr/fr/actus/details/news/make-our-planet-great-again-18-premiers-chercheurs-selectionnes/','Make our planet great again : 18 premiers chercheurs sélectionnés','ANR','2017 selection Thomas Lauvaux','2017',status='search_index_text; underlying page not opened in this subtask')
src(231,'https://www.sciencespo.fr/recherche/fr/recherches/conventions-de-recherche/les-conventions-avec-l-agence-nationale-de-recherche/','Les conventions avec l’Agence Nationale de Recherche','Sciences Po','SIP partner Marion Fontaine 2024-10-01–2027-09-30; indexed today')
src(232,'https://history.fas.harvard.edu/news/prof-mary-lewis-awarded-guggenheim-memorial-foundation-fellowship','Mary Lewis awarded Guggenheim Memorial Foundation Fellowship','Harvard University','Earlier fellowship2015; indexed2months','2015-04-09')
src(233,'https://cordis.europa.eu/project/id/249546','TRADEDEPRESSION — grant agreement 249546','European Commission CORDIS','Earlier grant2010–15 EUR1408015.40; archived2024-06-18; indexed last month')
src(234,'https://tcdie-lb01-production.terminalfour.net/news_events/articles/tcd-researcher-receives-european-research-council-grant-to-study-trade-policy-and-great-depression/','TCD Researcher Receives European Research Council Grant to Study Trade Policy and Great Depression','Trinity College Dublin','O’Rourke PI; rounded1.4million; announcement2010','2010-01-11',status='search_index_text; underlying page not opened in this subtask')
src(235,'https://www.radcliffe.harvard.edu/people/francesca-trivellato','Francesca Trivellato — Bunting Fellow','Harvard Radcliffe Institute','Earlier2006–07 fellowship; indexed last month')
src(236,'https://www.clir.org/programs-and-grants/mellon/fellowshiprecipients/','Fellowship Recipients','Council on Library and Information Resources','2006 Mellon Fellows: Jonathan Levy; indexed5days')
src(237,'https://www.sciencespo.fr/ecole-droit/fr/annuaire/glaser-sarah-marthe/','Sarah Marthe Glaser','Sciences Po','Max Weber2024–25; undated Cambridge/Heidelberg bursaries; indexed4months')
src(238,'https://www.eshs.org/wp-content/uploads/2024/07/2022eshs-general-assembly-minutes-of-meetingFINAL-Copy.pdf','ESHS General Assembly — 10 September 2022','European Society for the History of Science','p53 Emma Prevignano early scholar grant; indexed last month','2022-09-10',typ='official_minutes_PDF')
src(239,'https://www.sciencespo.fr/histoire/fr/annuaire/lanko-natalia/','Natalia Lanko','Sciences Po','NYU Bayly Winder2023;MacCracken2022; CHEP2025; indexed last month')
src(240,'https://snfpaideia.upenn.edu/people/liane-hewitt/','Liane Hewitt','University of Pennsylvania','Named external funder support but no periods or amounts; CHEP support; indexed3weeks')
src(241,'https://hca.ed.ac.uk/history/research/research-projects/removal-of-citizens-rights-in-france','The Removal of Citizens’ Rights in France and the French Empire, 1789–1914','University of Edinburgh','Joseph La Hausse de Lalouvière British Academy fellowship2024–27','2024-08-01',status='search_index_full_text; direct_open_failed_403')
src(242,'https://www.sciencespo.fr/histoire/fr/annuaire/chessel-marie-emmanuelle/','Marie-Emmanuelle Chessel','Sciences Po','SAB Sciences Po-UPC project2024–26 lead',status='search_index_text; underlying page not opened in this subtask')
src(243,'https://www.sciencespo.fr/cso/sites/sciencespo.fr.cso/files/CSO_Rapport_2024_.pdf','Rapport d’activité CSO 2024','Sciences Po CSO','p40 LOGE ANR Access ERC; Gautier Morin under Lemercier; lead','2024',status='search_index_text; underlying PDF not opened in this subtask',typ='official_report_PDF')
src(244,'https://www.sciencespo.fr/ecole-recherche/en/directory/giosue-francesco/','Francesco Giosuè','Sciences Po','IdEx2023–24 lead',status='search_index_text; direct_open_failed_cache_miss')
src(245,'https://www.sciencespo.fr/histoire/en/news/lucile-truffy-recipient-vibeke-sorensen-research-fellowship-2026/','Lucile Truffy, recipient of the Vibeke Sørensen research fellowship','Sciences Po','2026 archival fellowship; one-month visit','2026-10-23',status='search_index_full_text; direct_open_failed_cache_miss')
src(246,'https://www.sciencespo.fr/ecole-recherche/fr/annuaire/iyamu-ebunoluwa/','Ebunoluwa Iyamu','Sciences Po','Graduate Institute and A.G.Leventis scholarships; dates unknown',status='search_index_full_text; direct_open_failed_403')
src(247,'https://fr.linkedin.com/in/emma-prevignano','Emma Prevignano','LinkedIn / researcher','Cambridge Trust/Gerda Henkel and society grant leads',status='search_index_text; not opened',typ='researcher_profile')
src(248,'https://devpatel.scholars.harvard.edu/sites/g/files/omnuum8541/files/devpatel/files/rosetta_stone.pdf','A Rosetta Stone for Human Capital','Harvard author repository','NSF DGE1745303 acknowledgement lead',status='search_index_text; direct_open_failed',typ='working_paper_PDF')
src(249,'https://albert.ias.edu/bitstreams/fed12df9-1b6c-411e-99ae-625dacec1c3b/download','Francesca Trivellato — CV','Institute for Advanced Study','Many earlier fellowships incl declined; pending extraction','2025-06',status='search_index_text; not opened',typ='institution_hosted_CV_PDF')
src(250,'https://chicago.academia.edu/ChiaraCordelli/CurriculumVitae','Chiara Cordelli — CV','Researcher / Academia.edu','Earlier fellowship leads incl declined; pending institution confirmation',status='search_index_text; not opened',typ='researcher_CV')
src(251,'https://anr.fr/Projet-ANR-21-FRAL-0012','DesinEE — La Désindustrialisation en Allemagne et en France','ANR','EUR189214;August2022;36months; lead to Fontaine participation; indexed2months')
src(252,'https://www.uni-saarland.de/lehrstuhl/lemmes/forschung/dfg-anr-projekt-desinee.html','DFG-ANR-Projekt DesinEE','Universität des Saarlandes','Fontaine co-workshop involvement; does not identify her personal allocation',status='search_index_text; not opened')
src(253,'https://www.sciencespo.fr/cso/sites/sciencespo.fr.cso/files/CV%20J.%20Lazarus%20-%202024.pdf','Jeanne Lazarus — CV','Sciences Po CSO','LIEPP household money project co-led with Nicolas Delalande; EUR70000 lead','2024',status='search_index_text; not opened',typ='institution_hosted_CV_PDF')
src(255,'https://histecon.fr/fr/research_visitors.html','Research visitors — French route','CHEP','French Cordelli page retrieved; indexed last month')
src(256,'https://rsss.cass.anu.edu.au/news/decra-grant-awarded-dr-aditya-balasubramanian','DECRA grant awarded to Dr Aditya Balasubramanian','Australian National University','2024 award $477039; exact award period not stated; indexed2months','2024-08-27')
src(257,'https://www.sciencespo.fr/histoire/fr/recherche/centre-for-history-and-economics-paris-chep/','CHEP host page — older indexed state','Sciences Po','Search indexed older state names David Todd coordinator; newer opened state Levy. No snapshot date; cannot date change',status='search_index_older_state; 2months crawl; direct_open_newer_state')
src(258,'https://www.sciencespo.fr/ecole-recherche/fr/actualites/entretien-avec-david-todd-directeur-des-etudes-en-histoire/','Entretien avec David Todd, directeur des études en Histoire','Sciences Po','Coordination since2022 stated in dated interview; indexed2weeks','2025-07-21')
src(259,'https://www.sciencespo.fr/histoire/en/events/centre-for-history-and-economics-in-paris-chep/','Centre for History and economics in Paris (CHEP) — 29 November 2023','Sciences Po','Dated event explicitly calls Todd coordinator; indexed last year','2023-11-29')
src(260,'https://ehs.org.uk/person/professor-kevin-orourke/','Professor Kevin O’Rourke','Economic History Society','2010 ERC Advanced Investigator Grant awarded; corroborates earlier award; indexed last month')
src(261,'https://www.kva.se/nyheter/ekonomipriset-2019/','Ekonomipriset 2019','Royal Swedish Academy of Sciences','Award announcement: Banerjee, Duflo and Kremer; prize divided equally among three laureates; indexed last month','2019-10-14')
src(262,'https://www.nobelprize.org/prizes/economic-sciences/2019/summary/','Economic Sciences 2019 — summary','Nobel Prize','Canonical source attempted; accessible Academy award announcement used instead',status='direct_open_failed_403')
src(263,'https://www.nobelprize.org/prizes/economic-sciences/2019/banerjee/facts/','Abhijit Banerjee — Facts','Nobel Prize','Canonical laureate source attempted; accessible Academy award announcement used instead',status='direct_open_failed_403')
src(264,'https://www.nobelprize.org/prizes/economic-sciences/2019/duflo/facts/','Esther Duflo — Facts','Nobel Prize','Canonical laureate source attempted; accessible Academy award announcement used instead',status='direct_open_failed_403')
for s in sources:
    if s['source_id']=='P03-S242': s['retrieval_status']='retrieved_indexed_cache; indexed2months';s['supports']='Projects heading: funded SAB Sciences Po-UPC project2024–26; shared with Kevin Mellet and Ariane Mak'
    if s['source_id']=='P03-S234': s['retrieval_status']='search_index_full_text; direct_open_failed_cache_miss'

cohort=[]
def person(name,category,connection,dates,ss):
    cohort.append(dict(person_id=f'P03-P{len(cohort)+1:03}',name=name,inclusion_category=category,Paris_connection=connection,connection_dates=dates,evidence_status='verified',source_ids=ss))
associates=['Anatole Le Bras','Nicolas Delalande','Guillaume Daudin','Marion Fontaine','Roberto Galbiati','Elsa Génard','Joseph la Hausse de Lalouvière','Claire Lemercier','Mélanie Lamotte','Thomas Lauvaux','Jonathan Levy','Mary Lewis','Eric Monnet','Cheyenne Olivier',"Kevin O’Rourke",'M’Hamed Oualdi','Giacomo Parrinello','Gareth Stedman Jones','Francesca Trivellato','Alexia Yates']
for name in associates:
    dates='date_unknown; displayed in accessed directory'
    category='research_associate'
    ss='P03-S203;P03-S204'
    connection='CHEP Research Associate'
    if name=='Anatole Le Bras': dates='fellow 2021–2023; associate start date_unknown'; category+=';past_fellow'; ss+=';P03-S206'
    if name=='Elsa Génard': dates='fellow 2021–2022; associate start date_unknown'; category+=';past_fellow'; ss+=';P03-S206'
    if name=='Jonathan Levy': category+=';coordinator'; connection+='; Coordinator';ss+=';P03-S202'
    person(name,category,connection,dates,ss)
person('Jessica Balguy','research_fellow','CHEP fellow; host lists postdoctoral researcher','date_unknown','P03-S205;P03-S210')
person('Joan Chaker','postdoctoral_researcher','Listed in host CHEP research community','date_unknown','P03-S210')
person('Liane Hewitt','past_fellow','CHEP past research fellow','2024–2025 (CHEP list)','P03-S206')
for name in ['Francesco Giosuè','Rébecca Mathiot','Giulio Piumelli','Aesa Virely']:
    person(name,'research_student;scholarship_holder','CHEP research student and scholarship holder','2026','P03-S207;P03-S210')
person('Chiara Cordelli','research_visitor;senior_research_fellow','CHEP visiting senior fellow','2025–2027','P03-S208;P03-S255')
for name in ['Dev Patel','Emma Prevignano']:
    person(name,'visiting_graduate_student','Selected exchange2020; visiting CHEP2021–22','2020;2021–2022','P03-S209;P03-S211')
for name,role in [('Mary-Rose Cheadle','Coordination with CHE-Cambridge and CHE-Harvard'),('Amy Price','Web architect')]:
    person(name,'support_function',role,'date_unknown','P03-S202')
for name in ['Megan Ma','Sarah Glaser']:
    person(name,'selected_exchange_student','Named selected CHEP exchange student','2020','P03-S211')
for name in ['Marie-Emmanuelle Chessel','Thierry Mayer','Paul-André Rosental','Emma Rothschild']:
    person(name,'governance_activity_contributor','Named contributor to organisation of CHEP activities','date_unknown','P03-S211')
person('Lola Zappi','CHEP_supported_exchange;EHP_fellow','Host describes CHEP-facilitated Harvard stay; EHP-CHEP list','2021–2022','P03-S211;P03-S425')
person('Jingyi Huang','EHP_CHEP_fellow','Host CHEP cooperation visitor; EHP-CHEP list','2021–2022','P03-S212;P03-S425')
person('Lina Skoglund','visiting_postdoctoral_researcher','Explicit CHEP visit','2025-12-01/2027-08-31','P03-S212')
person('Ivanna Cherchovych','support_beneficiary','CHEP funded Lviv research fellowship','2022 autumn','P03-S211')
for name in ['Vincent Harmsen','Ebunoluwa Iyamu','Natalia Lanko','Lucile Truffy']:
    person(name,'scholarship_holder','CHEP research scholarship recipient','2025','P03-S408')
person('Leonard le Roux','scholarship_holder','CHEP PhD research grant','2022–2023','P03-S411')
person('Hugo Carlier','scholarship_holder','CHEP research grant','2022','P03-S410')
person('Aditya Balasubramanian','EHP_CHEP_fellow','2021 CHEP-EHP fellows list','2021–2022','P03-S425;P03-S432')
person('David Todd','historical_coordinator','Coordinator since2022 stated in July2025 interview; current host page names Levy','2022 start; still described2025-07-21; end date_unknown','P03-S258;P03-S259;P03-S210')
person('Abhijit Banerjee','historical_scientific_council_member','CHEP scientific council member in March2020 institutional minutes; current status not established','attested 2020-03-10; start and end date_unknown','P03-S309')
person('Esther Duflo','historical_scientific_council_member','CHEP scientific council member in March2020 minutes; source misspells Duflot; normalized using award authority; current status not established','attested 2020-03-10; start and end date_unknown','P03-S309;P03-S261')
person('Jenny Andersson','historical_scientific_council_member','CHEP scientific council included her in March2020 institutional minutes; current status not established','attested 2020-03-10; start and end date_unknown','P03-S309')
for p in cohort:
    if p['name']=='Claire Lemercier':
        p['inclusion_category']+=';historical_coordinator'
        p['Paris_connection']+='; coordinator attested2020-03-10'
        p['connection_dates']+='; coordinator2020-03-10; term boundaries unknown'
        p['source_ids']+=';P03-S309'
    elif p['name'] in ['Marie-Emmanuelle Chessel','Nicolas Delalande','Giacomo Parrinello','Paul-André Rosental','Thierry Mayer','Francesca Trivellato','Guillaume Daudin']:
        p['inclusion_category']+=';historical_scientific_council_member'
        p['Paris_connection']+='; scientific council attested2020-03-10'
        p['connection_dates']+='; scientific council2020-03-10; term boundaries unknown'
        p['source_ids']+=';P03-S309'

fund=[]
def grant(scheme,project,funder,beneficiary,ss,award='date_unknown',start='date_unknown',end='date_unknown',amount='not_found_publicly',currency='not_found_publicly',basis='not_found_publicly',recipient='not_found_publicly',admin='not_found_publicly',instrument='research_grant',connection='CHEP associate; affiliation start unknown; independently awarded; not CHEP income',status='award_announced',ev='verified',parent='not_applicable'):
    fund.append(dict(funding_id=f'P03-F{201+len(fund)}',parent_award_id=parent,relationship_category='grants_to_individuals_with_CHEP_connection',instrument_type=instrument,scheme=scheme,project=project,funder=funder,recipient=recipient,administrator=admin,beneficiary=beneficiary,CHEP_connection=connection,award_date=award,start_date=start,end_date=end,amount=amount,currency=currency,amount_basis=basis,award_or_call_status=status,evidence_status=ev,source_ids=ss))
grant('ERC Consolidator Grant 819353','SlaveVoices','European Union / ERC','M’Hamed Oualdi (PI); project team','P03-S217;P03-S218;P03-S203','2019-06-28','2019-10-01','2027-08-31','1999975.00','EUR','total EU project contribution; not expenditure','European University Institute; Fondation Nationale des Sciences Politiques',instrument='project_grant')
grant('ERC 819353 beneficiary component','SlaveVoices','European Union / ERC','M’Hamed Oualdi project','P03-S217;P03-S203','2019-06-28','2019-10-01','2027-08-31','421690.00','EUR','net EU beneficiary contribution included in P03-F201','European University Institute',instrument='beneficiary_allocation',parent='P03-F201')
grant('ERC 819353 beneficiary component','SlaveVoices','European Union / ERC','M’Hamed Oualdi project','P03-S217;P03-S203','2019-06-28','2019-10-01','2027-08-31','1578285.00','EUR','net EU beneficiary contribution included in P03-F201','Fondation Nationale des Sciences Politiques',instrument='beneficiary_allocation',parent='P03-F201')
grant('ANR-13-BSH1-0005','TOFLIT18','ANR','Guillaume Daudin (coordinator); project consortium','P03-S219;P03-S203',start='2013-12',amount='249950',currency='EUR',basis='ANR project aid total;48months from December2013; end date not stated',instrument='project_grant',connection='Earlier member award before Paris collaboration; later CHEP associate; not CHEP income')
grant('ANR-21-CE26-0022','SOSELF','ANR','Emeric Henry (coordinator); Roberto Galbiati (collaborator); project consortium','P03-S220;P03-S221;P03-S203',start='2022-06',amount='355152',currency='EUR',basis='ANR project aid total;48months; Galbiati personal allocation unknown',instrument='project_grant')
grant('Émergence(s)','SHIFTING SHORES','Ville de Paris','Giacomo Parrinello; research team','P03-S222;P03-S223;P03-S203',award='2018',start='2019',end='2024',basis='amount unknown; retrospective project period2019–24 differs original funding through2022',instrument='project_grant',connection='Award predates2019 Paris collaboration; project overlaps; CHEP associate; not CHEP income',ev='conflicting')
grant('AHRC AH/S012680/1','Rise of the Rentier','Arts and Humanities Research Council','Alexia Yates; project team','P03-S224;P03-S203',start='2020',end='2022',basis='two-year project; amount not stated',instrument='project_grant')
grant('Fonds de recherche EHESS','Book on Bretton Woods monetary system','EHESS','Eric Monnet','P03-S225;P03-S203',start='2020-01',end='2021-12',instrument='book_writing_grant')
grant('8/9 achievement grant','Thesis completion','EHESS Endowment Fund','Jessica Balguy','P03-S226;P03-S205',award='2019',instrument='completion_grant',connection='Earlier career award before documented CHEP fellowship; not CHEP income')
grant('Joint research grant','not_found_publicly','Fondation pour la Mémoire de l’esclavage; Musée du Quai Branly–Jacques Chirac','Jessica Balguy','P03-S226;P03-S205',award='2022',connection='Earlier career award before documented CHEP fellowship; not CHEP income')
grant('Radcliffe Fellowship','Making Race / history research','Harvard Radcliffe Institute','Mélanie Lamotte','P03-S227;P03-S203',start='2021',end='2022',instrument='fellowship')
grant('Department Enhancement Grant','Courses on Black slavery at Tulane','Board of Regents of Louisiana','Mélanie Lamotte; Tulane courses','P03-S228;P03-S203',amount='50000',currency='USD',basis='researcher reports departmental course-development grant; award date and legal recipient unknown',instrument='teaching_grant')
grant('Excellence Grant Award','not_found_publicly','French Embassy in the U.S. / France-UT Center of Excellence','Mélanie Lamotte','P03-S228;P03-S203',start='2022',end='2023')
grant('Make Our Planet Great Again / PIA','CIUDAD','French Programme d’investissements d’avenir (ANR operator)','Thomas Lauvaux (coordinator); project team','P03-S229;P03-S203',instrument='project_grant',connection='CHEP associate; ANR-funded project attested2019; no CHEP receipt established')
grant('ANR collaborative project','Le sport et les investissements patronaux (1880–1980) — SIP','ANR','Marion Fontaine (Sciences Po partner); consortium','P03-S231;P03-S203',start='2024-10-01',end='2027-09-30',instrument='project_grant',connection='CHEP associate participates through CHSP; personal allocation and CHEP transfer not established')
grant('Guggenheim Fellowship','not_found_publicly','John Simon Guggenheim Memorial Foundation','Mary Lewis','P03-S232;P03-S203',award='2015',instrument='fellowship',connection='Earlier member award before Paris collaboration; later CHEP associate')
grant('ERC Advanced Grant 249546','TRADEDEPRESSION','European Union / ERC','Kevin O’Rourke (PI); research team','P03-S233;P03-S234;P03-S260;P03-S203',start='2010-05-01',end='2015-04-30',amount='1408015.40',currency='EUR',basis='EU project contribution; not personal income or annual expenditure',recipient='University of Oxford; Trinity College Dublin',instrument='project_grant',connection='Earlier member award before Paris collaboration; later CHEP associate; project-to-person link from indexed TCD notice not retrieved directly',ev='inferred')
grant('Bunting Fellowship','Cosmopolitanism in European commercial society','Harvard Radcliffe Institute','Francesca Trivellato','P03-S235;P03-S203',start='2006',end='2007',instrument='fellowship',connection='Earlier member award before Paris collaboration; later CHEP associate')
grant('Mellon Dissertation Research Fellowship','Risk and freedom in America','Mellon fellowship programme','Jonathan Levy','P03-S236;P03-S202',award='2006',admin='Council on Library and Information Resources',instrument='fellowship',connection='Earlier award before Paris collaboration; later CHEP Coordinator')
grant('Max Weber Fellowship','not_found_publicly','European University Institute','Sarah Glaser','P03-S237;P03-S211',start='2024',end='2025',instrument='fellowship',connection='2020 CHEP exchange selectee; later independent fellowship')
grant('Early scholar grant','ESHS2022 conference context','European Society for the History of Science','Emma Prevignano','P03-S238;P03-S209',award='2022',instrument='early_career_grant',connection='CHEP visitor2021–22; independent society award')
grant('Bayly Winder Summer Funding Fellowship','not_found_publicly','New York University','Natalia Lanko','P03-S239;P03-S408',award='2023',instrument='fellowship',connection='Award before2025 CHEP studentship; independently received')
grant('MacCracken Fellowship','not_found_publicly','New York University','Natalia Lanko','P03-S239;P03-S408',award='2022',instrument='fellowship',connection='Award before2025 CHEP studentship; independently received')
grant('SAB Sciences Po-UPC','The Making of Market Research in the 1950s and 1960s (France and Great Britain)','SAB Sciences Po-UPC','Marie-Emmanuelle Chessel; Kevin Mellet; Ariane Mak','P03-S242;P03-S211',start='2024',end='2026',instrument='project_grant',connection='CHEP governance/activity contributor; independently funded project; no CHEP receipt established')
grant('Discovery Early Career Researcher Award (DECRA)','Roads and Road Transport in India: An Environmental and Economic History','DECRA scheme','Aditya Balasubramanian','P03-S256;P03-S425',award='2024',amount='477039',currency='not_found_publicly',basis='Source states $477039; ISO currency not explicit on award notice; do not aggregate',instrument='project_grant',connection='Former CHEP-EHP fellow2021; independent later award; not CHEP income')
for laureate in ['Abhijit Banerjee','Esther Duflo']:
    grant('2019 Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel','Experimental approach to alleviating global poverty','not_found_publicly',laureate,'P03-S261;P03-S309',award='2019-10-14',basis='Equal share among three joint laureates (one third); no individual cash amount inferred',recipient=laureate,admin='Royal Swedish Academy of Sciences (award authority)',instrument='prize',connection='Independent2019 prize; historical CHEP scientific council attestedMarch2020; present membership unknown; no CHEP receipt established')
grant('ERC Starting Grant','A political history of the future: knowledge production and future governance 1945–2010 (FUTUREPOL)','European Union / ERC','Jenny Andersson (PI); research team','P03-S018;P03-S309',start='2012-01',end='2017-09',instrument='project_grant',connection='Earlier member grant; historical CHEP scientific council attestedMarch2020; present membership unknown; not CHEP income')

checks={
'Anatole Le Bras':('2019–2026','P03-S203;P03-S206','Targeted grant/fellowship search; thesis-prize lead delegated'),
'Nicolas Delalande':('2019–2026','P03-S203;P03-S253','LIEPP EUR70000 co-led project lead awaits CV date verification'),
'Guillaume Daudin':('2013–2026','P03-S203;P03-S219','PORTIC contribution lead not extracted'),
'Marion Fontaine':('2019–2026','P03-S203;P03-S231;P03-S251;P03-S252','DesinEE involvement pending underlying partner-source verification'),
'Roberto Galbiati':('2019–2026','P03-S203;P03-S220;P03-S221','Personal share unavailable'),
'Elsa Génard':('2021–2026','P03-S203;P03-S206;P03-S424','External targeted search primarily EHP; distributed fellowship handled separately'),
'Joseph la Hausse de Lalouvière':('2017–2026','P03-S203;P03-S241','British Academy2024–27 official indexed text; direct403; earlier Tawney/JCB fellows leads pending'),
'Claire Lemercier':('2019–2026','P03-S203;P03-S243','LOGE lead is supervision not personal award'),
'Mélanie Lamotte':('2011–2027','P03-S203;P03-S227;P03-S228','Future2027 ACLS entry excluded from historical ledger; earlier fellowships/prizes queue'),
'Thomas Lauvaux':('2017–2026','P03-S203;P03-S229;P03-S230','CIUDAD award/start/end/amount require award agreement'),
'Jonathan Levy':('2006–2026','P03-S202;P03-S236','Other earlier fellowships appear in institution-hosted CV search; not exhaustively extracted'),
'Mary Lewis':('2003–2026','P03-S203;P03-S232','Earlier NEH2003 recipient lead; term and amount not inferred'),
'Eric Monnet':('2011–2026','P03-S203;P03-S225','SYSRI30 and D-FIH participant status not personal award; omitted from individual award total'),
'Cheyenne Olivier':('2019–2026','P03-S203','Targeted grant search; arts prize leads; no funding record established'),
'Kevin O’Rourke':('2010–2026','P03-S203;P03-S233;P03-S234','Earlier award isolated; full lifetime grant history not claimed'),
'M’Hamed Oualdi':('2019–2027','P03-S203;P03-S217;P03-S218','CORDIS current period supersedes2019 original plan; actual disbursement unknown'),
'Giacomo Parrinello':('2018–2026','P03-S203;P03-S222;P03-S223','Original funding2022 vs retrospective2024 end; grant extension not inspected'),
'Gareth Stedman Jones':('2019–2026','P03-S203','Targeted search returned honorary BA fellowship; not monetary funding'),
'Francesca Trivellato':('2006–2026','P03-S203;P03-S235;P03-S249','Earlier CV awards incl declined remain queue; visiting title alone not cash evidence'),
'Alexia Yates':('2019–2026','P03-S203;P03-S224','UKRI Gateway direct retrieval failed; AHRC amount unknown; Leverhulme prize lead pending'),
'Jessica Balguy':('2015–2026','P03-S205;P03-S226','ANR2015 Repairs/2020 Datas CV entries do not establish award nature; prizes delegated'),
'Joan Chaker':('2018–2026','P03-S210','Targeted search:2018 Orient-Institut doctoral fellow lead; no award details established'),
'Liane Hewitt':('2019–2026','P03-S206;P03-S240','SSRC/Chateaubriand/DAAD/JeanMonnet external support listed without dates or amounts'),
'Francesco Giosuè':('2023–2026','P03-S207;P03-S244','IdEx2023–24 lead open failed; CHEP grant handled separately'),
'Rébecca Mathiot':('2019–2026','P03-S207','Targeted search only CHEP award evidence; handled separately'),
'Giulio Piumelli':('2023–2026','P03-S207','Chicago exchange form/Alliance profile leads insufficient for award inference'),
'Aesa Virely':('2024–2026','P03-S207','Targeted search;2024 masters prize lead; CHEP grant handled separately'),
'Chiara Cordelli':('2004–2026','P03-S208;P03-S250','Earlier CV grants and declined offers not fully extracted'),
'Dev Patel':('2019–2026','P03-S209;P03-S248;P03-S424','NSF acknowledgement underlying PDF failed; EHP handled separately'),
'Emma Prevignano':('2019–2026','P03-S209;P03-S238;P03-S247','Cambridge/GerdaHenkel bursaries in LinkedIn lead require official corroboration'),
'Megan Ma':('2019–2026','P03-S211','Targeted search found profile/visits but no separately verified funding'),
'Sarah Glaser':('2020–2026','P03-S211;P03-S237','Undated Cambridge bursary may duplicate CHEP; do not add'),
'Marie-Emmanuelle Chessel':('2019–2026','P03-S211;P03-S242','SAB2024–26 verified; other older CV grants not extracted'),
'Thierry Mayer':('2012–2026','P03-S211','HETMAT ERC earlier grant lead passed to root'),
'Paul-André Rosental':('2011–2026','P03-S211','SILICOSIS ERC earlier grant lead passed to root'),
'Emma Rothschild':('2019–2026','P03-S211','Targeted search; joint institutional funding handled by institutional work package'),
'Lina Skoglund':('2025–2026','P03-S212;P03-S424','Targeted search; EHP funding handled separately'),
'Jingyi Huang':('2021–2026','P03-S212;P03-S425','Targeted search; excluded homonymous Wisconsin soil scientist grant'),
'Vincent Harmsen':('2025–2026','P03-S408','Targeted search dominated homonymous journalist and executive; no award attribution inferred'),
'Ebunoluwa Iyamu':('date_unknown–2026','P03-S408;P03-S246','GraduateInstitute/Leventis scholarships lead; direct403; datesunknown'),
'Natalia Lanko':('2022–2026','P03-S408;P03-S239','Language programme participation not equated to funded award'),
'Lucile Truffy':('2023–2026','P03-S408;P03-S245','VibekeSørensen2026 indexed official award; direct cache miss; earlier prizes pending'),
'Leonard le Roux':('2020–2026','P03-S411','CV inspected by support agent; external grants remain queue'),
'Hugo Carlier':('2022–2026','P03-S410','External targeted search found co-organised event and homonyms; no extra grant verified'),
'Aditya Balasubramanian':('2012–2026','P03-S425;P03-S432;P03-S256','DECRA award verified; earlier Marshall2013 scholarship lead not extracted'),
'Lola Zappi':('2019–2026','P03-S211;P03-S425','Targeted search returned EHP and prize leads; no extra external grant verified'),
'David Todd':('2019–2026','P03-S258;P03-S259;P03-S210','Targeted search; historical coordinator end date unknown; independent funding not established'),
'Abhijit Banerjee':('2019 award;2020 connection','P03-S309;P03-S261;P03-S262;P03-S263','Targeted Nobel2019 verification only; award authority confirms equal share; other grants/prizes not searched'),
'Esther Duflo':('2019 award;2020 connection','P03-S309;P03-S261;P03-S262;P03-S264','Targeted Nobel2019 verification only; source typo Duflot normalized; other grants/prizes not searched'),
'Jenny Andersson':('2012–2017 project;2020 connection','P03-S309;P03-S018','Targeted official FUTUREPOL verification; amount and exact award date unknown; other grants/prizes not comprehensively searched'),
}
coverage=[]
for p in cohort:
    name=p['name']; checked=checks.get(name)
    n=sum(name.lower() in f['beneficiary'].lower() for f in fund if f['parent_award_id']=='not_applicable')
    if checked: years,ss,gaps=checked;status='targeted_search_partial; see gap and separate support/prize coverage'
    else:years=p['connection_dates'];ss=p['source_ids'];gaps='Roster/source checked only; independent personal award search not undertaken';status='roster_only; award_search_pending_or_outside_support_role_scope'
    coverage.append(dict(entity_or_scheme=name,entity_type='person',person_id_if_applicable=p['person_id'],years_checked=years,sources_checked=ss,findings_count=n,gaps=gaps,completion_status=status))

def write(name,rows):
    with (OUT/name).open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
write('cohort.csv',cohort);write('people_funding.csv',fund);write('people_coverage.csv',coverage);write('people_sources.csv',sources)
print({'cohort':len(cohort),'funding_rows':len(fund),'source_rows':len(sources)})
