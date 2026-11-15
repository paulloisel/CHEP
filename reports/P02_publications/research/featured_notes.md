# Featured-publication verification batch

As of 2026-11-15. This is a research intermediate for P02 only. All source IDs, direct URLs, source titles, owners, source dates, access dates, and retrieval statuses are in the `sources` array of [featured.json](featured.json). Publication dates are distinguished from retrieval/crawl dates. The web tool mostly returned indexed representations; none is a dated archival snapshot or proof of live-page condition.

## Counts and counting decisions

Both [English](https://histecon.fr/en/publications.html) and [French](https://histecon.fr/fr/publications.html) publication pages contain **18 edition entries**, with the same titles and authors. The initial estimate of 17 was corrected by enumeration. They represent **14 underlying works**, **15 distinct named authors/editors**, and **18 catalogue records**. Of the edition records, 15 are monographs, one a short monograph/Cambridge Element, one an edited volume, and one a methods book. At work level the corresponding counts are 11, 1, 1, and 1. These are counts of the centre's curated display, not all CHEP scholarship or 18 separate research projects. Sources P02-SF001–002.

Four internal pairs share work IDs:

- Rothschild: *An Infinite History* (2021) and *De proche en proche* (2025). The companion site links both; an opened bibliographic review explicitly identifies the translation. P02-SF013, SF023–025.
- Trivellato: *The Promise and Peril of Credit* (2019) and *Juifs et capitalisme* (2023). The author's June 2025 CV, p.3, explicitly identifies the translation. P02-SF022, SF026.
- Delalande: *La Lutte et l’Entraide* (2019) and *Struggle and Mutual Aid* (2023). Sciences Po's publication inventory explicitly identifies the English version. P02-SF010, SF019, SF030.
- Todd: *A Velvet Empire* (2021) and *Un empire de velours* (2022). Sciences Po and the French publisher verify the relation. P02-SF011, SF015, SF030.

Three other displayed editions have earlier originals outside the 18-tile list: Oualdi's 2023 French edition follows *A Slave Between Empires* (Columbia, 2020); Lemercier/Zalc's 2019 English edition translates and revises their 2008 French original; Rosental's 2018 book translates and updates *L’intelligence démographique* (2003). The latter two links are explicit in the authors' companion site and Sciences Po profile. Oualdi's link is explicit in the BnF indexed record, but direct BnF access failed: the French book's title/year are verified by Sciences Po, while its linkage is conservatively labelled inferred pending direct catalogue/copyright-page confirmation. P02-SF027–029, SF031–032.

Publication formats are not multiplied: *Sociologie historique du capitalisme* uses the EPUB identifier actually linked by CHEP; *A World of Public Debts* uses its linked hardcover date (27 October 2020), noting the eBook appeared one day earlier; *Unruly Waters* uses the recovered 2018 eBook record rather than silently dating the work to its 2020 paperback. Princeton pages sometimes repeat the selected format's ISBN under several format tabs, so no format-specific data were inferred from these repeated widgets.

## Content read and possible atlas connections

These are proposed analytic connections, not evidence of collaboration, influence, or endorsement. Except for Rosental's publisher-hosted introduction and Delalande's institutional author interview, the substantive reading was publisher descriptions, abstracts, contents, or author companion material. No claim rests on having read all these books.

1. **Defining and governing capitalism.** Levy's publisher overview returns to historical debates about the economy, uncertainty, money, and corporations. François/Lemercier's contents organize changes through commerce, factories, finance, labour and state institutions. A useful shared question is how historians select economic categories and periods. P02-SF005, SF014.
2. **Credit, sovereignty, and exclusion.** Barreyre/Delalande's volume presents public borrowing as part of political institution building; Trivellato studies a false attribution of financial invention to Jews and the boundaries of legitimate credit. A joint reading can compare public authority with cultural boundary-making without equating their arguments. P02-SF016, SF022.
3. **Empire, property, and law.** Todd's descriptions connect informal imperial power with finance, luxury, and extraterritorial law. Oualdi's original publisher description follows Husayn's estate and the competing claims surrounding it. Yates's abstract treats real estate as a form of possession/dispossession linking local sites to wider institutions. P02-SF011–012, SF015, SF028.
4. **Solidarity and collective economic action.** Delalande's interview asks how international solidarities were financed, organized and sustained through local ties. François/Lemercier's contents offer a connection through labour regimes and class conflict; this is an editorial pairing, not an asserted common theory. P02-SF014, SF034.
5. **Everyday lives and disciplinary institutions.** Génard's author announcement describes prison registers, correspondence and work hierarchies; Le Bras's publisher account follows confined patients and their relationships outside asylums. These support a focused conversation about tracing lives through institutional records. P02-SF004, SF007.
6. **Population, networks, and historical methods.** Rothschild's companion site displays family and social-network research; Lemercier/Zalc explain accessible quantitative tools; Rosental's introduction examines how demographic science and policy developed together. This connects the use of categories with their history, without reducing all three projects to one method. P02-SF024, SF020, SF032–033.
7. **Environment and development.** Amrith's publisher description connects water control, political independence and development in South Asia. Yates supplies a possible comparison about built environments and institutions, although the environmental cluster is thin within the featured-book corpus and should be strengthened through the independently researched Paris cohort. P02-SF021, SF012.

## Source tree and retrieval findings

```text
CHEP publications EN + FR [both retrieved/indexed; same 18 items]
├── EHESS / Sous les verrous [502]
│   └── Author announcement via H2C [retrieved; synopsis + contents]
├── Princeton / Real Economy; Velvet Empire [retrieved]
├── Princeton / Infinite History [indexed full catalogue; direct timeouts]
│   ├── Harvard publication list [retrieved; corroborates 2021]
│   └── Author companion EN + FR [retrieved]
├── CNRS / Aliénés [retrieved]
├── Seuil / four French titles [403 on all four]
│   ├── Rothschild: Harvard + companion + bibliographic review [retrieved]
│   ├── Trivellato: IAS author CV [retrieved PDF; p.3 inspected]
│   ├── Oualdi: Sciences Po announcement + Columbia original [retrieved]
│   │   └── BnF translation entry [indexed record; direct cache miss]
│   └── Delalande: BNFA + Sciences Po interview [retrieved]
├── Other Press / Struggle and Mutual Aid [retrieved]
├── La Découverte / Un empire de velours [retrieved]
├── Cambridge / Yates Element [retrieved abstract and metadata]
├── Collection Repères / Sociologie historique [502]
│   └── La Découverte canonical same-ISBN page [retrieved]
├── Palgrave old / Public Debts [cache miss]
│   └── Springer DOI page [retrieved]
├── UVA / Quantitative Methods [original slashless route cache miss]
│   └── Canonical trailing-slash page + author About/Languages [retrieved]
│       └── Author homepage/The Book category [Anubis challenge]
├── Peter Lang old / Population [cache miss]
│   └── Modern document route + Sciences Po author profile [retrieved]
├── Penguin old author route [cache miss]
│   └── Modern Unruly Waters edition route [retrieved]
└── Princeton old title route / Credit [cache miss]
    └── Modern ebook route [retrieved historical metadata; 2-year crawl age]
```

No pagination or publication archive link was present in the inspected EN/FR publication-page navigation. This batch did not infer an exhaustive historic archive from that absence. Parent research handles broader site mapping and author career expansion. The wider Harvard publication list was used only to corroborate already Paris-featured works, not to import additional Harvard outputs.

## Remaining checks for merged deliverables

- Replace temporary `person_ids` (names) and generic `featured participant publication` relationship with the parent's roster IDs and dated Paris evidence. No featured book here establishes CHEP funding. None has been labelled explicitly supported by CHEP.
- Retain the metadata notes in a supplementary ledger or the methods note when exporting the required CSV schema. Missing exact days are intentional; access dates are not publication dates.
- Recover the EHESS publisher/copyright page for Génard's identifier and exact date. HAL search returned DOI `10.4000/14x0b`, but opening the DOI failed and the opened HAL representation differed from its indexed search text; therefore the identifier was not promoted into this batch's record.
- Recheck Seuil metadata, Oualdi's translation evidence, and older Princeton cached content before a public-facing catalogue release. Recovery failures describe this research tool, not a finding that public links are universally broken.
- The CNRS Aliénés page's bibliographic metadata gives 4 January 2024, but one embedded review is labelled January 2023. Follow the dedicated publication field; do not treat a review-date typo as a second edition.
- No cover images or copyrighted text were downloaded or proposed for reuse. Publisher previews are not equivalent to open access books. `open_access_url=not_found_publicly` means this batch did not verify a lawful full-book open-access URL, not that none exists.

The JSON source register has 34 supporting or failed-target records. Failed auxiliary search leads that did not inform the catalogue are not treated as evidence.
