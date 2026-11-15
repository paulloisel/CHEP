import csv,json
from pathlib import Path
D=Path(__file__).resolve().parent.parent
read=lambda f:list(csv.DictReader((D/f).open()))
P,R,O,E,S=[read(f) for f in ['people.csv','roles.csv','organisations.csv','relationships.csv','sources.csv']]
pm={p['name']:p['person_id'] for p in P};om={o['short_name']:o['organisation_id'] for o in O};sm={s['source_id']:s for s in S};en={e['edge_id']:e for e in E}
# Counts refer to explicit categories; category overlap is intentional.
table='''| Checked category | Publicly supported coverage | Temporal rule |
|---|---|---|
| Paris coordination / website functions | 1 Coordinator; 2 coordination/web credits; 1 earlier agenda credit | Agenda continuation and effective appointment dates unconfirmed. |
| Earlier coordinators and council | 2 prior coordinators; 10 historical council identities | Council attestation is 2020, not a current committee roster. |
| Current academic contributors | 4 named helpers in host overview; Rosental also lists scientific-council membership | Do not convert these labels into an executive-committee roster. |
| Research associates | 20 names, all extracted; each linked profile lead checked, with alternatives or gaps recorded | Current roster listing; external employer labels can lag. |
| Fellows / postdoctoral researchers | 1 on fellows branch; 1 additional postdoctoral researcher on host page; 3 former fellows | Balguy and Chaker are distinct current entries; former periods retained. |
| Visitors | 1 Senior Research Fellow, 2025–2027; 2 visiting graduate students, 2021–2022 | A visitor category does not imply permanent membership. |
| Doctoral scholarship / exchange cohorts | 4 awardees in 2026; 4 in 2025; 4 selected for exchanges in 2020 | Named historical cohorts; previous-students index remains inaccessible. |
| Other supported connections | 1 facilitated Harvard stay; 1 EHP-CHEP fellow; 1 non-residential Lviv recipient | No current residency or permanent membership inferred. |
| Host and partner context | 11 CHSP function-holders; 9 Harvard governance/support people; 1 verified current Cambridge director plus 5 historical Cambridge role-holders | Overlapping people; Cambridge roster incomplete. |
| Participation boundary | 15 publication-page author identities, including 4 with no other established Paris role; 1 selected event-only speaker | Appearance alone is not membership. |
'''
counts=f'''- **{len(P)} unique person identities** in `people.csv`.
- **{len(R)} sourced role/category/period assertions** in `roles.csv`; parallel source labels are not distinct appointments.
- **{len(O)} organisation/unit/committee/programme entities** and **{len(E)} sourced relationship edges**.
- **{len(S)} distinct source URLs** in `sources.csv`, including failed retrievals, historical documents and alternate routes; URL count is not independent evidence count.
- **20/20 names** extracted from the accessible associate roster; **4/4** from the 2026 students page; **3/3** from the past-fellows page. Denominators describe those exact retrieved pages only.
- **2/2 Harvard governance/support branches** read, giving **9 unique people and 11 current assignments**. A historical Yang wording variant is deduplicated.
- **0 successful dated web-archive snapshots**. This is a retrieval result, not a claim that no snapshots exist.
'''
branch='''Five of the six direct Paris People branches yielded usable body text: Organisation, Fellows, Associates, Students and Visitors. The Executive Committee did not. The linked Past Research Fellows and Visiting Graduate Students pages were also read; Previous Research Students remained inaccessible. Historical student coverage was supplemented with a dated 2025 award notice and the host's 2020 selection account, without pretending to reconstruct the missing index. French associates contain the same 20 names; the French visitor body reproduces the Cordelli information. Current French student and committee routes were not retrievable.

All 20 associate profile leads were checked across the roster and supplementary passes; some linked pages failed, so retrieved institutional alternatives or older explicitly labelled biographies were used. All four 2026 students have sourced themes. Broader participant and host/partner records have deliberately uneven profile depth; `profile_coverage.csv` records selected profile URLs and whether themes are sourced, not found or inapplicable.'''
for fn in ['report.md','coverage.md']:
 text=(D/fn).read_text()
 for key,val in {'people_count':len(P),'roles_count':len(R),'org_count':len(O),'coverage_table':table,'counts_block':counts,'branch_coverage':branch,'fellows_status':'R','previous_students_status':'F','profile_queue':'Resolve Vincent Harmsen’s inaccessible profile, Thomas Lauvaux’s current external title, and the linked historical exchange-student profiles. No biography should be fabricated from a missing page.'}.items():text=text.replace('{{'+key+'}}',str(val))
 (D/fn).write_text(text)
# Resolve all diagram edges directly to the relationship inventory.
def edge(a,b,contains):
 matches=[e for e in E if e['from_id']==a and e['to_id']==b and contains in e['relationship_type']]
 assert len(matches)==1,(a,b,contains,matches)
 return matches[0]
formal=[
(edge(om['CHEP'],om['CHSP'],'hosted at'),'hosted at'),
(edge(om['CHSP'],om['Sciences Po'],'research centre of'),'research centre of'),
(edge(om['CHEP Executive Committee'],om['CHEP'],'listed People'),'listed branch; composition unverified'),
(edge(om['CHEP scientific council'],om['CHEP'],'scientific council of'),'scientific council; dated evidence'),
(edge(pm['Jonathan Levy'],om['CHEP'],'COORDINATOR'),'Coordinator'),
(edge(pm['Mary-Rose Cheadle'],om['CHEP'],'Coordination with'),'coordination with partner centres'),
(edge(pm['Amy Price'],om['CHEP'],'Web architect'),'Web architect'),
(edge(pm['Guillaume Piketty'],om['CHSP'],'role: Director'),'CHSP Director'),
(edge(pm['Violette Toye'],om['CHSP'],'Centre administrator'),'CHSP administrator'),
(edge(pm['Paul-André Rosental'],om['CHEP scientific council'],'Membre de Conseils'),'membership listed in current profile')]
partner=[
(edge(om['Joint Center'],om['CHEP'],'joint network site'),'network site'),
(edge(om['Joint Center'],om['CHE-Harvard'],'joint network site'),'network site'),
(edge(om['Joint Center'],om['CHE-Cambridge'],'joint network site'),'network site'),
(edge(om['CHE-Harvard'],om['Harvard'],'based at'),'based at'),
(edge(om['CHE-Cambridge'],om['Magdalene College'],'based at'),'based at'),
(edge(om['CHE-Cambridge'],om['King’s College'],'established at'),'1991 foundation; continuing collaboration'),
(edge(om['EHC'],om['CHEP'],'initiative based at'),'programme based at'),
(edge(om['EHC'],om['CHE-Harvard'],'initiative based at'),'programme based at'),
(edge(om['EHC'],om['CHE-Cambridge'],'initiative based at'),'programme based at'),
(edge(pm['Mary-Rose Cheadle'],om['CHE-Harvard'],'coordinates with'),'coordinates with; CHEP remit'),
(edge(pm['Mary-Rose Cheadle'],om['CHE-Cambridge'],'coordinates with'),'coordinates with; CHEP remit')]
labels={p['person_id']:p['name'] for p in P}|{o['organisation_id']:o['short_name'] for o in O}
labels[om['CHEP Executive Committee']]='CHEP Executive Committee<br/>current roster unavailable'
labels[om['CHEP scientific council']]='CHEP scientific council<br/>2020 roster; current individual evidence'
def diagram(items,orientation):
 out=['```mermaid',f'flowchart {orientation}']
 for n in dict.fromkeys(n for e,label in items for n in [e['from_id'],e['to_id']]):out.append(f'  {n.replace("-","")}["{labels[n]}"]')
 for e,label in items:
  connector='-.->' if ('unverified' in label or 'network' in label or 'programme' in label or 'coordinates' in label or '1991' in label) else '-->'
  out.append(f'  {e["from_id"].replace("-","")} {connector}|"{label} · {e["edge_id"]}"| {e["to_id"].replace("-","")}')
 out.append('```');return '\n'.join(out)
def edge_table(items):
 out=['| Edge | Meaning / temporal scope | Evidence |','|---|---|---|']
 for e,label in items:
  links='; '.join(f'[{sid}: {sm[sid]["title"]}]({sm[sid]["url"]})' for sid in e['source_ids'].split(';'))
  out.append(f'| {e["edge_id"]} | {e["valid_dates"]} | {links} |')
 return '\n'.join(out)
text='''# CHEP organisation and partnership maps

**as_of_date: 2026-11-15.** Draft for institutional review. These are evidenced functions and connections, not a discovered line-management structure. Nodes resolve to [people.csv](people.csv) or [organisations.csv](organisations.csv); edge IDs resolve to [relationships.csv](relationships.csv). All cited sources accessed 2026-11-15.

## 1. Formal organisation and documented functions

A solid arrow means the specific labelled host, function or body relationship is supported. It does **not** mean “reports to”. A dotted arrow highlights a navigation-only/unverified-composition link, a partnership or dated institutional context. The current Executive Committee composition is unknown. “Conseil scientifique” and “Executive Committee” remain separate labels until their equivalence and remit are confirmed.

'''+diagram(formal,'TB')+'\n\n'+edge_table(formal)+'''

The diagram shows two CHSP functions to make the host boundary visible. The full host support directory includes eleven people/functions in the tables; their CHEP allocations are not documented. Four scholars named as helping organise CHEP activities—Chessel, Mayer, Rosental and Rothschild—have collaboration records, not inferred executive-committee appointments. [CHSP support](https://www.sciencespo.fr/histoire/en/the-centre/research-directorate-and-support-team/); [French CHEP host overview](https://www.sciencespo.fr/histoire/fr/recherche/centre-for-history-and-economics-paris-chep/).

## 2. Partnership and research-programme map

The Joint Center node is a publicly documented network description, not an inferred legal parent. Programme and coordination arrows are connections, not supervisory authority. The CSV preserves college/university and Harvard FAS context beyond this compact view.

'''+diagram(partner,'LR')+'\n\n'+edge_table(partner)+'''

## Leadership/support overlay and historical context

| Centre / period | Documented public functions | Boundary |
|---|---|---|
| Paris, current checked listings | Jonathan Levy, Coordinator; Mary-Rose Cheadle, partner coordination; Amy Price, Web architect | Dates and employment/reporting arrangements not stated. [Organisation](https://histecon.fr/en/organisation.html). |
| Harvard, current checked listings | Emma Rothschild and David Yang, directors; Emily Gauthier, administration/finance; Jennifer Nickerson, research/fellowships; Amy Price, websites | Harvard roles do not create Paris membership. [Organization](https://histecon.fas.harvard.edu/organization.htm). |
| Harvard committee, current checked list | Abhijit Banerjee; Maya Jasanoff; Kenneth Mack; Emma Rothschild; Francesca Trivellato; David Yang | Same people may have separately evidenced Paris roles. [Executive Committee](https://histecon.fas.harvard.edu/executive.htm). |
| Cambridge, current corroborated leadership | Tim Harper, Director | Does not establish sole leadership or full committee/staff roster. [Cambridge profile](https://www.bennettschool.cam.ac.uk/about-us/person/tim-harper/). |
| Cambridge, historical observations | Harper Associate Director, Inga Huld Markan Executive Officer and Amy Price Webmistress in 2012; Paul Warde Director and William O’Reilly Assoc Director in 2021/22 | Current status not inferred from these observations. See source-linked role records. |
| Paris coordination history | Claire Lemercier with David Todd, 2019–2021; Todd coordination since 2022, attested in July 2025 | Levy's effective start and Todd's end remain unknown. [CV p. 11](https://lemercier.ouvaton.org/wp-content/uploads/2024/03/Lemercier-CV-mars-2024.pdf); [interview](https://www.sciencespo.fr/ecole-recherche/fr/actualites/entretien-avec-david-todd-directeur-des-etudes-en-histoire/). |

The 2007 announcement's joint-management and separate-executive-oversight arrangements are historical evidence for Cambridge/Harvard. They are not drawn as a current authority chain over Paris. [Harvard Gazette, 24 May 2007](https://news.harvard.edu/gazette/story/2007/05/harvard-cambridge-establish-joint-center-for-history-and-economics/).

**Before public use:** confirm the current Paris committee composition, terminology and remit; coordinator transition date; current Cambridge roster; and the institutionally preferred description of host versus partnership relationships. No assumption is made about who has committed to this review.
'''
(D/'organigram.md').write_text(text)
print(json.dumps({'people':len(P),'role_assertions':len(R),'organisations':len(O),'relationships':len(E),'sources':len(S),'formal_diagram_edges':len(formal),'partnership_diagram_edges':len(partner)},indent=2))
