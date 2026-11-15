# CHEP: parallel research prompts for a more active research community

Prepared on 15 November 2026 for a Master of Research student supporting Jonathan Levy and the Centre for History and Economics in Paris (CHEP).

The purpose is to arrive at a meeting with **documented findings, concrete prototypes, and feasible proposals**: things a student can help deliver, with clear benefits for researchers and students. These are prompts for future research runs, not completed reports or commitments by CHEP.

## How to run the prompts

**P01–P12 can run simultaneously. Run P13 after their reports are available.** The first four build reusable factual inventories; the others develop proposals and prototypes. No parallel prompt must wait for another: where an inventory is unavailable, it conducts its own focused research and labels the result provisional for later reconciliation.

For an agent with access to this file, use this launcher, replacing `PXX`:

```text
Read prompts_proposal.md. Execute PXX, applying the entire “Shared research brief and source map” section and the selected prompt. Do not execute the other prompts. Read Summary.md if available; if empty or unavailable, use the source map in the brief. Conduct the research, write the requested deliverables into the assigned reports/PXX_... directory, and finish with a short account of the findings and links to your outputs. For P01–P12, other reports are optional inputs: do not wait for them. Run P13 after the research runs finish; inventory available reports and flag missing workstreams before synthesising. Do not modify this prompt pack or another agent’s files.
```

For a research tool without file access, paste **the whole shared brief, including the source map, followed by one prompt**. Request the tables as copyable CSV blocks if attachments cannot be created. The prompts include structured research steps and short evidence-based explanations; they do not request private chain-of-thought.

| Prompt | Report or prototype | Output directory |
|---|---|---|
| P01 | Organisation chart, people directory, institutional relationships | `reports/P01_organisation/` |
| P02 | Publication census and research themes | `reports/P02_publications/` |
| P03 | Historical grants and funding ledger | `reports/P03_funding_history/` |
| P04 | Institutional timeline and event inventory | `reports/P04_timeline/` |
| P05 | Website audit and redesign brief | `reports/P05_website/` |
| P06 | Newsletter prototype and communications plan | `reports/P06_communications/` |
| P07 | Seminar speakers and research connections | `reports/P07_speakers/` |
| P08 | Symposium concepts and a pilot programme | `reports/P08_symposium/` |
| P09 | Current grants directory for students and affiliates | `reports/P09_opportunities/` |
| P10 | Annual research report prototype | `reports/P10_annual_report/` |
| P11 | Anniversary publication retrospective | `reports/P11_retrospective/` |
| P12 | Community-building and partnership programme | `reports/P12_community/` |
| P13 | Reconciled meeting brief and implementation choices | `reports/P13_synthesis/` |

If research capacity is limited, start with P01–P04, P09, and the two proposal prompts most useful for the next meeting. Running all twelve is an option, not a recommendation to implement twelve projects.

## Shared research brief and source map

**Include this entire section in every research run.**

### Role, purpose, and assumptions

You are a research assistant helping a Master of Research student prepare proposals for Jonathan Levy at CHEP. Investigate how the centre can support stronger scholarly exchanges, make its research more visible, connect people, and provide useful services to students and affiliates.

- Write in clear English. Preserve original French titles, names, and accents; supply French public-facing examples when the prompt requests them.
- Use the actual date of your run as `as_of_date`. Recheck roles, deadlines, events, and website content rather than inheriting this pack’s preparation date.
- Use **5 student hours per week and no confirmed discretionary budget** as a planning scenario, not a statement about actual resources. Show alternatives where useful. Give setup hours, recurring hours, and cash costs separately; label estimates and their assumptions.
- The student’s task description calls Jonathan Levy the head of CHEP. The public [organisation page](https://histecon.fr/en/organisation.html) identifies him as **Coordinator**. Verify the current wording and use documented institutional titles.
- `Summary.md` supplies four starting points: Sciences Po’s CHEP page and the Paris, Harvard, and Cambridge centre websites. Read it for any additions. The map below expands those starting points using official navigation; it does not establish that every page or record has been checked.
- Produce research, drafts, and recommendations. Do not send messages or invitations, subscribe to mailing lists, submit applications, change websites, or publish material.

### Initial source map

This is a starting map, not a completed crawl. Links below were retrieved or observed on official pages during the preliminary check on 15 November 2026. **R** means content was retrieved; **L** means the link was observed but its target could not be retrieved in that check. Retrieval failure is not proof that a public page is broken. Recheck both categories.

| Branch | Official starting links | Status and use |
|---|---|---|
| Paris overview | [CHEP English home](https://www.histecon.fr/en/); [French home](https://histecon.fr/fr/index.html); [English route supplied in Summary.md](https://histecon.fr/en/index.html) | R: English home alias and French home; supplied English route failed retrieval. Mission, navigation, institutional dates, notices, language comparison |
| Host institution | [Sciences Po CHEP page supplied in Summary.md](https://www.sciencespo.fr/histoire/en/research/centre-for-history-and-economics-in-paris-chep/); [alternate CHEP route](https://www.sciencespo.fr/histoire/en/content/centre-history-and-economics-paris-chep/) | R: host relationship and research community; check redirects and duplicate routes |
| People and organisation | [People](https://histecon.fr/en/people.html); [Organisation](https://histecon.fr/en/organisation.html); [Research fellows](https://histecon.fr/en/research_fellows.html); [Visitors](https://histecon.fr/en/research_visitors.html) | R: roster and role entry points; preserve current versus historical distinctions |
| Further people branches | [Executive committee](https://histecon.fr/en/executive_committee.html); [Associates](https://histecon.fr/en/research_associates.html); [Students](https://histecon.fr/en/research_students.html); [Past fellows](https://histecon.fr/en/research_fellows_past.html) | L: follow from People and fellows pages; do not omit these categories if retrieval is difficult |
| Research outputs | [Publications](https://histecon.fr/en/publications.html) | R: selected recent publications by participants, not a complete bibliography; follow publishers and author profiles |
| Projects and events | [Projects](https://histecon.fr/en/projects.html); [Seminars](https://histecon.fr/en/seminars.html); [Conferences, meetings and workshops](https://histecon.fr/en/events_sub.html) | L: discover dated subpages, programmes, PDFs, and archive links |
| Funding and news | [Research grants](https://histecon.fr/en/research_grants.html); [Announcements archive](https://histecon.fr/en/announcements_archive.html) | R: separate calls, awards, prizes, appointments, and project announcements |
| Communications | [CHEP mailing-list page](https://histecon.fr/en/list.html) | L: inspect public subscription information only; discover any public issue archive. A subscription form does not establish that an archive exists |
| Harvard centre | [Home](https://histecon.fas.harvard.edu/); [People](https://histecon.fas.harvard.edu/people_main.html); [Research](https://histecon.fas.harvard.edu/research_main.html); [Events](https://histecon.fas.harvard.edu/events_main.html); [News](https://histecon.fas.harvard.edu/news.html) | R: shared activities and cross-checks; Harvard affiliation alone does not establish Paris affiliation |
| Joint thematic programme | [Economic History, Climate, and the Environment](https://histecon.fas.harvard.edu/ehc/) | R: related projects, people, reading groups, and outputs; verify CHEP’s role item by item |
| Cambridge centre and earlier Paris material | [Cambridge home](https://www.histecon.magd.cam.ac.uk/); [historical Paris project](https://www.histecon.magd.cam.ac.uk/chep/) | L: partnership history and shared activities; try official alternate routes or dated archive snapshots if needed |

The rough navigation to expand is:

```text
CHEP Paris /en/ and /fr/
├── People → organisation / committee / fellows / associates / students / visitors / former fellows
├── Publications → publishers / author profiles / repositories
├── Projects → programme pages / collaborators / funding acknowledgements
├── Events → seminars / conferences and workshops → dated pages / programmes / archives
├── Grants → current calls / archived calls / recipient announcements
└── Announcements and contact → history / mailing list / public communication channels

Sciences Po /histoire/ → CHEP page / relevant profiles / events / research publications
Cambridge and Harvard centres → Paris-linked activities / shared programmes / historical cross-checks
External verification → publishers / repositories / funders / institutional profiles
```

**Two factual cautions to carry into the research:**

1. CHEP’s [home page](https://www.histecon.fr/en/) distinguishes the collaboration beginning in **2019** from the centre’s establishment in **2022**. A fifth anniversary of the latter would fall in **2027**, subject to confirmation of the intended institutional milestone. Investigate earlier activity rather than forcing all dates into one founding story.
2. At preparation, the [grant page](https://histecon.fr/en/research_grants.html) described 2027 support for eligible Sciences Po **PhD students**. This does not establish Master’s eligibility, an award to any individual, or the status of a future call. Recheck the full terms when executing P03 or P09.

### Research method

1. **Define the corpus.** State dates, people categories, institutional boundaries, and inclusions/exclusions. Centre the research on Paris. Use Cambridge/Harvard and wider Sciences Po selectively for documented connections; do not treat their entire membership or output as CHEP’s.
2. **Map before extracting.** Inspect navigation, language variants, archives, pagination, linked PDFs, and a sitemap where available. Produce a task-specific tree with URLs and retrieval status. Use targeted searches to find orphaned material, for example `site:histecon.fr "research fellows"`, `site:histecon.fr "bourse"`, and `site:sciencespo.fr/histoire "CHEP"`. Search results are leads; open the underlying sources.
3. **Extract and verify.** Prefer the responsible institution for roles and events, publishers/repositories for bibliographic metadata, and funders’ official calls for eligibility. Use dated archived official pages for historical states. Record publication date, event/award date, archive-snapshot date, and access date separately where relevant. Do not read copyright years or search-engine crawl dates as evidence of when an activity occurred. Identify cached/indexed retrievals when the tool exposes that information; an old cached page alone cannot establish the live site’s present condition.
4. **Reconcile.** Compare French/English versions and `www`/non-`www` aliases, preserving substantive differences. Deduplicate people, works, editions, event announcements, and awards. Prefer persistent identifiers where available. Do not let a stale search snippet override an inspected source without investigating the discrepancy.
5. **Interpret with restraint.** Separate documented facts, analytic inferences, and proposed actions. Provide a short methods-and-decisions note explaining consequential choices and unresolved conflicts, with evidence. Do not output private deliberation or an exhaustive reasoning transcript.
6. **Check coverage.** For inventories, traverse all discovered relevant branches and check each in-scope person/year/category. Stop when those branches and their relevant leads have been processed, or document the remaining queue and practical limit. “Comprehensive within the checked public corpus” is acceptable; “complete” without a defined, checked corpus is not. No arbitrary top-ten limit for a census.
7. **Turn research into decisions.** Connect each recommendation to a finding and explain the scholarly/community benefit, feasible first step, student workload, required support, maintenance burden, and a useful success measure.

Use public material and respect access restrictions and reasonable request rates. If automated crawling is possible, check site rules, cache responses, and avoid repeated bulk requests. If tools cannot browse or retrieve a source, state the limitation and leave claims unverified. Do not reconstruct missing evidence from memory.

### Evidence and data conventions

- Every substantive factual claim and inventory record needs a supporting **direct URL**, source title, and access date. Use inline Markdown links in prose and source IDs in tables. Provide short evidence notes or page/section locators where attribution is non-obvious.
- Use evidence statuses `verified`, `inferred`, `conflicting`, or `unverified`. Use explicit missing values such as `not_found_publicly`, `not_applicable`, and `date_unknown`; unknown is never zero. A recommendation may be plausible while its supporting demand remains untested.
- Give each record a workstream-prefixed ID, such as `P02-W001`. Record DOI/ISBN/ORCID or canonical URLs when available so the synthesis agent can reconcile duplicates. Do not invent identifiers.
- Preserve institutional role and affiliation dates. A participant, visitor, former fellow, committee member, and current affiliate are different categories. A collaboration link is not a reporting line.
- For money, preserve currency, period, recipient, award versus expenditure, and amount basis. Do not total unknown values or mix currencies, multi-year commitments, and annual spending.
- Use professional research information. Do not infer personal relationships, willingness to participate, or demographic attributes from names or photographs. Contact routes should be public institutional pages; avoid unnecessary personal data collection.
- Reproduce only brief necessary extracts; summarize research in your own words. Catalogue publications rather than copying full texts. Use cover images, photographs, and quotations in proposed publications only with an explicit rights/status check.

### Common deliverables and quality standard

Write only into your assigned directory. Produce:

1. **`report.md`**: a one-page decision brief first, followed by findings, the task-specific prototype or analysis, and a short methods/limitations section. Aim for 1,500–2,500 words of analysis; inventories and substantive draft artifacts may be longer. Do not truncate the evidence to meet the prose target.
2. **Task-specific tables/files** listed in the prompt, using UTF-8 CSV for substantial inventories and Markdown for drafts. If file output is unavailable, provide clearly named, copyable sections instead.
3. **`sources.csv`** with `source_id, url, title, publisher_or_owner, source_date, accessed_at, source_type, supports, retrieval_status`.
4. **`coverage.md`** with the task-specific source tree, sections/years checked, corpus counts, inaccessible sources, exclusions, conflicting evidence, unresolved questions, and the next retrieval steps. Give a percentage only if its denominator is known. Identify which conclusions require internal information.

The decision brief must answer: **What did we learn? What can CHEP do with it? What can the student deliver next? What support or decision is needed?** Supply up to three recommended actions, each with evidence, expected benefit, setup and recurring effort, cost assumptions, and a success measure. Suggest an owner by function where responsibility is not documented; never assign someone a commitment.

**Shared few-shot examples — fictional, for format only; never import them as CHEP findings:**

| Example finding | Evidence/status | Useful interpretation and next step |
|---|---|---|
| EX-A: An official 2023 page lists Person A as a fellow; a current directory does not list them. | Historical role verified; current status unverified; cite both inspected pages. | Record the historical fellowship. Current omission alone does not establish the end date. |
| EX-B: No public newsletter issues were located after checking the home page, subscription page, and news archive. | `not_found_publicly`; enumerate the checked sources. | Propose a public issue archive as an option and ask whether an internal archive already exists; do not claim CHEP has no newsletter. |

For a recommendation, use this pattern: **“Finding [source] → proposed action → benefit → estimated effort and assumptions → dependency → evaluation.”** For example, EX-C: “The checked calendar has no clearly labelled works-in-progress series → pilot three lunches → make unfinished research discussable → estimated three setup hours and two hours per session → room and an academic convenor → assess repeat participation and participant feedback.” This is an illustrative hypothesis, not an observed gap at CHEP.

## P01 — Organisation, people, and institutional relationships

```text
Apply the shared brief and source map. Write to reports/P01_organisation/.

TASK
Build the most comprehensive publicly supportable organisational map of CHEP, with a directory that can support a website, annual report, and community programme. Explain how Paris relates to its Sciences Po host and the Cambridge/Harvard centres without inventing a unified hierarchy.

RESEARCH STEPS
1. Traverse every People branch, the organisation and committee pages, relevant Sciences Po profiles, and historical snapshots. Record current and former coordinators, academic governance, administrative/communications functions, fellows, associates, students, visitors, and other explicitly named categories.
2. Create separate records for a person’s identity and each dated role/affiliation. Preserve exact source terminology. Identify participants appearing only on event or publication pages without automatically promoting them to members.
3. Map formal governance and support functions separately from partnerships and research collaboration. Check the official organisation/people pages of all three centres to include their documented leadership, committees, coordination, and administrative connections in a network overview; keep the exhaustive affiliate directory focused on Paris. Trace any proposed reporting line to explicit evidence; otherwise label the relationship “hosted at”, “coordinates with”, “member of”, or another supported term.
4. Summarize research themes and potential internal connectors using public work. Note missing or inconsistent profiles and which questions require institutional confirmation.

DELIVERABLES
- people.csv: person_id, name, category, institution, research_themes, profile_url, current_status, evidence_status, source_ids.
- organisations.csv: organisation_id, official_name, short_name, location, institutional_type, official_url, evidence_status, source_ids. Include the three centres and relevant host units so every relationship endpoint resolves to a documented entity.
- roles.csv: role_id, person_id, role_exact, organisation, start_date, end_date, date_precision, evidence_status, source_ids.
- relationships.csv: edge_id, from_id, to_id, relationship_type, valid_dates, evidence_status, source_ids.
- organigram.md: a Mermaid formal organisation chart plus a separately labelled partnership map, with a legend and citations for edges. If formal reporting lines are undocumented, show functions without inventing them.
- In report.md: a readable institutional explanation, directory coverage by category, and three practical uses for the student.

FEW-SHOT EXAMPLES — FICTIONAL
- EX-ROLE: Person A | visiting fellow | 2021–2022 | historical role verified | current affiliation unknown. Do not list Person A as a current permanent member.
- EX-EDGE: Centre A → University B | hosted at | official overview. This supports a host relationship, not a claim that the university president supervises the centre’s seminars.
```

## P02 — Publication census and research atlas

```text
Apply the shared brief and source map. Write to reports/P02_publications/.

TASK
Create a reusable catalogue of all discoverable published texts by documented CHEP-associated scholars within an explicit scope. It must support the website, annual report, speaker selection, and anniversary retrospective. Do not treat the selected books on CHEP’s website as a complete bibliography.

RESEARCH STEPS
1. Build or reuse a dated Paris roster. Define a core cohort of documented current/former Paris affiliates and a separate cohort of wider participants whose work CHEP features. Record inclusion evidence for each person. Do not expand to every Harvard/Cambridge scholar.
2. First inventory every item featured on CHEP’s publication pages. For documented Paris affiliates, then check institutional bibliographies/CVs, HAL or other institutional repositories, ORCID where available, and publisher/journal pages. Seek their available career bibliographies, retaining dates so relevant periods can be filtered. For wider participants, include CHEP-featured or explicitly Paris-connected works; do not automatically expand to their entire careers. If the cohort is too large to finish, complete and report clear person/category batches and leave an explicit remaining queue.
3. Include monographs, edited volumes, articles, chapters, working papers, substantial essays, reviews, and public scholarship, with types kept separate. Catalogue theses separately if included. Put unpublished manuscripts, datasets, recordings, and other non-text outputs in a supplementary table, not the published-text total.
4. Deduplicate records and link translations, editions, preprint/published versions, and multi-author works. Preserve original titles. Separate a work’s first publication from edition dates.
5. For each item distinguish: explicitly supported by CHEP; published during documented affiliation; authored by a current/former affiliate outside that period; featured participant publication; relationship unresolved. Publication during affiliation is not proof of funding or institutional causation.
6. Create a thematic research atlas grounded in abstracts, introductions, or available text. If only metadata was read, say so and do not invent an argument or scholarly contribution.

DELIVERABLES
- publications.csv: record_id, work_id, edition_or_version_id, title, authors, person_ids, type, first_publication_year, edition_date, venue_or_publisher, language, DOI_or_ISBN, canonical_url, open_access_url, themes, period_studied, geography_studied, CHEP_relationship, affiliation_evidence, support_evidence, verification_status, source_ids.
- cohort.csv: person_id, name, inclusion_category, Paris_connection, connection_dates, evidence_status, source_ids. Make the report self-contained even if P01 is unavailable.
- author_coverage.csv: person_id, cohort, sources_checked, years_covered, output_types_checked, gaps, completion_status.
- research_atlas.md: aim for 5–8 evidence-based thematic clusters and cross-person connections; use fewer if the corpus warrants it. Avoid prestige rankings or claims that raw publication volume measures quality.
- report.md: totals by clearly defined work/type/cohort/period, counting rules, gaps, and uses for CHEP.

FEW-SHOT EXAMPLES — FICTIONAL
- EX-W01: Original book, 2020; French translation, 2023 → two edition records linked to one work. An anniversary may feature the translation, but should not count two independent research projects.
- EX-W02: Article, 2018, by a person who joined in 2022 → member’s earlier scholarship; not “CHEP research produced in 2018” and not assumed CHEP-funded.
```

## P03 — Historical grants, awards, and funding flows

```text
Apply the shared brief and source map. Write to reports/P03_funding_history/.

TASK
Build a documented historical ledger of funding received by CHEP, received independently by associated researchers, and administered or distributed through CHEP. Keep this separate from P09’s directory of opportunities to apply for now.

RESEARCH STEPS
1. Search grants pages, dated calls and recipient announcements, project pages, annual reports, relevant member CVs, acknowledgements, and official funder award databases. Cover the earliest documented Paris collaboration to the run date; label earlier member awards separately.
2. Separate three funding relationships: incoming institutional/project funding; grants to individuals with a documented CHEP connection; support administered/distributed by CHEP. Record funder, legal recipient when stated, administrator, beneficiary, and project separately.
3. Separate awards actually announced from open/historical calls, prizes, donations, fellowships, and reimbursement ceilings. A call proves an opportunity, not an award or the number of recipients.
4. Link related records so an institutional grant and downstream studentships are not added twice. Verify amount, currency, award period, and whether the figure is a total, annual amount, maximum allowance, or expenditure. Never infer an award amount from a programme’s ceiling.
5. Assess what public evidence can establish and prepare a short, targeted list of missing records an administrator could supply. Do not reconstruct private finances or imply that a missing public award means no funding existed.

DELIVERABLES
- funding_ledger.csv: funding_id, parent_award_id, relationship_category, instrument_type, scheme, project, funder, recipient, administrator, beneficiary, CHEP_connection, award_date, start_date, end_date, amount, currency, amount_basis, award_or_call_status, evidence_status, source_ids.
- cohort.csv: person_id, name, inclusion_category, Paris_connection, connection_dates, evidence_status, source_ids. Establish the member cohort independently if P01 is unavailable.
- funding_coverage.csv: entity_or_scheme, entity_type, person_id_if_applicable, years_checked, sources_checked, findings_count, gaps, completion_status. Cover people, projects, schemes, and institutional funding; zero findings means no evidence located in the checked corpus.
- calls_and_unverified_leads.csv for opportunities or mentions that cannot establish an actual award.
- report.md: funding-flow diagram, reliable totals only where comparable, distribution by supported purpose where documented, missing evidence, and potential material for the annual report.

FEW-SHOT EXAMPLES — FICTIONAL
- EX-F01: A call offers “up to €800” to successful applicants; no awards are announced → call record, maximum allowance €800, recipient not_found_publicly; no awarded-total calculation.
- EX-F02: A €30,000 institutional award funds three €2,000 bursaries → record parent award and linked distributions; do not report €36,000 raised.
```

## P04 — Institutional timeline and event inventory

```text
Apply the shared brief and source map. Write to reports/P04_timeline/.

TASK
Reconstruct CHEP’s institutional history and public programme, producing the factual timeline needed for an anniversary, annual report, and future event planning.

RESEARCH STEPS
1. Investigate the start of the collaboration, formal establishment, any public launch, leadership changes, cohorts, major programmes, grants, and partnerships. Test the 2019/2022 distinction against dated official evidence. Record date precision and disagreements; do not force a single origin date.
2. Traverse seminar and conference/workshop pages, announcements, archived programmes, and relevant partner calendars. Build an event census from the earliest Paris-linked activity to the run date. Separate future announcements from historical activities.
3. For each event record title, date, format, speakers, organisers, partners, language, topic, location, and evidence of CHEP’s role. Deduplicate bilingual notices and cross-postings. Keep events merely advertised by CHEP distinct from events organised or co-organised by it.
4. Distinguish “announced”, “documented as held”, “cancelled/postponed”, and “status unknown”; a past date on an announcement does not prove an event occurred. Do not invent attendance or audience composition.
5. Analyse visible programming patterns and gaps, accounting for incomplete archives. Explain which anniversary windows are defensible and what an institutional confirmation would settle.

DELIVERABLES
- timeline.csv: milestone_id, date_start, date_end, date_precision, category, description, entities, significance, evidence_status, source_ids.
- events.csv: event_id, title, dates, status, format, speakers, organisers, partners, CHEP_role, topics, language, location_or_mode, programme_url, recording_url, source_ids.
- timeline.md: a concise visual or chronological narrative, aiming for 10–15 key milestones selected from the full inventory; use fewer rather than padding if evidence is sparse.
- report.md: origin-date assessment, coverage by year, programme patterns, and implications for an anniversary and future activities.

FEW-SHOT EXAMPLES — FICTIONAL
- EX-T01: A partnership begins in Year A; an institution is formally created in Year B → retain both milestones and name the anniversary basis explicitly.
- EX-E01: French and English notices describe the same workshop → one event, two source records; no attendance claim without a report or attendance evidence.
```

## P05 — Website audit and redesign brief

```text
Apply the shared brief and source map. Write to reports/P05_website/.

TASK
Prepare an evidence-based website improvement proposal that makes CHEP easier to discover, understand, and join. Deliver an audit, proposed navigation, and representative page copy for discussion. Do not build, modify, or publish a website.

RESEARCH STEPS
1. Map the public French and English sites, relevant Sciences Po landing pages, and links to Cambridge/Harvard. Identify apparent canonical pages, duplicates, archives, and missing or inconsistent content. Record retrieval failures separately from verified broken links; tools may fail on working pages. Distinguish observed content dates from search-index/cache dates, which cannot establish live staleness. Mark untested live-site or CMS issues as unknown.
2. Test six visitor journeys: a prospective student identifying relevant researchers; an affiliate finding funding; a visitor finding the next seminar; a scholar discovering research outputs; a new participant understanding how to get involved; and a journalist finding the centre's remit and public contact route. Record entry page, steps, successful outcome or obstacle, URLs, and evidence. Do not invent analytics or user-test findings.
3. Assess role/date accuracy, event freshness, publication discoverability, language parity, contact information, navigation and archive clarity. Where rendering tools permit, inspect mobile layout, keyboard navigation, headings, link labels and image descriptions. Clearly distinguish observed checks from an accessibility assessment requiring specialist testing; do not claim formal compliance.
4. Inspect two or three relevant research-centre websites for concrete practices worth adapting. Explain comparability, resource assumptions and what CHEP would gain. Do not recommend features simply because larger institutions have them.
5. Propose a small information architecture and reusable content fields for people, publications, events, grants and news. Define which records need institutional validation and who could maintain them by function. Preserve historical records and existing URLs where practical; flag potential redirect needs without assuming CMS access.
6. Prioritise improvements under the five-hours-per-week planning scenario. Separate content corrections a student can prepare from design/development tasks requiring institutional staff. Compare a minimal four-week content refresh with a larger redesign; estimate recurring maintenance as well as setup.

DELIVERABLES
- page_inventory.csv: page_id, URL, language, page_type, apparent_owner, last_update_evidence, audience_task, issue, evidence_status, proposed_action, source_ids.
- audit_backlog.csv: issue_id, affected_URLs, observed_problem, user_consequence, priority_rationale, proposed_fix, setup_hours_estimate, recurring_effort, required_role, dependency, verification_method.
- proposed_navigation.md: current-versus-proposed source/navigation trees, content types, bilingual policy and a short migration checklist.
- page_prototypes.md: an annotated text wireframe and complete draft copy for the homepage, one researcher profile template and one event page template. Use verified facts with citations; mark invented layout text and unavailable content explicitly. Include French and English homepage headings and participation calls to action. Do not promise services that CHEP has not approved.
- report.md: the three strongest improvements, screenshot references where available, a phased implementation estimate, and a maintenance plan. Define success through task completion and content freshness; treat traffic targets as proposed measures without a known baseline.

FEW-SHOT EXAMPLES — FICTIONAL
- EX-WEB01: A visitor reaches a past seminar page through the main “Events” link and finds no route to current dates → propose clearly separated Upcoming/Archive views; test whether a visitor can find the next verified event in two navigational steps. This is a proposed acceptance criterion, not measured performance.
- EX-WEB02: One language page lists a former coordinator and another lists a successor → prioritise factual reconciliation, cite both pages, and prepare consistent copy for institutional validation. Do not silently select a current title from visual appearance or search ranking.
```

## P06 — Newsletter prototype and communications plan

```text
Apply the shared brief and source map. Write to reports/P06_communications/.

TASK
Prepare a sustainable communications proposal and a substantive pilot newsletter that helps people participate in CHEP's intellectual life. Determine what already exists before proposing a new channel. Produce drafts only; do not subscribe, collect addresses, send messages, or publish.

RESEARCH STEPS
1. Map publicly visible communication channels: the centre's website and mailing-list page, any accessible newsletter archive, Sciences Po news and calendars, partner-centre channels, and linked public social accounts. Establish which channels are specifically CHEP's and which belong to the wider network. If no public newsletter archive is found, report the checked sources rather than concluding that no newsletter exists.
2. Define useful audience groups from documented activities: current researchers, students, former affiliates, potential seminar participants and wider scholarly readers. Identify a concrete information need and participation route for each. Mark audience size, preferences and engagement as unknown unless evidence exists.
3. Review recent public material and collect verified, timely content for a pilot issue: research, upcoming events, funding, member news and a participation opportunity where actually available. Separate new developments from evergreen introductions. Recheck all event dates and funding deadlines against the execution date; do not present past material as forthcoming.
4. Compare two or three university/research-centre newsletters for usable editorial practices, linking inspected issues. Propose a realistic cadence and a French/English strategy. Estimate collection, fact-checking, editing, translation, approval and distribution time; show how a compact issue could fit alongside the student's other responsibilities.
5. Define a repeatable workflow: public/member submissions, selection criteria, named-by-function editorial review, factual validation, link checks, publication and archive maintenance. Draft a short voluntary submission form, without creating or distributing it. Explain what can be repurposed from a single verified item across channels.
6. Propose meaningful evaluation: replies expressing research interest, event participation attributed through voluntary feedback, repeat contributors, and readership measures only if already available. Avoid invented baselines or promises of growth. Include an initial three-issue experiment and a review point.

DELIVERABLES
- channel_audit.csv: channel_id, owner, URL, intended_audience, observed_content, observed_frequency, archive_status, possible_overlap, evidence_status, source_ids.
- pilot_newsletter.md: publication-ready draft of approximately 600–900 words, subject line, preview text, concise editorial opening, linked research highlights, verified calendar/funding items and an appropriate participation call. Include French and English subject lines and opening paragraphs; label the principal issue language. Keep internal source/verification notes separate from reader-facing copy.
- editorial_calendar.csv: three proposed issues with theme, sections, candidate source items, collection/review dates relative to launch, owner_function, estimated_hours and dependencies. Unconfirmed content remains explicitly provisional.
- communications_playbook.md: issue template, selection rubric, voluntary submission questions, review workflow, reuse examples and maintenance checklist.
- report.md: recommendation on improving the existing arrangement or piloting an additional format, expected benefit, capacity assumptions and decisions needed. If current public material is too sparse for a full issue, deliver a shorter honest issue and a labelled content-request list.

FEW-SHOT EXAMPLES — FICTIONAL
- EX-COM01: “Research spotlight: Person A's new article examines municipal debt [publisher link]. Join the author's confirmed discussion on [verified date/event link].” Use the participation sentence only when such an event is documented; publication alone does not establish a forthcoming presentation.
- EX-COM02: No public issue archive is located → record not_found_publicly and propose an archive option conditional on the existing newsletter workflow. Never write “CHEP has never published a newsletter.”
```

## P07 — Seminar speakers and research connections

```text
Apply the shared brief and source map. Write to reports/P07_speakers/.

TASK
Develop an academically convincing seminar-speaker shortlist and proposed research connections. Each recommendation must link an identifiable piece of scholarship to CHEP's documented interests and explain what participants could learn. Provide material Jonathan Levy can evaluate; do not approach candidates or imply invitations, availability, or existing relationships.

RESEARCH STEPS
1. Build a focused picture of CHEP's research themes, people and recent programming from official sources. Use P01, P02 or P04 if available, but conduct direct checks if not. Distinguish established strengths, possible intersections and apparent programming gaps; an incomplete archive cannot prove that a topic has never been discussed.
2. Search institutional profiles, recent publisher/journal pages, working-paper repositories, conference programmes and upcoming scholarly projects for candidates. Include emerging scholars as well as established researchers, scholars within practical travelling distance and selected international possibilities. Examine disciplinary, methodological, geographic and period coverage using public scholarship; do not infer personal demographic characteristics.
3. Aim for a longlist of 18–24 well-supported candidates and a shortlist of eight, or fewer if the evidence is insufficient. These are planning targets, not an excuse to pad the list. For each shortlist candidate read enough accessible material to identify a substantive question; disclose when assessment rests only on metadata or an abstract.
4. Propose a particular talk, paper discussion or book conversation rather than a generic prestigious name. Suggest one or two intellectually suitable internal/nearby respondents using evidence from their work. Label every proposed match as an inference, not an established connection or commitment.
5. Rank recommendations with a transparent qualitative rubric: research fit, specificity of the proposed conversation, complementarity to recent programming, contribution to student learning and practical feasibility. Keep uncertain travel/availability separate from scholarly merit. Check whether a candidate has already appeared in the available CHEP record.
6. Build a balanced four-session pilot around a coherent question. Estimate student preparation and coordination separately from academic convening, hosting, travel and institutional support. Offer a local/online version where useful, without assuming either is free or that candidates would accept.

DELIVERABLES
- candidates.csv: candidate_id, name, current_institution, career_stage_if_documented, public_profile_URL, research_themes, relevant_work, work_date, work_URL, evidence_read, proposed_topic, CHEP_connection, previous_CHEP_appearance, suggested_respondents, practical_unknowns, rationale, priority, source_ids.
- shortlist.md: up to eight concise candidate briefs, each with a two-sentence research contribution, proposed question, intended audience, supporting sources and unresolved practical details.
- pilot_series.md: four sessions, their intellectual progression, proposed formats, student participation, timing assumptions, estimated workload and a lower-resource alternative. Include a short pre-reading/activity suggestion for each session where the source is accessible.
- invitation_drafts.md: two editable invitation drafts tied to different formats, with clearly marked placeholders for date, honorarium, travel support and institutional sender. Supply one French and one English draft. Do not invent authorisation to invite on the centre's behalf.
- report.md: strongest candidates, the selection rubric, limitations, and the minimum decisions needed to turn the shortlist into a programme.

FEW-SHOT EXAMPLES — FICTIONAL
- EX-SPK01: Person A's article uses shipping insurance records to study environmental risk → propose a paper discussion with Person B, whose documented research concerns commercial law. The connection is an evidence-based suggestion; it does not show that they know each other.
- EX-SPK02: Person C is based nearby and fits the theme → mark “potentially lower travel burden; availability and costs unverified.” Do not turn proximity into a claim that the visit is free or the invitation likely to be accepted.
```

## P08 — Symposium concepts and a feasible pilot programme

```text
Apply the shared brief and source map. Write to reports/P08_symposium/.

TASK
Develop three differentiated symposium or workshop concepts, then prepare a detailed proposal for the strongest feasible option. Make the intellectual purpose and expected community benefit explicit. This is a discussion package, not an announced event or a confirmed budget.

RESEARCH STEPS
1. Identify documented research strengths and possible connections across CHEP members, students and partner institutions. Review available recent CHEP and nearby institutional calendars to reduce duplication and identify useful complements. If other workstream reports are unavailable, establish a small sourced baseline independently.
2. Formulate three distinct questions that justify collective discussion: for example, a substantive historical problem, a methodological exchange or a conversation between emerging projects. Let the evidence determine the topics. For each, explain what the format could accomplish beyond a sequence of unrelated papers.
3. Specify audiences, scholarly objectives and possible outputs. Distinguish a working session for developing research from a public showcase. Include meaningful student roles such as presenting work, discussing sources or preparing a short synthesis; avoid allocating students only logistical labour.
4. Select plausible contributors and partners from documented work, with direct sources. Separate candidate speakers, respondents, convenors and institutional partners. Existing collaboration may support a proposal, but does not establish endorsement, funding or willingness to participate. Use P07's shortlist only after checking its evidence.
5. Compare practical variants: a small local half-day workshop, a fuller one-day meeting and a broader international version where justified. Estimate cash and labour separately, accounting for room arrangements, access needs, refreshments, travel/accommodation, recording if proposed and administrative support. Mark costs as planning estimates, dated quotes or unknown; do not imply confirmed funding or free services.
6. Choose one concept through explicit criteria: intellectual coherence, community benefit, evidence of participant fit, distinctiveness, student workload and institutional dependencies. Prepare a staged schedule under the five-hours-per-week scenario. If the preferred version exceeds that capacity, identify the required additional organiser/support and supply a smaller viable pilot.

DELIVERABLES
- concepts.md: three one-page concept notes with working title, 150-word rationale, audience, proposed questions, participant profile, format, likely output and principal tradeoffs.
- participants.csv: candidate_id, concept, proposed_role, institution, relevant_work_URL, contribution_rationale, connection_evidence, availability_status, source_ids. All uncontacted candidates have unconfirmed participation.
- pilot_programme.md: a timed programme for the selected option, session questions, provisional contributors/respondents, breaks, student involvement and a plan for capturing useful outcomes. Include one paragraph of public-facing draft copy, clearly marked as unpublished and provisional.
- budget_and_workplan.csv: item_or_task, cash_estimate_low, cash_estimate_high, currency, estimate_basis, student_hours, other_support_hours, owner_function, lead_time, dependency, status. Include setup, delivery and follow-up rather than only the event day.
- report.md: a comparison matrix, chosen pilot, a relative-date preparation calendar, key institutional decisions, and proposed evaluation. Measure the quality of discussion, new research exchanges and participant feedback; attendance targets remain assumptions until a venue and audience are known.

FEW-SHOT EXAMPLES — FICTIONAL
- EX-SYM01: Two researchers use court archives for different economic-history questions → propose a half-day source workshop with circulated extracts and student respondents. The deliverable is a shared methods note; a publication or edited volume is an optional later decision, not a promised outcome.
- EX-SYM02: A one-day meeting requires an estimated 35 student hours over six weeks → it exceeds the five-hour weekly scenario before other duties. Recommend additional organising support or a smaller half-day pilot, with revised estimates; do not disguise the workload as routine volunteering.
```

## P09 — Current funding opportunities for students and affiliates

```text
Apply the shared brief and source map. Write to reports/P09_opportunities/.

TASK
Create a dependable, current funding directory that helps CHEP-associated students and researchers decide where they can realistically apply. Cover archival travel, conference participation, research expenses, language or methods training, fellowships, and small collaborative activities. This is a prospective service, distinct from P03's historical ledger. It must be useful to a Master of Research student as well as doctoral and later-career researchers.

RESEARCH STEPS
1. Establish the public CHEP/Sciences Po context and create separate eligibility profiles: Master's student, early doctoral student, advanced doctoral student, postdoctoral researcher, and other affiliate. Do not assume nationality, residence, citizenship, or an employment contract. Record which missing applicant facts determine eligibility.
2. Search official Sciences Po opportunities, relevant French and European schemes, archival/library fellowships, learned societies, foundations, and Cambridge/Harvard-linked programmes where Paris eligibility is explicit. Use aggregators for discovery, then verify the current official call and applicable cycle. Do not import all partner-university funding as available to CHEP members.
3. Classify each opportunity as open, upcoming with an officially announced date, closed, recurring but next round unannounced, or unverified. Record application and referee deadlines separately, with time zone where stated. Never predict a new deadline from a previous year's date.
4. Check eligible degree stage, discipline, affiliation, geography, permitted expenses, award period, amount basis, application materials, referee requirements, host nomination, and restrictions on combining funding. Identify ambiguities without turning them into positive eligibility claims.
5. Rank practical fit using transparent criteria: verified eligibility, research relevance, useful funding purpose, preparation burden, and deadline readiness. Distinguish “worth monitoring” from “ready to apply”. Aim for 15–25 well-supported opportunities across profiles, but return fewer rather than dilute the list with unsuitable or stale calls.
6. Design a maintainable update process: responsible function, monthly check time, expiry labels, and a method for correcting entries. Do not apply, create accounts, or contact funders.

DELIVERABLES
- opportunities.csv: opportunity_id, scheme, funder, official_call_url, cycle, status, eligible_profiles, affiliation_rules, location_or_nationality_rules, eligible_costs, amount, currency, amount_basis, award_period, application_deadline, referee_deadline, timezone, materials, nomination_needed, fit_rationale, unresolved_eligibility, last_verified, source_ids.
- deadline_calendar.md: verified upcoming deadlines and preparation milestones; put unannounced future rounds in a separate watchlist.
- applicant_guide.md: a usable one-page selection guide for each profile, plus two application-preparation checklists built around verified opportunities. State clearly if no currently open Master's-eligible scheme was found.
- report.md: strongest options by applicant profile, gaps, and a low-maintenance service proposal. Include a sample 120-word bilingual funding notice grounded in one verified call.

FEW-SHOT EXAMPLES — FICTIONAL
- EX-G01: Scheme A funds first-to-third-year PhD students → eligible stage: early PhD; Master's: ineligible. The student's connection to CHEP does not override the degree rule.
- EX-G02: Scheme B closed on 10 May last year and has no new call → recurring/unannounced watchlist; next deadline unknown. Do not display “10 May this year” in the live calendar.
```

## P10 — Annual research report and reusable editorial system

```text
Apply the shared brief and source map. Write to reports/P10_annual_report/.

TASK
Prepare an evidence-backed prototype of a CHEP annual research report that makes the community's work legible to members, prospective students, partner institutions, and supporters. Produce actual sample editorial content, not only a table of contents. The report should celebrate scholarship without inflating institutional attribution or requiring excessive annual administration.

RESEARCH STEPS
1. Use the latest fully completed academic year, defined explicitly as 1 September–31 August, unless an official CHEP reporting period is documented. State the exact dates. Keep subsequent developments in a labelled postscript. If another period is more useful, explain and preserve a comparable twelve-month boundary.
2. Independently build a focused roster and inventory of publications, activities, projects, training, exchanges, and publicly documented support within that period. Existing P01–P04 outputs may help, but are optional and must be checked for scope, evidence, and reporting dates.
3. Define attribution rules: centre-organised, co-organised, centre-supported, member achievement, and wider-network news. Preserve affiliation timing. Choose research stories across career stages, methods, subjects, and types of contribution; do not equate publication counts with research quality.
4. Develop a narrative around three or four evidenced themes. Write short research profiles using accessible abstracts or texts; if only metadata is available, produce a bibliographic notice rather than pretending to explain the argument. Use no invented interviews, quotations, testimonials, or director's foreword.
5. Build a small indicator set with explicit definitions and denominators. Count unique works and events under consistent rules. Report announced activities separately from confirmed held events. Attendance, expenditure, grant totals, and readership remain unavailable unless supported; distinguish missing data from zero.
6. Create a repeatable submission and editing workflow: a short member contribution form, source checks, editorial ownership, translation, accessibility, rights checks, and annual archiving. Estimate setup and recurring effort against the shared student-capacity scenario.

DELIVERABLES
- annual_report_draft.md: a substantial six-to-eight-page-equivalent prototype containing a sourced overview, three 200–250-word research features, a junior-researcher section, a programme/partnership spread, a selected bibliography, and a documented-support section. Where evidence is insufficient, insert specific editorial queries rather than fictional copy. Mark all public-facing text as draft.
- indicator_register.csv: indicator, definition, period, value, unit, counting_rule, denominator, evidence_status, source_ids, missing_data_owner_function.
- content_register.csv: item_id, section, subject, CHEP_relationship, source_ids, image_or_quote_rights, fact_check_status, editorial_query.
- editorial_workflow.md: proposed calendar, roles by function, an eight-question contribution form, and update steps that reuse the underlying tables.
- report.md: purpose, audience, editorial choices, coverage limits, and a feasible minimum edition. Identify material that requires institutional verification before publication.

FEW-SHOT EXAMPLES — FICTIONAL
- EX-A01: A member published a book during a documented affiliation, with no CHEP acknowledgement → “A book by a CHEP affiliate”; do not write “Research funded by CHEP”.
- EX-A02: Eight workshops were announced; five have post-event documentation → report eight announcements and five documented held events. Do not claim eight completed workshops or invent attendance.
```

## P11 — Anniversary publication retrospective and celebration proposal

```text
Apply the shared brief and source map. Write to reports/P11_retrospective/.

TASK
Develop a scholarly retrospective that could accompany CHEP's proposed fifth-anniversary celebration. Make it a useful account of ideas, people, and research connections, supported by a defensible bibliography and institutional chronology. Treat the anniversary date as a question to establish, not a fact supplied by the project title.

RESEARCH STEPS
1. Verify the collaboration's beginning, formal establishment, and any launch. Explain possible anniversary bases and recommend a clearly named period. The initial sources distinguish 2019 collaboration from 2022 establishment; a fifth anniversary of the latter points to 2027, subject to institutional confirmation. If that anniversary is future, label the retrospective a preparation draft with a current evidence cutoff.
2. Independently construct the relevant publication corpus from CHEP pages, dated affiliations, author bibliographies, repositories, and publishers. P02/P04 are optional inputs. Keep the bibliography comprehensive within the declared cohort and period; distinguish this evidence inventory from the smaller editorial selection.
3. Separate work produced during affiliation, explicitly CHEP-supported work, earlier scholarship by later members, and publications featured by the centre. Connect translations and new editions to their original works. Explain inclusion rules for books, articles, chapters, essays, and student research, making room for contributions beyond senior scholars' monographs.
4. Identify four or five thematic conversations that connect the selected works. Read available abstracts, introductions, or texts before describing arguments. Do not infer intellectual influence or collaboration merely because people share a subject. Mark interpretive connections as editorial analysis.
5. Select 12–18 showcase items if the corpus supports that number, with a transparent rationale balancing themes, career stages, languages, and forms. Identify overlooked areas and rights-sensitive material. Ask for no full copyrighted texts to be reproduced.
6. Compare three feasible celebration formats: a digital retrospective, a small printed booklet with discussion, and a half-day research gathering. Show costs, student hours, partner support, lead time, and likely scholarly benefit. Recommend a minimum viable version suited to available capacity; make all participant involvement hypothetical until confirmed.

DELIVERABLES
- anniversary_basis.md: sourced milestone assessment, recommended framing, exact coverage dates, and the institutional question that would resolve remaining uncertainty.
- bibliography.csv and selection.csv: stable work IDs, bibliographic metadata, affiliation/support relationship, theme, selection rationale, source_ids, and rights/status notes.
- retrospective_draft.md: a proposed title, 300-word opening, four thematic section introductions, six polished 150-word publication cards, and a compact sourced timeline. Use real verified material; flag any missing research rather than filling gaps with invented content.
- celebration_options.md: three costed planning scenarios and a concrete programme for the preferred option, including discussion questions, student contributions, and a dissemination plan.
- report.md: editorial case, feasibility, unresolved dates, and the next work package the student can deliver.

FEW-SHOT EXAMPLES — FICTIONAL
- EX-R01: Centre A begins a partnership in 2018 and is formally established in 2021 → propose “Five years since establishment, 2021–2026”, with the partnership described as a prehistory.
- EX-R02: A 2024 translation of a 2020 book falls in the chosen period → feature the translation as a new edition; count one underlying work and explain why its reception matters.
```

## P12 — Community life, research connections, and useful peer practices

```text
Apply the shared brief and source map. Write to reports/P12_community/.

TASK
Design a modest programme that makes CHEP easier to join, more useful to early-career researchers, and better connected across projects and institutions. Prioritise recurring scholarly relationships and practical mutual help. Investigate what already exists before proposing additional events or administrative work.

RESEARCH STEPS
1. Map existing CHEP seminars, workshops, student activities, visitor programmes, communications, and relevant partner offerings. Verify whether activities are current or only historically documented. Identify publicly observable entry points and potential friction, while acknowledging that websites cannot establish participants' satisfaction, unmet demand, or attendance.
2. Describe three or four audience journeys: a new Master's student, a doctoral affiliate, a visiting researcher, and a Paris-based external collaborator. Distinguish documented access rules from proposed improvements. Do not assume every programme admits every audience.
3. Examine four to six relevant research centres or scholarly networks, including different resource levels. Find concrete practices documented on official sites: works-in-progress lunches, peer feedback, methods clinics, reading groups, visitor introductions, research directories, or grant-writing support. Cite how each works; do not infer success from its existence or copy a large institution's staffing assumptions.
4. Build a practice-transfer matrix linking each potentially useful idea to a CHEP need hypothesis, existing provision, audience, adaptation, effort, and evidence still required. Recommend strengthening a current activity where that is more feasible than creating another one.
5. Develop a twelve-week pilot comprising at most three connected activities within an average of five student hours per week. Specify academic support, room/platform requirements, preparation, follow-up, language access, and how newcomers enter. Use public research interests to suggest intellectual connections, never presumed personal relationships or willingness to participate.
6. Draft a lightweight needs assessment for later use, without distributing it. Define learning goals and measures such as repeat participation, useful feedback exchanged, or continued research conversations. Avoid prestige rankings, demographic inference, and intrusive individual tracking. Provide a stop/adapt decision rule if demand or support is insufficient.

DELIVERABLES
- comparator_practices.csv: centre, practice, audience, documented_mechanism, source_url, resource_evidence, possible_adaptation, limits_of_comparison.
- community_map.md: existing provision, entry points, research-theme connections, and gaps framed as testable hypotheses.
- pilot_plan.md: a week-by-week calendar, total setup and recurring hours, cost assumptions, proposed roles, and three fully specified session plans with agendas and follow-up outputs. Include an example welcome page and a reusable two-paragraph event invitation draft; do not send it.
- needs_assessment.md: six neutral questions, an optional conversation guide, proposed data minimisation, and how findings would change the pilot.
- report.md: the strongest proposal, what it builds on, who benefits, evidence limits, and continuation criteria.

FEW-SHOT EXAMPLES — FICTIONAL
- EX-C01: Centre B documents a monthly draft-paper lunch → evidence of a format, not evidence of impact. Adapt to a three-session CHEP pilot only after checking existing provision and likely convenor capacity.
- EX-C02: A current reading group already covers the proposed theme → propose a newcomer welcome note and rotating student discussants, instead of assuming a second group is needed.
```

## P13 — Reconcile the reports and prepare the meeting with Jonathan Levy

```text
Apply the shared brief and source map. Write to reports/P13_synthesis/.

TASK
Run this prompt after research reports are available. Turn their findings and prototypes into a concise, coherent meeting pack for Jonathan Levy. Help the student propose a small number of useful contributions that fit real capacity, while making the evidence and unresolved decisions easy to review. Do not simply concatenate the reports or imply that every proposed project should proceed.

RESEARCH STEPS
1. Inventory P01–P12 outputs, including their as-of dates, source registers, coverage, prototypes, and missing files. Proceed with available material and identify which decisions lack support. Do not fabricate absent reports or silently treat partial research as complete.
2. Reconcile people, affiliations, works/editions, events, milestones, and funding using stable identifiers, canonical URLs, dates, and original source records. Preserve an ID crosswalk rather than overwriting other agents' files. Resolve consequential disagreements against inspected primary evidence; retain unresolved alternatives and explain their practical implications.
3. Check sensitive factual foundations: current institutional roles, Paris versus wider-network attribution, anniversary basis, grant eligibility/deadlines, unique publication counts, and grant-versus-expenditure totals. Reverify time-sensitive items at synthesis time. Do not award credibility merely because a claim appears in several reports drawing on the same source.
4. Compare proposed actions by scholarly/community benefit, evidence of need, student effort, ongoing maintenance, cash cost, external dependencies, and reversibility. Make scores and weights transparent if used; a brief qualitative comparison is preferable to spurious precision. Separate validated needs from promising hypotheses.
5. Develop three alternative portfolios: a low-effort service improvement, a community-building pilot, and a research-visibility package. Show the combined setup and weekly workload, including maintenance and coordination, against the five-hour-per-week planning scenario. Explain what must be deferred if a portfolio exceeds capacity.
6. Recommend one portfolio with no more than three initial actions. Specify the student's first deliverable, suggested institutional counterpart by function, milestones, dependencies, and success/stop criteria. Distinguish a decision on strategic fit from later permission needed to publish, spend, or contact people.
7. Prepare a short meeting sequence that opens with concrete findings and prototypes, then reaches a small number of decisions. Draft only; do not send the pack or schedule a meeting.

DELIVERABLES
- meeting_brief.md: a two-page maximum brief with five sourced findings, the recommended portfolio, its total resource needs, and three precise decisions for discussion.
- proposal_comparison.csv: proposal, supporting_report_ids, evidence_strength, benefit, setup_hours, recurring_hours, estimated_cash, dependencies, maintenance_owner_function, recommended_status.
- reconciliation_log.csv and id_crosswalk.csv: conflicting claims or duplicates, underlying evidence, resolution/status, and affected outputs.
- 90_day_plan.md: phased tasks, concrete outputs, owners by function, workload totals, review points, and items explicitly deferred.
- meeting_agenda.md: a twenty-minute agenda and a one-minute opening statement; link the most persuasive prototypes rather than recreating all their content.
- report.md: synthesis methods, remaining uncertainty, and links to every input and final artifact.

FEW-SHOT EXAMPLES — FICTIONAL
- EX-S01: Three proposed initiatives require two hours weekly each → six hours before coordination; the five-hour scenario cannot support all three. Recommend two and defer the third, with the trade-off stated.
- EX-S02: Two reports repeat an unverified membership claim from one old page → one unresolved evidence chain, not independent corroboration. Keep the person outside confirmed-current totals until resolved.
```
