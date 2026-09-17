# TECHi traffic assessment

## Contents
- `techi_articles.csv` — 120 supplied Part 1 article rows.
- `analysis.ipynb/.py` — reproducible analysis code.
- `analysis.xlsx` — article data, summaries, and traffic-data limitation sheet.
- `memo.md` — decision memo, under 700 words.
- `method.txt` — collection/analysis method and limits.
- `requirements.txt` — Python dependencies.
- `chart_company_mentions_by_section.png`
- `chart_format_mix.png`

## Setup
Python 3.10+ recommended.
VS Code Jupter Notebook.
Anaconda Jupter Notebook.

```bash
pip install -r requirements.txt
jupyter file analysis.ipynb
```

## Decisions and trade-offs
The brief asks for arithmetic on 12 invented months of sessions and newsletter signups. The available workbook did not contain those numeric observations. I chose not to reconstruct or infer them from prose because the brief explicitly says that any number not measured invalidates the work.

The submission therefore separates:
1. measured/descriptive results from the 120-row article dataset; and
2. untested traffic hypotheses from the assessment notes.

Only two charts are produced, both from measured article metadata.

## Tests
The analysis asserts:
- exactly 120 rows;
- no missing values;
- exactly six expected sections;
- 20 rows per section.

It also reports the available Guides dates after March 2026, allowing the “almost nothing since Mar 2026” note to be checked against the Part 1 sample.