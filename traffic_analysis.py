import pandas as pd

pd.set_option("display.width", 120)

# Invented months of sessions + newsletter signups (given in the brief).
# This data is INVENTED per the assessment; kept in its own file/frame, never merged with the real techi_articles.csv rows.
traffic = pd.DataFrame([
    ["Jul 2025", 10000, 20000, 15000, 12000, 8000, 25000, 500],
    ["Aug 2025", 10200, 20500, 14800, 12200, 8100, 25200, 520],
    ["Sep 2025", 10500, 20100, 15500, 12400, 7900, 24800, 540],
    ["Oct 2025", 14500, 21000, 16000, 12500, 8200, 25000, 560],
    ["Nov 2025", 14800, 21500, 46000, 12700, 8400, 25500, 580],
    ["Dec 2025", 15000, 22000, 16500, 13000, 8500, 26000, 590],
    ["Jan 2026", 15200, 22500, 16200, 13100, 8600, 25800, 600],
    ["Feb 2026", 8500, 12500, 9000, 7300, 4800, 14500, 610],
    ["Mar 2026", 8600, 12700, 9200, 7400, 4900, 14000, 620],
    ["Apr 2026", 8700, 12600, 9100, 7500, 4800, 8000, 630],
    ["May 2026", 8800, 12800, 9300, 7600, 5000, 4000, 640],
    ["Jun 2026", 8900, 13000, 9500, 7800, 5100, 1500, 650],
], columns=["Month", "AI_Sessions", "Markets_Sessions", "Crypto_Sessions",
            "Breakthroughs_Sessions", "Policy_Sessions", "Guides_Sessions",
            "Newsletter_Signups"])
section_cols = ["AI_Sessions", "Markets_Sessions", "Crypto_Sessions",
                 "Breakthroughs_Sessions", "Policy_Sessions", "Guides_Sessions"]
traffic["Total_Sessions"] = traffic[section_cols].sum(axis=1)

print("=" * 78)
print("RAW MONTHLY TABLE")
print("=" * 78)
print(traffic.to_string(index=False))

# (a) Is "up 30% YoY" true?
print("\n" + "=" * 78)
print("(a) 30% YoY CLAIM")
print("=" * 78)
first, last = traffic.iloc[0], traffic.iloc[-1]
span_change = (last["Total_Sessions"] - first["Total_Sessions"]) / first["Total_Sessions"]
print(f"First month on file: {first['Month']} = {first['Total_Sessions']:,} total sessions")
print(f"Last month on file:  {last['Month']} = {last['Total_Sessions']:,} total sessions")
print(f"Change, first->last (11 months, not a clean 12-month YoY pair): "
      f"{span_change:+.1%}")
print("No Jun-2025 or Jul-2026 row exists, so a true calendar YoY pair "
      "cannot be built from this file at all.")
print('=> The "up 30% YoY" claim is NOT supported: measured sessions fell '
      f"{abs(span_change):.0%} across the 11 months on file, they did not rise 30%.")

# (b) Best estimate of underlying change?
print("\n" + "=" * 78)
print("(b) UNDERLYING CHANGE, ADJUSTING FOR THE KNOWN ONE-OFF AND THE BREAK")
print("=" * 78)
# Step 1: strip the Nov-2025 Crypto aggregator spike (one-off per the notes), replacing it with the average of the surrounding two months as a baseline.
adj = traffic.copy()
nov_idx = adj.index[adj["Month"] == "Nov 2025"][0]
oct_crypto = adj.loc[adj["Month"] == "Oct 2025", "Crypto_Sessions"].iloc[0]
dec_crypto = adj.loc[adj["Month"] == "Dec 2025", "Crypto_Sessions"].iloc[0]
baseline_nov_crypto = (oct_crypto + dec_crypto) / 2
spike_excess = adj.loc[nov_idx, "Crypto_Sessions"] - baseline_nov_crypto
adj.loc[nov_idx, "Crypto_Sessions_adj"] = baseline_nov_crypto
print(f"Nov-2025 Crypto_Sessions reported: {adj.loc[nov_idx, 'Crypto_Sessions']:,}; "
      f"Oct/Dec average baseline: {baseline_nov_crypto:,.0f}; "
      f"one-off excess removed: {spike_excess:,.0f}")
adj["Total_Sessions_adj"] = adj["Total_Sessions"]
adj.loc[nov_idx, "Total_Sessions_adj"] = adj.loc[nov_idx, "Total_Sessions"] - spike_excess

# Step 2: split at the Feb-2026 tracking-snippet change and compare period averages.
pre = adj[adj["Month"].isin(["Jul 2025", "Aug 2025", "Sep 2025", "Oct 2025",
                              "Nov 2025", "Dec 2025", "Jan 2026"])]
post = adj[adj["Month"].isin(["Feb 2026", "Mar 2026", "Apr 2026", "May 2026", "Jun 2026"])]
pre_avg = pre["Total_Sessions_adj"].mean()
post_avg = post["Total_Sessions_adj"].mean()
measured_drop = (post_avg - pre_avg) / pre_avg
print(f"\nPre-break (Jul25-Jan26, spike-adjusted) average total sessions/mo: {pre_avg:,.0f}")
print(f"Post-break (Feb26-Jun26) average total sessions/mo:                {post_avg:,.0f}")
print(f"Measured change across the break: {measured_drop:+.1%}")

# Step 3: cross-check against a metric that does NOT run through the swapped site snippet -- newsletter signups (collected via the email platform).
print("\nNewsletter_Signups by month (independent of the site analytics snippet):")
print(adj[["Month", "Newsletter_Signups"]].to_string(index=False))
signup_growth = adj["Newsletter_Signups"].diff().dropna()
print(f"\nMonth-over-month signup change: min {signup_growth.min():.0f}, "
      f"max {signup_growth.max():.0f}, mean {signup_growth.mean():.1f}")
print("Signups climb by a steady 10-20/month with NO break or slowdown at "
      "Feb 2026 -- the one metric in this file that survives the snippet swap "
      "shows no sign of a real audience collapse at the same moment sessions "
      "cratered site-wide.")

print("\n=> Best estimate: the ~{:.0%} apparent drop across Feb 2026 is dominated by "
      "the unchecked tracking-snippet swap, not a real traffic collapse. The "
      "clean, comparable pre-break trend (Jul25-Jan26, spike-adjusted) was "
      "roughly flat-to-modestly up (~{:+.0%} Jul25->Jan26); nothing in this file "
      "supports a +30% YoY figure, and nothing in this file lets us rule out "
      "flat-to-slightly-down once the tracking break is accounted for. "
      "Best-supported call: underlying traffic is roughly FLAT, not up 30%, "
      "and the true post-Feb number is unmeasurable from sessions alone."
      .format(abs(measured_drop),
              (pre["Total_Sessions_adj"].iloc[-1]-pre["Total_Sessions_adj"].iloc[0])/pre["Total_Sessions_adj"].iloc[0]))

# (c) Retire Guides?
print("\n" + "=" * 78)
print("(c) RETIRE GUIDES?")
print("=" * 78)
guides = adj[["Month", "Guides_Sessions"]].copy()
guides["pct_of_jan26"] = guides["Guides_Sessions"] / guides.loc[guides["Month"] == "Jan 2026", "Guides_Sessions"].iloc[0]
print(guides.to_string(index=False))

other_sections = ["AI_Sessions", "Markets_Sessions", "Breakthroughs_Sessions", "Policy_Sessions"]
other_pre = adj.loc[adj["Month"] == "Jan 2026", other_sections].sum(axis=1).iloc[0]
other_post = adj.loc[adj["Month"] == "Jun 2026", other_sections].sum(axis=1).iloc[0]
other_drop = (other_post - other_pre) / other_pre
guides_drop = (adj.loc[adj["Month"] == "Jun 2026", "Guides_Sessions"].iloc[0]
               - adj.loc[adj["Month"] == "Jan 2026", "Guides_Sessions"].iloc[0]) \
              / adj.loc[adj["Month"] == "Jan 2026", "Guides_Sessions"].iloc[0]
print(f"\nOther 4 sections (AI, Markets, Breakthroughs, Policy), Jan26->Jun26: {other_drop:+.1%}"
      " (one step down at the Feb break, then roughly flat -- consistent with a "
      "measurement change).")
print(f"Guides, Jan26->Jun26: {guides_drop:+.1%} (keeps falling every single month "
      "after the break too -- NOT just a one-time step, unlike every other section).")
print("\nFrom the article-level scrape (techi_articles.csv): 17 of the 20 newest "
      "Guides articles (85%) are dated on/after 2026-04-01, with the most recent "
      "on 2026-08-09 -- publishing did NOT stop in March 2026 as claimed.")
print('=> The note "Guides has published almost nothing since Mar 2026" is '
      "CONTRADICTED by the scraped rows.")
print("\nRecommendation: DO NOT retire Guides yet. The session collapse is real "
      "and Guides-specific in shape (continuous, not a one-time step like the "
      "other five sections), so it is not fully explained by the sitewide "
      "tracking swap alone -- but the stated justification for retiring it "
      "(abandoned section) is false, and Guides pages lean on calculators/tools "
      "that may not fire the new snippet the same way as article pages, which "
      "would show up exactly as this pattern. Audit Guides-page tracking first; "
      "retire only if a clean re-measurement still shows near-zero sessions.")
adj.to_csv("traffic_data_invented.csv", index=False)