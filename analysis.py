import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
BASE = Path.cwd()

# PART 1:
df = pd.read_csv(BASE / "techi_articles.csv")
assert len(df) == 120
assert (df.groupby("section").size() == 20).all()
section_summary = (
    df.groupby("section")
      .agg(
          articles=("url", "size"),
          company_headlines=("names_a_company", "sum"),
          number_headlines=("contains_a_number", "sum"),
      )
)
section_summary["company_headline_pct"] = (
    section_summary["company_headlines"] / section_summary["articles"] * 100
)
section_summary["number_headline_pct"] = (
    section_summary["number_headlines"] / section_summary["articles"] * 100
)
format_summary = pd.crosstab(df["section"], df["format"])

# Guides publication-recency check.
guides = df[df["section"] == "Guides"].copy()
guides["date_parsed"] = pd.to_datetime(guides["date_shown (verbatim)"], errors="coerce")
if guides["date_parsed"].isna().any():
    raise ValueError("Some Guides dates failed to parse -- check date_shown (verbatim).")
analysis_start_date = pd.Timestamp("2026-04-01")
guides_check = pd.DataFrame({
    "metric": [
        "Total Guides rows (sample)",
        "Guides rows dated on/after 2026-04-01",
        "Earliest Guides date in sample",
        "Latest Guides date in sample",
    ],
    "value": [
        len(guides),
        int((guides["date_parsed"] >= analysis_start_date).sum()),
        guides["date_parsed"].min().date().isoformat(),
        guides["date_parsed"].max().date().isoformat(),
    ],
})

# Cross-listing check (articles appearing on 2+ category pages).
dupe_mask = df.duplicated("url", keep=False)
n_dupe_articles = df.loc[dupe_mask, "url"].nunique()
crosslisting_check = pd.DataFrame({
    "metric": [
        "Sampled rows (120 = 6 sections x 20)",
        "Unique urls in sample",
        "Articles appearing on 2+ category pages in sample",
        "Category-page story counts, summed (site-reported totals)",
    ],
    "value": [
        len(df),
        df["url"].nunique(),
        n_dupe_articles,
        "472+1637+119+425+270+115 = 3038 (AI, Markets, Crypto, Breakthroughs, Policy, Guides)",
    ],
})

print("SECTION SUMMARY\n", section_summary, "\n")
print("FORMAT SUMMARY\n", format_summary, "\n")
print("GUIDES CHECK\n", guides_check, "\n")
print("CROSS-LISTING CHECK\n", crosslisting_check, "\n")

# PART 2:
traffic = pd.read_csv(BASE / "traffic_data_invented.csv")

# Export everything to one workbook.
xlsx = BASE / "analysis.xlsx"
with pd.ExcelWriter(xlsx, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Article_Data", index=False)
    section_summary.reset_index().to_excel(writer, sheet_name="Section_Summary", index=False)
    format_summary.reset_index().to_excel(writer, sheet_name="Format_Summary", index=False)
    guides_check.to_excel(writer, sheet_name="Guides_Check", index=False)
    crosslisting_check.to_excel(writer, sheet_name="CrossListing_Check", index=False)
    traffic.to_excel(writer, sheet_name="Traffic_Data_INVENTED", index=False)

print(f"Workbook written: {xlsx}")

# Chart 1: article format mix per section (bug from the original notebook fixed explicit fig/ax instead of relying on the current-figure default).
fig1, ax1 = plt.subplots(figsize=(8.5, 5))
format_summary.plot(kind="bar", stacked=True, ax=ax1)
ax1.set_ylabel("Number of Sampled Articles")
ax1.set_xlabel("Article Section")
ax1.set_title("Article Format Mix: 20 Newest Sampled Articles per Section")
ax1.tick_params(axis="x", rotation=30)
for label in ax1.get_xticklabels():
    label.set_ha("right")
ax1.legend(title="Article Format")
fig1.tight_layout()
fig1.savefig(BASE / "chart_format_mix.png", dpi=180)
plt.close(fig1)

# Chart 2: monthly sessions by section, with the Feb-2026 tracking-change line marked, so the reader sees the break rather than reading it as trend.
section_cols = ["AI_Sessions", "Markets_Sessions", "Crypto_Sessions",
                 "Breakthroughs_Sessions", "Policy_Sessions", "Guides_Sessions"]
fig2, ax2 = plt.subplots(figsize=(9, 5.2))
for col in section_cols:
    ax2.plot(traffic["Month"], traffic[col], marker="o", label=col.replace("_Sessions", ""))
ax2.axvline(x="Feb 2026", color="red", linestyle="--", linewidth=1, alpha=0.7)
ax2.text(traffic["Month"].tolist().index("Feb 2026") + 0.1, ax2.get_ylim()[1] * 0.92,
         "analytics snippet\nswapped 1 Feb 2026", color="red", fontsize=8, va="top")
ax2.set_ylabel("Sessions (invented data)")
ax2.set_xlabel("Month")
ax2.set_title("Monthly Sessions by Section, with the Unchecked Tracking Change Marked")
ax2.tick_params(axis="x", rotation=45)
for label in ax2.get_xticklabels():
    label.set_ha("right")
ax2.legend(fontsize=8, ncol=2)
fig2.tight_layout()
fig2.savefig(BASE / "chart_sessions_by_section.png", dpi=180)
plt.close(fig2)

print("Charts written: chart_format_mix.png, chart_sessions_by_section.png")