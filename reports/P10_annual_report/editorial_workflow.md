# Proposed annual editorial workflow — P10

**Status:** internal proposal, not an adopted CHEP procedure. **as_of_date:** 2026-11-15. **Prototype period:** 2025-09-01–2026-08-31. All suggested roles are functions requiring agreement, not commitments by named individuals.

## Product and ownership

Produce one short, accessible annual web document, with an optional PDF derived from the same text. The eight-page-equivalent draft demonstrates the full editorial architecture; a six-page minimum edition combines the programme and support pages and shortens the reading list. Keep three 200–250-word research features and a junior-researcher section. Publication counts are descriptive, never a ranking of quality.

| Function | Proposed responsibility | Annual support estimate, separate from student hours |
|---|---|---|
| Academic editor, nominated by CHEP coordination | Set scope; check attribution and research summaries; decide unresolved queries; approve final institutional text | 4 hours |
| Student editor | Maintain records; request contributions after institutional authorisation; draft; reconcile; document corrections | See 40-hour first-cycle plan below |
| Research administration / grant administrator | Confirm affiliation periods, award cycle and any approved financial wording | 1 hour |
| French-language reviewer | Check French abstract, titles, names, and key navigation | 3 hours for a short French summary, not full translation |
| Web/accessibility owner | Publish approved accessible version and archive; check navigation and any PDF export | 2 hours |
| Individual contributors | Confirm their own summary and dated affiliation; identify a permissible link/illustration | About 10–15 minutes each; number of contributors not fixed |

This division follows the need to separate scholarly approval, data stewardship and website maintenance. The public organisation page lists a Coordinator, cross-centre coordination and a web architect, but does not assign annual-report duties: [CHEP Organisation](https://histecon.fr/en/organisation.html), accessed 2026-11-15, P10-S001. Named personnel should not be presumed available.

## Eight-question contribution form

One submission per work, activity or support record; estimated completion time 5–8 minutes. Do not request private student records, identity documents or unpublished full manuscripts.

1. **Who contributed?** Give the public name(s), contribution(s), professional profile link and career stage you wish to display; career-stage disclosure is optional.
2. **What is the item?** Supply its exact title, type (publication, dataset, event, project milestone, training, exchange or award), and a plain-English account of the research question and contribution in at most 100 words.
3. **When did it happen?** Give publication/online-first date, event date(s), exchange dates or award decision date; distinguish these from announcement date. If uncertain, write “date unknown”.
4. **What was the CHEP relationship at that time?** Give role and start/end dates, and choose centre-organised, co-organised, centre-supported, member achievement, or wider-network news. Specify what CHEP actually did; list other organisers/supporters separately.
5. **What public evidence verifies it?** Supply up to three direct links, DOI/ISBN if available, relevant page/section, and whether each source documents an announcement, a completed activity, an award or payment. For research summaries, link an abstract or accessible text.
6. **What may be published?** Confirm the supplied wording can be edited and published; identify any embargo. For images or quotations, give creator, rights holder, licence/permission and required credit. An image is optional and absence of permission means text only.
7. **What is still uncertain?** List dates, collaborators, figures or affiliations needing checking. For money, distinguish committed/awarded/paid, currency and award period; otherwise leave the amount unavailable. Do not send sensitive financial documents through this form.
8. **How can we verify the entry?** Give a professional institutional contact route for correction and confirm whether you can review the short edited entry by the proposed deadline. Contact information stays in the working register unless already a necessary public link.

## Calendar and capacity

Planning scenario: **5 student hours per week, no confirmed discretionary budget**. These are estimates for a focused edition, not actual staffing or cost information. Initial setup is 8 student hours; the repeatable annual cycle is 32 hours; first-cycle total is **40 hours**. Academic, administrative, translation and web support above are additional institutional inputs.

| Timing | Work | Student hours | Exit condition |
|---|---|---:|---|
| First cycle, two setup weeks | Agree scope and definitions (2); configure registers and form (3); prepare text template and archive convention (3) | 8 one-off | Academic editor accepts scope and missing-data rules |
| During each reporting year | Half-hour monthly capture of new source-backed items; record post-event evidence when supplied | 6 recurring annually | New records retain stable IDs and dates |
| Production week 1, after 31 August | Freeze period; deduplicate; issue one authorised contribution request and one reminder schedule | 4 | Item queue and eligibility decisions visible |
| Production week 2 | Check dates/affiliations and abstracts; select themes and junior contributions | 4 | All selected facts traced to evidence |
| Production week 3 | Draft features and overview; build indicators from registers | 4 | First full text and count reconciliation |
| Production week 4 | Contributor and academic fact check; resolve or remove unsupported claims | 4 | Query log decided, not silently erased |
| Production week 5 | Short French summary and reviewer handoff; accessibility and rights checks | 4 | Text-only fallback ready if rights unresolved |
| Production week 6 | Final corrections; approval package and web-owner handoff | 4 | Approved version or explicitly deferred release |
| After approval | Archive tables, rendered output if used, source dates and change log | 2 | Reproducible frozen edition |
| **Annual recurring total** | 6 capture + 24 production + 2 archive | **32** | |

For this retrospective prototype, the six capture hours can instead be spent recovering period records over two additional weeks. Spread the first cycle over ten weeks: two setup weeks at four hours, two recovery weeks at three hours, six production weeks at four hours. Use one spare hour in production week 5 to prepare the archive and one in week 6 to freeze the approved package; if approval is delayed, move that final hour to the release week. No week need exceed five hours. This is a bounded editorial service; it does not fit alongside five hours of other weekly commitments without reprioritisation.

With existing institutional hosting, software and support, proposed additional cash outlay is **€0** for a text-only digital edition. This is not a claim that labour, hosting or translation are free. Printing, design procurement and paid image licensing are outside the baseline. A fully translated second language edition is estimated to add 10–16 student/translator hours plus 3–4 reviewer hours and would require a revised schedule or separately agreed funding; no market quotation has been obtained. If support or time is unavailable, use the six-page format and defer a PDF and full translation.

## Updating the underlying data

1. **Add evidence first.** Append a source ID to `sources.csv`, preserving source date, access date, title, owner and retrieval mode. Search snippets are discovery leads; failed opens remain failed. Store brief factual extraction notes, not copies of copyrighted works.
2. **Add the record.** Reuse the work, person, event or support ID in the supporting inventories. Never turn a new web announcement into a second event. DOI identifies an underlying article; book translations and editions link to their original work. A multi-day conference is one event, while independently dated seminar sessions count separately.
3. **Set attribution and period.** A dated affiliation or explicit acknowledgement is required for the corresponding claim. A current roster is not evidence of last year's membership. Record years without exact dates as unresolved when the September boundary matters.
4. **Update `content_register.csv`.** Link every selected section to its evidence, rights status and unresolved question. Keep `fact_check_status` in the shared vocabulary: verified, inferred, conflicting or unverified. “Verified” does not mean institutional approval to publish.
5. **Recalculate `indicator_register.csv`.** Freeze the eligible record IDs and denominator. Distinguish all scheduled records from the subset with retrospective held evidence. Leave attendance, cash expenditure, readership and unknown publication totals as `not_found_publicly`; do not display zero or calculate rates from unknown denominators.
6. **Check research copy.** Write arguments only from inspected abstracts or texts. Metadata-only items receive notices. Ask authors to confirm work-in-progress version and precise findings; do not fabricate interviews or infer results from titles.
7. **Check accessibility and rights.** Use sequential headings, meaningful links, UTF-8 accents, readable tables with headers, sufficient contrast if designed, language tags and alt text for authorised images. Do not reproduce covers, photographs or quotations without a recorded licence or permission. If exporting PDF later, check reading order, tagging, searchable text and every rendered page; no PDF is produced in this P10 run.
8. **Release and preserve.** Publication requires the nominated institutional editor's approval and an authorised web owner. Keep an immutable `CHEP_annual_report_2025-2026_v1.0` package with Markdown, CSV, approved render if any, scope statement and version history. Corrections become v1.1 with date and reason; do not overwrite the evidence state silently. Roll forward blank registers, not last year's totals.

## Decision and learning checks

Before adoption, agree which function owns the membership denominator and whether a public annual report already exists internally. After the pilot, record editing hours, unresolved claims removed, corrections requested and whether readers can identify a research connection or useful resource. Use voluntary brief feedback; do not invent readership or collect intrusive individual tracking. Continue only if an academic reviewer and archive owner are available and the recurring 32-hour estimate is credible after one cycle. Otherwise retain the verified bibliography and junior-research digest as a smaller annual product.
