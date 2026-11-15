import json,csv,re
from pathlib import Path
p=Path(__file__).parent
parts=[json.loads((p/f).read_text()) for f in ['research_chep_map.json','research_candidates_root.json','research_candidates_a.json','research_candidates_b.json']]
sources=[s for d in parts for s in d['sources']]
sources.append(dict(source_id='P07-S034',url='https://histecon.fr/en/publications.html',title='Recent publications by CHEP participants',publisher_or_owner='CHEP',source_date='date_unknown',accessed_at='2026-11-15',source_type='institutional selected bibliography',supports='Research themes; selected outputs not complete census',retrieval_status='retrieved via web index; crawled three months before access'))
S={s['source_id']:s for s in sources}
def link(id):
 s=S[id];return f"[{s['title']}]({s['url']})"
C=[c for d in parts for c in d.get('candidates',[])]
short=['Guillaume Calafat','Marlous van Waijenburg','Destin Jenkins','Elizabeth Chatterjee','Elise Dermineur Reuterswärd','Anne L. Murphy','Hannah Farber','Stefania Barca']
common='P07-S007;P07-S033;P07-S005;P07-S009'
resp={
'Destin Jenkins':('Nicolas Delalande: public debt; Jonathan Levy: capitalism; both Paris-based proposed matches, inferred','P07-S015;P07-S014'),
'Vanessa Ogle':('David Todd: informal empire; Jonathan Levy: capitalism; inferred','P07-S016;P07-S017;P07-S014'),
'Marlous van Waijenburg':('Claire Lemercier: quantitative comparison; Nicolas Delalande: taxation and obligations; inferred','P07-S012;P07-S013;P07-S015'),
'Mary Bridges':('David Todd: informal empire; Jonathan Levy: capitalism; inferred','P07-S016;P07-S017;P07-S014'),
'Anne L. Murphy':('Nicolas Delalande: public debt; Claire Lemercier: economic institutions and methods; inferred','P07-S015;P07-S012'),
'Juliette Levy':('Claire Lemercier: comparative notarial methods; David Todd: economic networks; inferred','P07-S013;P07-S016'),
'Elise Dermineur Reuterswärd':('Claire Lemercier: comparative notarial methods; Jonathan Levy: credit and capitalism; inferred','P07-S013;P07-S014'),
'Hannah Farber':('Jonathan Levy: risk and capitalism; Guillaume Calafat: nearby maritime law; inferred','P07-S014;P07-S207;P07-S208'),
'Guillaume Calafat':('David Todd: Paris-based informal empire and Mediterranean legal sources; inferred. Francesca Trivellato is documented coauthor, a possible co-presenter not independent respondent','P07-S016;P07-S017;P07-S208'),
'Madeleine Dungy':('Nicolas Delalande: international political economy; David Todd: empire; inferred','P07-S015;P07-S017'),
'Hannah Catherine Davies':('Jonathan Levy: capitalism/risk; Francesca Trivellato: credit narratives (wider network; not assumed local); inferred','P07-S014;P07-S034'),
'Benjamin Bürbaumer':('Jonathan Levy: capitalism; David Todd: informal empire; inferred','P07-S014;P07-S017'),
'Matteo Pompermaier':('Claire Lemercier: quantitative methods; Jonathan Levy: credit/capitalism; inferred','P07-S013;P07-S014'),
'Elizabeth Chatterjee':('Giacomo Parrinello: environmental infrastructure and state/capital; Jonathan Levy: climate/capitalism; inferred','P07-S018;P07-S014'),
'Stefania Barca':('Nicolas Delalande: labour solidarity; Giacomo Parrinello: environmental history; inferred','P07-S015;P07-S018;P07-S322')}
previous={
'Guillaume Calafat':'verified scheduled: CHEP-supported Histoires, 2023-05-30 and 2023-10-17 (responsible series page); regional archive gives 2023-10-10, conflicting; no claim event held',
'Elizabeth Chatterjee':'verified scheduled: La matière du politique, 2022-04-08, Fuel Rioters; host-series precedent, not proof of a separate CHEP invitation or completed event',
'Vanessa Ogle':'verified scheduled: joint Cambridge/Harvard/Paris online seminar 2021-10-13; not Paris-only appearance',
'Paul Warde':'verified listed: joint online 2021-01-27; CHEP 2022-07-11; Paris workshop 2025-06-26; Cambridge joint workshop 2026-06-26; no attendance claim'}
for i,c in enumerate(C,1):
 c['candidate_id']=f'P07-C{i:03}'
 c['priority']='pilot_proposed' if c['name'] in short[:4] else 'shortlist_alternative' if c['name'] in short else 'reserve'
 c['previous_CHEP_appearance']=previous.get(c['name'],'not_found_publicly in checked Paris/host/joint corpus; not proof of no appearance')
 if c['name']=='Matteo Pompermaier':c['previous_CHEP_appearance']+='; regional archive lists PSE 2019-10-23 event, not evidence of CHEP sponsorship'
 if c['name']=='Fredrik Albritton Jonsson':c['previous_CHEP_appearance']+='; Scarcity suggested as future reading, not author participation'
 ids=c['source_ids']+';'+common
 if c['name'] in ['Guillaume Calafat','Matteo Pompermaier']:ids+=';P07-S022'
 if c['name']=='Fredrik Albritton Jonsson':ids+=';P07-S006'
 if c['name'] in resp:c['suggested_respondents'],extra=resp[c['name']];ids+=';'+extra
 c['source_ids']=';'.join(dict.fromkeys(ids.split(';')))
 if c['name']=='Paul Warde':c['CHEP_connection']='verified programme connection through joint online and Paris events; inferred fit with the climate programme'
 if c['name']=='Fredrik Albritton Jonsson':c['CHEP_connection']='inferred fit with economic ideas and climate; Scarcity appears as a suggested future reading, not author participation'
 c['CHEP_connection']=re.sub(r'\(S[0-9,–]+\)', '', c['CHEP_connection']).strip()
 c['as_of_date']='2026-11-15'
 c['evidence_status']='inferred'
 c['affiliation_evidence_status']='unverified' if c['name']=='Troy Vettese' else 'verified'
 c['appearance_evidence_status']='conflicting' if c['name']=='Guillaume Calafat' else 'verified' if c['name'] in previous else 'unverified'
 c['evidence_status_note']='Scholarly fit and proposed matches inferred; scholarship and public affiliation supported subject to evidence_read and retrieval caveats. No availability verified.'
fields='candidate_id name current_institution career_stage_if_documented public_profile_URL research_themes relevant_work work_date work_URL evidence_read proposed_topic CHEP_connection previous_CHEP_appearance suggested_respondents practical_unknowns rationale priority source_ids as_of_date evidence_status affiliation_evidence_status appearance_evidence_status evidence_status_note'.split()
def csvwrite(name,rows,fields):
 with (p/name).open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
csvwrite('candidates.csv',C,fields)
csvwrite('sources.csv',sorted(sources,key=lambda s:s['source_id']),'source_id url title publisher_or_owner source_date accessed_at source_type supports retrieval_status'.split())
B={c['name']:c for c in C}
briefs={
'Guillaume Calafat':('With Francesca Trivellato, Calafat uses a 1716 Mediterranean shipwreck to examine competing claims of sovereignty. The repository abstract makes legal categories and cross-confessional relations the basis for a focused historical problem.','Who could claim authority over passengers and property after a wreck?','Legal, Mediterranean, imperial and economic historians; students learning case reconstruction.','P07-S207;P07-S208;P07-S016;P07-S017','Abstract only; full article must be obtained lawfully or the session kept to an abstract-led source-design exercise. Paris affiliation suggests lower travel burden, not free participation. Revisit with 2024 work and acknowledge 2023 appearances.'),
'Marlous van Waijenburg':('Van Waijenburg estimates the fiscal value of coerced labour omitted from cash accounts in French colonial Africa. Her accessible methods essay explains why a conservative lower bound is preferable to false precision.','How should historians value a labour tax when records systematically undercount it?','African, imperial and economic historians; students learning measurement and source criticism.','P07-S105;P07-S106;P07-S107;P07-S108;P07-S013;P07-S015','Article abstract, full author essay and project abstract read; no full-book claim. New project publication date is unknown. US travel, online timing, fees and willingness unresolved.'),
'Destin Jenkins':('Jenkins connects municipal borrowing to unequal urban development in postwar San Francisco. The chapter abstracts identify credit ratings and finance institutions as mechanisms through which political choices shape infrastructure.','Who governs a city when creditors assess its future?','Urban, social and economic historians; students learning to map institutional causation.','P07-S101;P07-S102;P07-S015;P07-S014','Assessment rests on introduction/chapter abstracts, not full book. Suitable open orientation exists, but a full chapter requires lawful access. Stanford affiliation implies international logistics, not a known departure point.'),
'Elizabeth Chatterjee':('Chatterjee compares energy protests by US truckers and North Indian farmers. Her article examines how energy-dependent small owners organise demands on the state, connecting class formation to carbon-intensive livelihoods.','When does a claim to cheap energy become class politics—and where does the comparison break down?','Environmental, South Asian, social and economic historians; students practising comparative argument.','P07-S301;P07-S302;P07-S018;P07-S014;P07-S033','Open article abstract, opening and conclusion inspected; not a close reading of all sections. Related 2022 host-series talk makes this a proposed published-paper follow-up, conditional on convenor judgment. Online timing, fees and availability unverified.'),
'Elise Dermineur Reuterswärd':('Dermineur studies credit before banks through relationships and records in preindustrial France. Her author essay presents reciprocal obligations and renegotiation as features that complicate a purely institutional account of lending.','When does flexible credit include borrowers, and when does it reproduce exclusion?','Early modern, legal and economic historians; students working with probate or network evidence.','P07-S201;P07-S202;P07-S203;P07-S013;P07-S014','Publisher synopsis and full author essay read; full book not read. Stockholm affiliation suggests a European visit or online option, with itinerary, language, fees and availability unresolved.'),
'Anne L. Murphy':('Murphy reconstructs the eighteenth-century Bank of England through its working practices. Her open author essay juxtaposes fallible clerks with public service and institutional trust.','How did ordinary clerical work help a private bank become credible as a public institution?','Early modern, organisational and financial historians; students linking microhistory and state power.','P07-S111;P07-S112;P07-S113;P07-S015;P07-S012','Publisher account and complete short author essay read; not the book. Portsmouth is a potential UK option; senior administrative responsibilities reveal no availability. Travel, access and honorarium remain unresolved.'),
'Hannah Farber':('Farber explains how marine insurance helped build economic authority around the American founding. Her open essay uses a disputed insurance case to examine overlapping commercial and imperial legal orders.','Can a private insurance contract govern an empire?','Atlantic, maritime, legal and economic historians; students learning competing-claim reconstruction.','P07-S204;P07-S205;P07-S206;P07-S014;P07-S207','Publisher synopsis and full open author essay read; repository introduction blocked. Book first published 2021; paperback 2026. Columbia records leave through Spring 2027: location and availability require checking, not inference.'),
'Stefania Barca':('Barca’s publisher description foregrounds reproductive and subsistence labour as historical work sustaining life. It offers a way to question which workers environmental histories make visible, with a later book extending the discussion.','Whose work counts, and which archives reveal unpaid care and subsistence?','Labour, gender, environmental and economic historians; students evaluating categories of work.','P07-S303;P07-S304;P07-S305;P07-S015;P07-S018;P07-S322','Book descriptions and contents only; no close reading claimed. Before a substantive book session, obtain a permitted chapter; the open synopsis supports only orientation. USC affiliation, not older Coimbra biographies; fees, language, travel and willingness unknown.')}
text=['# P07 — Eight candidate briefs','\n**as_of_date: 2026-11-15. All cited sources accessed 2026-11-15. Draft for academic review.**\n','Order follows the proposed intellectual sequence, then alternatives; it is not a prestige ranking. All respondent matches and session designs are **inferred**. No invitations, availability or commitments are established. `sources.csv` supplies source dates and retrieval qualifications. The four pilot names remain conditional on the existing programme and duplication review.\n']
for n in short:
 c=B[n];con,q,a,ids,limits=briefs[n]
 text += [f'## {c["candidate_id"]} — {n}',f'**Documented position:** {c["career_stage_if_documented"]}, {c["current_institution"]}.',con,f'**Proposed question:** {q}',f'**Audience:** {a}',f'**Proposed respondent(s):** {c["suggested_respondents"]}.',f'**Prior record:** {c["previous_CHEP_appearance"]}.',f'**Evidence and practical limits:** {limits}','**Sources:** '+ '; '.join(link(i) for i in ids.split(';'))+'.\n']
(p/'shortlist.md').write_text('\n\n'.join(text))
# Qualitative judgments; no numeric score, no inferred acceptance probability.
rows=[]
for c in C:
 n=c['name'];rep=n in previous
 rows.append(dict(candidate_id=c['candidate_id'],name=n,research_fit='strong',conversation_specificity='strong' if n in short or n=='Oscar Sanchez-Sibony' else 'moderate',complementarity='conditional: returning/related topic; agree new contribution' if rep else 'moderate: plausible addition; archive/demand incomplete',student_learning='strong: open substantive essay/article/excerpt' if n in ['Marlous van Waijenburg','Elizabeth Chatterjee','Elise Dermineur Reuterswärd','Hannah Farber','Anne L. Murphy','Oscar Sanchez-Sibony','Paul Warde','Juliette Levy'] else 'conditional: abstract/description orientation; obtain permitted reading',feasibility='unverified: '+c['practical_unknowns'],recommendation=c['priority'],reason=c['rationale'],evidence_status='inferred',source_ids=c['source_ids']))
csvwrite('selection_matrix.csv',rows,list(rows[0]))
print('Wrote',len(C),'candidates;',len(sources),'source entries; shortlist',len(short))
