# P01 coverage, source tree and unresolved questions

**as_of_date: 2026-11-15; access date for all sources: 2026-11-15.** This is a Paris-centred public organisation/directory inventory, not a census of all people at Cambridge, Harvard or Sciences Po. `Summary.md` was present and read: its four starting URLs added no further instructions or evidence. Only P01 was executed; other report files were not inputs.

## Defined corpus

Included: every discovered Paris People category; named current and former coordination/support functions; dated historical scientific-council records; Paris-affiliated research fellows, associates, students and visitors; explicitly documented scholarship/support participants; relevant current host functions; partner leadership, committees and support; and clearly labelled publication participants/selected event speakers to preserve the boundary between participation and membership.

Temporal scope: current public listings checked on the access date; Paris historical material from the pre-establishment collaboration and dated 2020 records onwards; prior coordination explicitly dated 2019–2021; selective partner governance history back to the 2007 joint-centre announcement and earlier foundation facts it reports. Dates are only as precise as their sources. A role listed in a 2021/22 report is an observation during that reporting period, not an invented two-year appointment.

Excluded: exhaustive partner affiliate lists, the entire Sciences Po faculty, all historical careers, private membership/employment records, events and publications censuses, grant amounts and eligibility research, personal contact harvesting and inferred personal relationships. Programme pages were used only to establish organisational connections or public research themes. No communications were sent and no material was published.

## Task-specific source tree

**R** = body/content retrieved, usually via an indexed web-tool copy; **P** = partial or mixed retrieval; **F** = attempted, no usable underlying content; **L** = observed link or unresolved lead. These codes describe this research run, not live website health. Exact observations, titles, owners and access metadata are in [sources.csv](sources.csv).

- Paris entry points
  - **R** [English home, www alias](https://www.histecon.fr/en/) — mission, CHSP host, 2019/2022 dates, EHC link, notices.
  - **F** [English index route in Summary](https://histecon.fr/en/index.html) — HTTP 406; alternate home used.
  - **R / older indexed content** [French home](https://histecon.fr/fr/index.html) — source of bilingual comparison, not current events evidence.
  - **R** [People](https://histecon.fr/en/people.html) — six primary category links; no pagination observed in retrieved body.
    - **R** [Organisation EN](https://histecon.fr/en/organisation.html) — three current public function labels.
    - **P** [Organisation FR](https://histecon.fr/fr/organisation.html) — older open response names Todd/Egea; newer search response names Levy. Direct GET returned 406. Live bilingual discrepancy is **not established**.
    - **F** [Executive Committee](https://histecon.fr/en/executive_committee.html) — open, click, www/HTTP variants failed. Current composition remains unknown.
    - **R** [Research Fellows](https://histecon.fr/en/research_fellows.html).
      - **R** [Past Research Fellows](https://histecon.fr/en/research_fellows_past.html) — three entries with stated periods.
    - **R** [Research Associates](https://histecon.fr/en/research_associates.html) — all 20 listed identities extracted; linked profiles checked to the extent recorded in the profile register.
    - **R** [Research Students 2026](https://histecon.fr/en/research_students.html) — all four named students; links to profiles and former cohorts.
      - **F** [Previous Research Students](https://histecon.fr/en/research_students_previous.html) — outcome detailed below.
    - **R** [Research Visitors](https://histecon.fr/en/research_visitors.html) — exact appointment terminology distinguished from page category.
      - **R** [Visiting Graduate Students](https://histecon.fr/en/visiting_graduate_students.html) — Dev Patel and Emma Prevignano, 2021–2022.
  - **R** [Announcements archive](https://histecon.fr/en/announcements_archive.html) — affiliation/support checks, including Jingyi Huang and Ivanna Cherchovych; not an awards ledger.
  - **R** [Publications](https://histecon.fr/en/publications.html) — all 15 unique named authors identified, with participation-only classification where no affiliation was established.
  - **R** [Recent Events](https://histecon.fr/en/events_recent.html) and [dated Sciences Po CHEP event](https://www.sciencespo.fr/histoire/en/events/centre-for-history-and-economics-in-paris-chep/) — selective boundary and institutional-role checks, no event census.
  - **R** [French agenda](https://histecon.fr/fr/agenda.html) — Anna Egea credit; visible 2024–June 2025 entries; wider Paris scope.
  - **R** [Contacts](https://histecon.fr/en/contacts.html); **F** [mailing list](https://histecon.fr/en/list.html) — public routes only; no subscription.
  - **F** [robots.txt](https://histecon.fr/robots.txt) and [sitemap.xml](https://histecon.fr/sitemap.xml) — direct requests returned 406. No bulk crawl performed; navigation and targeted retrieval used.
- Sciences Po host and historical records
  - **R** [English CHEP research page](https://www.sciencespo.fr/histoire/en/research/centre-for-history-and-economics-in-paris-chep/) and [alternate content route](https://www.sciencespo.fr/histoire/en/content/centre-history-and-economics-paris-chep/) — same body, counted as one evidence chain, not independently corroborating institutions; HTTP redirect itself not established.
  - **R / mixed indexed versions** [French CHEP page](https://www.sciencespo.fr/histoire/fr/recherche/centre-for-history-and-economics-paris-chep/) — opened body has Levy, two postdoctoral researchers and explicit 2026 cohort; older search extract retained a prior roster and was not used for current membership.
  - **R** [CHSP direction/support](https://www.sciencespo.fr/histoire/en/the-centre/research-directorate-and-support-team/) — all eleven named functions/holders included as host context, not dedicated CHEP appointments.
  - **R** [CSO staff](https://www.sciencespo.fr/cso/en/cso/technical-and-administrative-staff/) — Egea's documentation function.
  - **R** [2020 scientific-council minutes](https://www.sciencespo.fr/sites/default/files/cd_cp/cs/2020/2020_03_10_CSFR.pdf), section 10, pp. 14–15 — meeting 2020-03-10; version validated 2020-06-02. Ten historical council names; CSO/CHSP context.
  - **R** [Todd interview](https://www.sciencespo.fr/ecole-recherche/fr/actualites/entretien-avec-david-todd-directeur-des-etudes-en-histoire/), 2025-07-21 — coordination since 2022.
  - **R** [Lemercier CV](https://lemercier.ouvaton.org/wp-content/uploads/2024/03/Lemercier-CV-mars-2024.pdf), 2024-03-12, p. 11 — co-coordination with Todd, 2019–2021; author domain linked by institutional profile.
  - **R** Dated scholarship notices: [2025 recipients](https://www.sciencespo.fr/ecole-recherche/en/news/quatre-doctorants-du-centre-d-histoire-laureats-de-la-bourse-d-excellence-du-chep/), 2025-02-07; [2026 recipients](https://www.sciencespo.fr/ecole-recherche/fr/actualites/quatre-jeunes-chercheurs-histoire-laureats-bourse-chep-2026/), 2026-01-28.
  - **R/P** Individual institutional profiles — see [profile_coverage.csv](profile_coverage.csv). Professional subjects only; missing themes remain explicit.
- Harvard partner
  - **R** [Home](https://histecon.fas.harvard.edu/index.html) → [People](https://histecon.fas.harvard.edu/people_main.html) → [Organization](https://histecon.fas.harvard.edu/organization.htm) and [Executive Committee](https://histecon.fas.harvard.edu/executive.htm).
  - **R** [Contact](https://histecon.fas.harvard.edu/contact.htm), [Yang welcome](https://histecon.fas.harvard.edu/yang_welcome.html) (2023-09-12), [Gauthier profile](https://histecon.fas.harvard.edu/Emily_Gauthier.htm) and linked academic profiles.
  - **R** [2007 establishment announcement](https://news.harvard.edu/gazette/story/2007/05/harvard-cambridge-establish-joint-center-for-history-and-economics/) — historical committee arrangements, no current Paris hierarchy inferred.
- Cambridge partner and historical Paris branch
  - **F** [Centre home](https://www.histecon.magd.cam.ac.uk/), HTTP/non-www aliases and candidate People/organisation routes — 403/502 or inaccessible; candidate paths do not prove those pages exist.
  - **F** [Historical CHEP project](https://www.histecon.magd.cam.ac.uk/chep/) and [Conseil scientifique](https://www.histecon.magd.cam.ac.uk/chep/conseil_scientifique.html) — source-map and host-linked historical entry points.
  - **R** Responsible-institution substitutes: [Tim Harper profile](https://www.bennettschool.cam.ac.uk/about-us/person/tim-harper/); [Magdalene 2025 magazine](https://www.magd.cam.ac.uk/sites/default/files/2025-07/Magdalene%20Matters%20Issue%2055.pdf); [Magdalene November 2012 magazine](https://www.magd.cam.ac.uk/sites/default/files/2025-05/magdalene_matters_issue_36.pdf); [King's publication scheme](https://www.kings.cam.ac.uk/kings-college-cambridge-publication-scheme); [CAMPOP 2021/22 report](https://www.campop.geog.cam.ac.uk/about/annualreports/annualreport2022.pdf); [Trinity Hall 2021/22 review](https://www.trinhall.cam.ac.uk/wp-content/uploads/2023/10/S01018_Trinity_Hall_Review_OS_22_SG_WEB-1.pdf); [Cambridge library guide](https://libguides.cam.ac.uk/history/EconomicandSocialHistory).
  - **P/L** [Magdalene magazine archive](https://www.magd.cam.ac.uk/alumni/publications/college-magazine) — directory read; selected Issuu targets unavailable. Juliet White accountant lead remains excluded from verified roles.
- Shared programme
  - **R** [Economic History, Climate, and the Environment](https://histecon.fas.harvard.edu/ehc/) — explicit Paris/Cambridge/Harvard programme relationship and selected themes; not its entire participant roster.
- Web archive
  - **F** Internet Archive CDX query and nearest-2024 organisation request, logged in sources. **No dated snapshot successfully retrieved**; a requested timestamp is not a snapshot date. Historical findings use dated responsible-source documents instead.

## Counts and completion boundary

- **72 unique person identities** in `people.csv`.
- **126 sourced role/category/period assertions** in `roles.csv`; parallel source labels are not distinct appointments.
- **22 organisation/unit/committee/programme entities** and **151 sourced relationship edges**.
- **133 distinct source URLs** in `sources.csv`, including failed retrievals, historical documents and alternate routes; URL count is not independent evidence count.
- **20/20 names** extracted from the accessible associate roster; **4/4** from the 2026 students page; **3/3** from the past-fellows page. Denominators describe those exact retrieved pages only.
- **2/2 Harvard governance/support branches** read, giving **9 unique people and 11 current assignments**. A historical Yang wording variant is deduplicated.
- **0 successful dated web-archive snapshots**. This is a retrieval result, not a claim that no snapshots exist.


Five of the six direct Paris People branches yielded usable body text: Organisation, Fellows, Associates, Students and Visitors. The Executive Committee did not. The linked Past Research Fellows and Visiting Graduate Students pages were also read; Previous Research Students remained inaccessible. Historical student coverage was supplemented with a dated 2025 award notice and the host's 2020 selection account, without pretending to reconstruct the missing index. French associates contain the same 20 names; the French visitor body reproduces the Cordelli information. Current French student and committee routes were not retrievable.

All 20 associate profile leads were checked across the roster and supplementary passes; some linked pages failed, so retrieved institutional alternatives or older explicitly labelled biographies were used. All four 2026 students have sourced themes. Broader participant and host/partner records have deliberately uneven profile depth; `profile_coverage.csv` records selected profile URLs and whether themes are sourced, not found or inapplicable.

The current Paris executive-committee branch remains unenumerated, so no defensible denominator exists for complete Paris membership. Cambridge's missing current committee/support roster likewise prevents a percentage for partner coverage. All names in successfully retrieved in-scope roster bodies were processed; individual profile coverage and unresolved leads are separately recorded. “Comprehensive within the checked public corpus” refers to those bodies, not every possible affiliate, employment contract or historical appointment.

## Consequential conflicts and decisions

1. **Coordinator succession.** Prefer Levy for current public wording because CHEP Organisation and opened Sciences Po CHEP pages agree. Preserve Todd's historical roles and the stale/conflicting profile wording. His 2025 interview is evidence of an attestation, not the end of his tenure or Levy's start date.
2. **Same URL, different indexed content.** French CHEP Organisation and Sciences Po CHEP search/open copies differ. Record retrieval metadata; do not diagnose a live translation problem from cached results. Root's direct public GET checks also returned 406.
3. **Anatole Le Bras.** Past-fellows body says 2021–2023; homepage calls him a fellow since 2023; a dated [Sciences Po event biography, 23 January 2024](https://www.sciencespo.fr/histoire/fr/evenements/alienes-une-histoire-sociale-de-la-folie-au-xixe-siecle/) explicitly says he joined in September 2023. Keep the former-fellows interval as an explicitly sourced claim, flag the conflict, and preserve the independently documented current associate category. Do not manufacture a continuous fellowship or choose a corrected start date.
4. **Scientific council versus Executive Committee.** A 2020 council roster and Rosental's current profile do not establish the current English committee's membership or prove equivalence of the labels. Ten historical identities are retained, including two described as previously included.
5. **Earlier origins.** The 2020 minutes' imprecise retrospective wording suggests activity before the current 2019 collaboration date. No exact earlier start is inferred. Establishment in 2022 remains the clear current institutional claim; the intended anniversary basis needs confirmation.
6. **Name reconciliation.** Minutes' “Duflot” and “Parinello” are reconciled to Esther Duflo and Giacomo Parrinello using official institutional profiles. The matching is an explicit inference; canonical spellings are verified. Other variants include Eric/Éric Monnet, M’Hamed/M’hamed Oualdi and Kenneth Mack/Kenneth W. Mack.
7. **Affiliation versus employment.** Current associates include former fellows. A publication appearance alone, shared grant theme, historical scholarship, or Harvard affiliation is insufficient for Paris membership. Host support roles do not establish CHEP-specific remit. [EUI’s September 2024 notice](https://www.eui.eu/news-hub?id=four-new-professors-join-the-history-department&lang=en-GB) updates the roster labels for Alexia Yates and M’Hamed Oualdi; current EUI and Sciences Po profiles establish the latter’s secondment context. Marion Fontaine’s current annuaire and CHSP support page identify her as head of the History Department, while an older linked profile retains doctoral-studies wording.
8. **Partner dates.** Yang was described as new director on 2023-09-12; this is not an exact start date. Gauthier joined the centre in 2009; that is not necessarily when her present title began. Cambridge historical roles stay historical unless independently reverified.

## Remaining queue and internal information needed

Priority 1: obtain a dated current Paris committee list and definition of its remit; confirm the executive/scientific-council terminology; establish the Levy/Todd succession date and how former/associate/student status is assigned. These require responsible institutional records if public retrieval remains insufficient.

Priority 2: retrieve the actual Cambridge People/organisation navigation and verify all current directors, committee members and support functions. Confirm whether Paul Warde's Director/Research Director wording reflects contemporary roles or historical change. Read the unresolved official college publications rather than promoting snippets.

Priority 3: Resolve Vincent Harmsen’s inaccessible profile, Thomas Lauvaux’s current external title, and the linked historical exchange-student profiles. No biography should be fabricated from a missing page. Recheck former-student cohort evidence and institutional labels before any public directory extract. Retain an individual review queue rather than treating missing profiles as absent researchers.

Priority 4: confirm Anna Egea's present agenda remit and the function responsible for CHEP communications, website approvals and maintaining role dates. The public site does not establish staff time allocation, a dedicated administrator, budget, or users' demand for a directory service.

The practical stop point was the processed navigation/body corpus plus documented inaccessible branches and profile queue. Further retries of the same blocked paths would not convert absence of access into evidence. The student can now take a bounded list of factual questions and usable draft files to the responsible institutional counterpart.
