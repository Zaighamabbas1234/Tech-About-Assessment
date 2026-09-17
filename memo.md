# Is TECHi traffic actually up? — Memo

## (a) Is "up 30% YoY" true?
No. The traffic file has no clean 12-month pair (it runs Jul 2025 -> Jun
2026, not Jun 2025 -> Jun 2026), but on the 11 months it does have, total
sessions **fell 49%** (90,000 -> 45,800), not up 30%. There is no reading
of this file that produces +30%.

## (b) Best estimate of the underlying change
Roughly **flat**, not down 49% and not up 30%. Two adjustments matter:
1. **Nov 2025 Crypto** (46,000 vs. a 16,250 Oct/Dec baseline) matches the
   noted 36-hour aggregator front-page hit — a one-off, removed from the
   trend.
2. The **1 Feb 2026 analytics-snippet swap** lines up with a simultaneous,
   uniform ~40-46% drop across *all six* sections in the same month
   (spike-adjusted pre-break average 95,850/mo -> post-break 51,480/mo,
   -46%). Six independent sections don't collapse by the same percentage
   in the same month by coincidence — that is a measurement break, not six
   demand collapses. **Newsletter signups**, collected outside that
   snippet, climbed a steady 10-20/month straight through Feb 2026 with no
   dip — the one metric that survived the swap shows no real collapse.
   Pre-break, spike-adjusted, sessions were themselves roughly flat-to-up
   (~+13% Jul25->Jan26). Best call: underlying traffic is **flat**, and the
   true post-Feb level is unmeasurable from sessions alone until the
   snippet is fixed.

## (c) Retire Guides?
**Not yet.** Guides sessions fell 94% (25,800 -> 1,500) and, unlike every
other section, kept falling every month *after* the Feb break too — not a
one-time step. That looks Guides-specific. But the stated justification —
"Guides has published almost nothing since Mar 2026" — is **false**: see
Finding 2 below. Guides pages lean on calculators/tools, which may not
fire the new snippet the way article pages do; that would produce exactly
this pattern. Audit Guides tracking first; retire only if a clean
re-measurement still shows near-zero sessions.

## Two findings from the rows, with numbers
1. **Cross-listing inflates the site's own article counts.** 14 of the
   120 sampled urls (11.7%) appear on two category pages at once. The six
   category pages report 3,038 stories combined (472+1,637+119+425+270+115),
   but with double-digit cross-listing that's consistent with something
   close to the "~2,000 articles" the brief cites for the underlying
   unique count.
2. **Guides did not go quiet.** 17 of the 20 newest Guides articles (85%)
   are dated on/after 2026-04-01, most recently 2026-08-09 — steady
   output through the summer, directly contradicting the "almost nothing
   since Mar 2026" note.

## Where Part 1 and the table meet
The article-level scrape is what falsifies the Guides publishing note
(finding 2) and is the reason the Guides recommendation in (c) is "audit
first," not "retire" — the traffic table alone would have supported
retiring; the scraped rows say the premise for that call is wrong.

## Recommendation and cost if wrong
Hold the "traffic is up 30%" claim as false, report underlying traffic as
flat, and spend a half-day auditing Guides-page tracking before any
retire decision. **Cost if this recommendation is wrong:** if Guides
really is dead and we delay retiring it by a few weeks for an audit, the
cost is near-zero — ads on Guides already pay near-zero per session. If we
instead retired Guides now on bad data and the tracking gap turns out to
be the whole story, we would cut a section that publishes weekly, lose
whatever newsletter-funnel value it has (unmeasured here), and that
decision is expensive to reverse (writers reassigned, content de-indexed).
The asymmetry favors checking before cutting.

## I would change my mind if...
...the Guides tracking audit shows the new snippet fires correctly on
Guides/tool pages and sessions are still near-zero — then the decline is
real and Guides-specific, and retiring it is the right call.

## The next number I want, free to get
Guides sessions **segmented by page template** (calculator/tool pages vs.
plain article pages) for Feb-Jun 2026, pulled straight from the analytics
tool already in use — no new tracking, no cost, and it directly tests the
snippet-coverage hypothesis in (c).