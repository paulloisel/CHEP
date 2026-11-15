# P05 live inspection record

as_of_date and access date: **2026-11-15** (user's America/Los_Angeles date). Public read-only browser visits; no form filled or submitted, no message sent and no site changed. The temporary mobile viewport was reset before finishing.

## Evidence interpretation

`*-ax.txt` files preserve browser accessibility-tree observations with their URL and title. `list-en-dom.txt` records the embedded bilingual form after it loaded. These are research observations, not permanent web archives or full-page HTML backups. `host-en-alias-ax.txt` shows the final research route reached from the older content route. `keyboard-activation-ax.txt` duplicates the Events destination only to document the keyboard check; it is not an additional inventory page.

All JPGs are browser screenshots. They document this environment's rendering, not every user's device. Screenshot capture took place on the access date; the source pages do not necessarily disclose their own update date.

| Evidence ID | URL / local record | Observation | Limits |
|---|---|---|---|
| P05-V01 | [English home](https://www.histecon.fr/en/); [desktop screenshot](home-en-desktop.jpg) | Viewport 1280×720; document scroll width 1402px. Three-column content and wide header extend beyond viewport. | One page/browser; not a performance test. |
| P05-V02 | [English home](https://www.histecon.fr/en/); [390px screenshot](home-en-mobile-390.jpg) | Viewport 390×844; document scroll width remains 1402px. Banner, navigation and main columns clipped horizontally. | Real viewport override, not a physical-phone test. Other breakpoints not tested. |
| P05-V03 | [English home](https://www.histecon.fr/en/) | Read-only DOM: `lang=en`; three H4s (Events and Announcements, Welcome, Recent Centre Books); no H1–H3; logo alt present; banner alt empty; four book images have no alt attribute; canonical link absent in sampled DOM. | Empty alt may be correct for decoration. No formal conformance or search-ranking conclusion. |
| P05-V04 | [English index](https://histecon.fr/en/index.html); [focus screenshot](keyboard-events-focus.jpg); [destination](keyboard-activation-ax.txt) | First Tab on home reached FR. In a fresh home visit, ten Tabs reached CHEP Events; Return loaded Events. | One main-navigation path. Dropdown operation, full focus order, focus contrast and screen readers untested. |
| P05-V05 | [French home](https://histecon.fr/fr/index.html); [screenshot](home-fr-desktop.jpg); [full tree](home-fr-ax.txt) | Live 2027 call and November/December 2026 notices; four current featured books. Logo href points to English home. | Old indexed April 2024 notice is superseded for live-state claims. |
| P05-V06 | [Mailing list](https://histecon.fr/en/list.html); [screenshot](mailing-list-desktop.jpg); [DOM](list-en-dom.txt) | Embedded bilingual form loaded with name, email, confirmation email and affiliation fields and Submit control. | Screenshot captures upper portion; DOM records form. No submission, deliverability, privacy-policy or archive test. |
| P05-V07 | [Host old route](https://www.sciencespo.fr/histoire/en/content/centre-history-and-economics-paris-chep/); [final tree](host-en-alias-ax.txt) | Browser ended at current `/en/research/centre-for-history-and-economics-in-paris-chep/` route. French switch href leads to CHSP French homepage. | HTTP redirect status not inspected; no analytics or SEO impact measured. |

The homepage DOM observations were read directly during the browser session. The width measurements and image-alt values are transcribed here; screenshots and full accessibility trees provide complementary evidence rather than exposing those DOM measurements themselves.

## Observed live versus indexed discrepancies

- English `/en/index.html`: research tool returned 406; browser loaded the current page. Treat as retrieval limitation.
- French homepage: indexed representation showed April 2024; browser showed November/December 2026 notices matching English. Do not call it stale on the basis of the cache.
- Sciences Po old/new landing routes: indexed results supplied different community lists; live old route resolved to the new route with Jonathan Levy, Jessica Balguy and Joan Chaker. The cache discrepancy does not establish two conflicting live English pages.
- Both live CHEP organisation languages list Jonathan Levy as Coordinator/Coordinateur. No current coordinator-language conflict was observed there.

## Checks remaining for a technical owner

Responsive checks at 320/768/1280px across templates; browser/device diversity; 200%/400% zoom and reflow; full keyboard order and focus appearance; menu operation; skip links and landmarks; contrast; screen-reader reading order; image alternatives in context; accessible form errors and success; link destinations; HTML validity; performance; server redirects; canonical/hreflang policy; robots and sitemap; security and CMS configuration. None is presumed failed merely because it was not tested.
