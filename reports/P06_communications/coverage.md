# P06 coverage and research decisions

**as_of_date / accessed_at: 2026-11-15** (user's America/Los_Angeles date). Only P06 was executed. `Summary.md` was read: it supplied the Sciences Po, Paris, Harvard and Cambridge starting URLs, with no additional task text. No other report was required or used. All outputs are confined to `reports/P06_communications/`.

## Corpus and counts

This is a focused communications audit and editorial prototype, not a people, publication, event or funding census. Include Paris-owned entry points; the host centre's communications and explicitly CHEP-supported programme; shared-network channels; two publisher descriptions for featured books; one dated junior-researcher announcement; and three substantive newsletter comparators. Dates of usable content range from the 2021 historical comparator to announced 2026–27 activity. Older material is clearly labelled.

The source register contains **53 URL records: 38 with some retrieved content and 15 with failed retrieval**. “Retrieved” includes limited profiles, dynamic shells and older indexed representations; it does not mean the live page was fully tested. Alias URLs remain separate retrieval records but do not count as separate organisations, channels or achievements. The channel audit has **17 rows**, including language versions and host/network routes. There are **three proposed issues**, **seven content records** (six selected for the pilot, one reserve), and **three core inspected comparator issues**. An additional Cambridge AHSS bulletin was inspected during discovery but is outside the core comparison.

No population-completeness percentage is supplied: the number of internal mailings, all public historical issues and dynamically accessible posts is unknown. Audience counts, readership, demand, costs already borne by institutions and staff capacity are **not_found_publicly**, never zero.

## Task-specific source tree

Legend: **R** = content retrieved; **P** = partial/shell/profile; **F** = retrieval failed. IDs resolve to direct URL, title, owner, access date and retrieval details in [sources.csv](sources.csv). A failure describes this research tool's result, not a diagnosed broken website.

- **Paris CHEP**
  - **R** [English home](https://www.histecon.fr/en/) — S001; **R, old indexed copy** [French home](https://histecon.fr/fr/index.html) — S002.
  - **F** [Summary.md English index route](https://histecon.fr/en/index.html) — S043; readable home alias used instead.
  - **R** [People navigation](https://histecon.fr/en/people.html) — S020 → **R** [Organisation](https://histecon.fr/en/organisation.html) — S003. Category links mapped; no exhaustive roster extraction required for P06.
  - **R** [Publications](https://histecon.fr/en/publications.html) — S025 → **R** [Princeton book page](https://press.princeton.edu/books/hardcover/9780691252551/the-real-economy) — S026; **R** [CNRS book page](https://www.cnrseditions.fr/catalogue/histoire/alienes/) — S027.
  - **F** [Projects](https://histecon.fr/en/projects.html), [Seminars](https://histecon.fr/en/seminars.html), [Conferences/workshops](https://histecon.fr/en/events_sub.html) — S047–S049. Relevant readable host programme used below.
  - **R** [Grant call](https://histecon.fr/en/research_grants.html) — S021 → **F** [application portal](https://histecon.fr/fr/bourses_portail.html) — S022. Terms inspected, functionality unverified.
  - **R** [Announcements](https://histecon.fr/en/announcements_archive.html) — S009 and **R** [French archive](https://histecon.fr/fr/archive_annonces.html) — S010. No newsletter issue sequence located. **F** [www archive alias](https://www.histecon.fr/en/announcements_archive.html) — S045.
  - **F** [English list](https://histecon.fr/en/list.html), [www list](https://www.histecon.fr/en/list.html), [French list](https://histecon.fr/fr/liste.html) — S004–S005/S044. Subscription purpose supported by home-page link text; public issue archive remains not_found_publicly.
  - **R** [Contact](https://histecon.fr/en/contacts.html) — S011; **F** [www alias](https://www.histecon.fr/en/contacts.html) — S046 → **P** [joint Bluesky profile](https://bsky.app/profile/historyecon.bsky.social) — S012.
  - **F** [robots.txt](https://histecon.fr/robots.txt) and [sitemap.xml](https://histecon.fr/sitemap.xml) — S041–S042. No automated bulk crawl undertaken. A limited local fetch also failed DNS; ordinary targeted web retrieval was used.
- **Sciences Po host**
  - **R** [English CHEP overview](https://www.sciencespo.fr/histoire/en/research/centre-for-history-and-economics-in-paris-chep/) — S006; **R** [alternate English route](https://www.sciencespo.fr/histoire/en/content/centre-history-and-economics-paris-chep/) — S007; **R** [French overview](https://www.sciencespo.fr/histoire/fr/recherche/centre-for-history-and-economics-paris-chep/) — S008.
  - Newsletter link → **F** [Google form](https://docs.google.com/forms/d/e/1FAIpQLSdBbKPJtbb95NbTjmSICnMoNA-xuko2YdrK--az3-5mHGnS3Q/viewform) — S018; no form interaction or address collection.
  - **R** [CHSP guide 2025–26](https://www.sciencespo.fr/histoire/files/Guidedoctorant2025-2026-15sept.pdf) — S019, printed pp. 8–9 inspected. PDF screenshot attempt failed; findings concern text, not visual layout.
  - **R** [News index](https://www.sciencespo.fr/histoire/en/news/) — S013, first page with 2025–26 items and older pagination observed. Older pages not traversed: the current content sample does not require a historical news census.
  - **P** [Events index](https://www.sciencespo.fr/histoire/en/events/) — S014, filters and three-page navigation visible but event cards not retrieved.
  - **R** [Economic-life seminar programme](https://www.sciencespo.fr/histoire/fr/recherche/seminaires/seminaire-des-axes-et-des-domaines/histoires-de-la-vie-economique/) — S023, 2026–27 selected; earlier 2022–26 sections observed; “Informations pratiques” explicitly credits CHEP support → **R** [17 November event detail](https://www.sciencespo.fr/histoire/fr/evenements/le-retour-des-inegalites-bilan-et-perspectives-historiographiques/) — S024. Embedded registration destination was not resolved.
  - **R** [CHSP seminar](https://www.sciencespo.fr/histoire/fr/recherche/seminaires/seminaire-du-centre-d-histoire/) — S050; restricted-members/visitors candidate excluded from broad participation call.
  - **R** [2026 awards, French](https://www.sciencespo.fr/ecole-recherche/fr/actualites/quatre-jeunes-chercheurs-histoire-laureats-bourse-chep-2026/) and [English](https://www.sciencespo.fr/ecole-recherche/en/news/four-young-history-researchers-chep-2026-grant/) — S029/S051, deduplicated as one announcement.
  - **R** [Visitors](https://www.sciencespo.fr/histoire/fr/le-centre/chercheurs/chercheurs-invites/) — S028, reserve candidate only; no invented finished project.
  - **R** [French host home](https://www.sciencespo.fr/histoire/fr/) — S015 → **P** [host Bluesky](https://bsky.app/profile/chsp-sciencespo.bsky.social) — S016; **P** [host LinkedIn](https://www.linkedin.com/showcase/centre-d-histoire-de-sciences-po/) — S017. No login, post-history census or follower metric adopted.
- **Partner centres**
  - **R** [Harvard home](https://histecon.fas.harvard.edu/), [news](https://histecon.fas.harvard.edu/news.html), [contact](https://histecon.fas.harvard.edu/contact.htm) — S031–S033; shared-network scope preserved.
  - **R** [Times of Drought](https://histecon.fas.harvard.edu/climate-loss/po/index.html) — S030, October 2022 full essay; directly linked in Paris archive. Optional evergreen reserve; broader thematic programme not inventoried.
  - **F** [Cambridge home](https://www.histecon.magd.cam.ac.uk/) and [historical Paris project](https://www.histecon.magd.cam.ac.uk/chep/) — S034–S035. HTTP home alias also returned 403; non-www HTTPS returned 502. Partner channels remain partially unverified.
- **Newsletter comparisons**
  - **R** [CHSP September 2021 issue](https://www.sciencespo.fr/histoire/sites/sciencespo.fr.histoire/files/Newsletter%20du%20CHSP%20-%20Septembre%202021.pdf) — S036, text of 12-page PDF; screenshot failed.
  - **R** [LSE Autumn 2025–26 issue](https://www.lse.ac.uk/asset-library/2526-at1.pdf) — S037, text of 13-page PDF and one successful page image; **R, older indexed copy** [termly archive](https://www.lse.ac.uk/Economic-History/AlumniNewsletter/Termly-Newsletter) — S038.
  - **R** [UCL Summer 2026 HTML issue](https://www.ucl.ac.uk/social-historical-sciences/history/alumni/ucl-history-summer-newsletter-2026) — S039.
  - Supplementary discovery: **R** [CEE follow-us archive](https://www.sciencespo.fr/centre-etudes-europeennes/en/media/follow-us/) — S040, linked July issue unavailable; **R** [IHR Bulletin subscription page](https://www.history.ac.uk/about-us/subscribe-ihr-bulletin) — S052, linked archive unavailable; **R** [Cambridge AHSS bulletin](https://www.ahssresearch.group.cam.ac.uk/ahss-research-and-impact-bulletin) — S053. Not included among core three comparator issues or as CHEP funding opportunities.

## Search and reconciliation decisions

Targeted searches included `site:histecon.fr newsletter "list"`, `site:histecon.fr "newsletter" archive`, and `site:sciencespo.fr/histoire CHEP newsletter`, with focused searches for seminars and actual comparator issues. Search results supplied leads; claims use opened institutional/publisher sources. No archive snapshot date was available: indexed crawl-age notices are not dated Wayback captures.

| Issue | Treatment and consequence |
|---|---|
| Current title versus old search results | Opened Paris organisation and both host-language overviews name Jonathan Levy as coordinator. Older search renderings name David Todd. Use the inspected wording, retain the mismatch, and do not infer appointment start dates. |
| English/French CHEP home content differs | Different crawl ages confound a live-site comparison. State only what the retrieved copies show; request a live editorial parity check. |
| CHSP newsletter cadence | September 2021 issue footer says second Thursday monthly; the opened 2025–26 guide gives no day. Current cadence therefore remains unknown. Do not turn a historical schedule into a present commitment. |
| Host English aliases | Same substantive content returned, counted once for institutional evidence. Redirect implementation not established. |
| Publications and roles | Publisher description supports summary; Paris publication selection supports association. A publisher's historical postdoc bio does not override newer appointment information. Neither implies CHEP funding. |
| Future event status | Dates are verified announcements, not proof the event will occur. Paris timezone is an inference from venue. Check access and live status before release. |
| Funding status | Official call inspected; portal retrieval failed. Describe announced terms without claiming successful application-system testing. |
| Anniversaries | 2019 collaboration and 2022 establishment are distinct documented milestones. No anniversary promotion is included. |

## Boundaries, remaining queue and internal questions

Completed the relevant entry-point map, pilot candidate checks, three core comparisons and workload design. Practical limits: web retrieval returns some cached representations, dynamic forms/calendars are incomplete, and Cambridge is inaccessible. Stop here rather than filling gaps with assumed newsletter history. Broader people branches, all publications, grant opportunities elsewhere, all past events and other prompts' inventories are out of scope.

Before circulation, the **communications/list-administration function** should establish whether there is already a CHEP digest, its frequency, list purpose, audience expectations, internal archive, available metrics and sender/preference controls. These cannot be answered from public sources. The **academic reviewer** should validate selected content and attribution; the **bilingual reviewer** should check language parity; the **web editor** should confirm an archive route and whether the subscription pages are accessible to ordinary users. Proposed owners are functions, not commitments.

Next retrieval steps, in order: (1) check the mailing-list pages and Google form read-only in an ordinary browser and identify any public archive; (2) recheck current event/call details, embedded registration and portal at actual launch; (3) obtain the latest host newsletter and confirm duplication/cadence with its responsible function if authorised later; (4) retry Cambridge's official site without bypassing restrictions; (5) only then decide whether a separate digest, a host-newsletter block or improved event alerts add value.

No messages, invitations, subscriptions, applications, social posts, website changes or mailing-list exports were made. The findings and drafts remain reviewable proposals.
