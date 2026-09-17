# Tech About Assessment:
A data analysis and web scraping assessment completed as part of the **Tech About recruitment process**. This project focuses on collecting article metadata, analyzing website traffic data, and evaluating traffic trends across different content sections.
# Project Overview:
The assessment was designed to investigate whether **TECHi's website traffic had increased by 30% year over year (YoY)**.
The project combines web scraping, data cleaning, exploratory data analysis, and business-oriented reporting to identify traffic patterns and evaluate the provided business claim.
# Objectives:
* Scrape the 20 newest articles from each designated TECHi section.
* Collect and organize article metadata.
* Perform data cleaning and feature engineering.
* Analyze traffic trends across website sections.
* Compare year-over-year traffic performance.
* Evaluate the claim that traffic increased by 30% YoY.
* Investigate the potential impact of retiring the **Guides** section.
* Communicate findings through a concise analytical memo.
# Sections Covered:
The article collection covered the following TECHi sections:
* AI.
* Markets.
* Crypto.
* Breakthroughs.
* Policy.
* Guides.
# Technologies & Tools:
* **Python**
* **Pandas** — Data manipulation and analysis.
* **Requests** — Web requests.
* **BeautifulSoup** — HTML parsing and web scraping.
* **Matplotlib / Seaborn** — Data visualization.
* **Jupyter Notebook / Google Colab**.
* **CSV** — Data storage and exchange.
* **Git & GitHub** — Version control.
# Data Collection:
The article dataset was designed to contain the following fields:
| Column                | Description                               |
| --------------------- | ----------------------------------------- |
| `url`                 | Article URL                               |
| `section`             | TECHi content section                     |
| `headline`            | Article headline                          |
| `author`              | Article author                            |
| `date_shown`          | Published or displayed date               |
| `headline_word_count` | Number of words in the headline           |
| `format`              | Article format                            |
| `names_a_company`     | Whether a company or named entity appears |
| `contains_a_number`   | Whether the headline contains a number    |

> The collection process followed the assessment's request-rate limitation of **one request every two seconds**.
# Analysis Workflow:
```text
Article Collection.
        ↓
Data Cleaning.
        ↓
Feature Engineering.
        ↓
Exploratory Data Analysis.
        ↓
Traffic Trend Analysis.
        ↓
Year-over-Year Comparison.
        ↓
Business Claim Evaluation.
        ↓
Final Analytical Memo.
```
# Key Analysis Areas:
## 1. Article Metadata Analysis:
* Distribution of articles by section.
* Headline word counts.
* Article formats.
* Authors and publishing patterns.
* Use of company names and numbers in headlines.

---

## 2. Traffic Analysis:
* Sessions by content section.
* Monthly traffic trends.
* Year-over-year comparisons.
* Contribution of individual sections to total traffic.
* Identification of growth and decline patterns.

---

## 3. Guides Section Evaluation:
The analysis considers the potential consequences of retiring the **Guides** section, including its contribution to traffic and its possible effect on overall website performance.
# Project Structure:
```text
Tech-About-Assessment/
│
├── data/
│   ├── techi_articles.csv
│   └── analysis.csv
│
├── notebooks/
│   └── analysis.ipynb
│
├── scripts/
│   └── scraping.py
│
├── memo.md
├── method.txt
└── README.md
```
> **Note:** Update the folder and file names above to match the actual repository structure.
# Deliverables:
* **Article dataset:** Scraped TECHi article metadata.
* **Traffic analysis:** Section-level traffic analysis and comparisons.
* **Methodology:** Explanation of scraping, assumptions, and analytical approach.
* **Analytical memo:** Summary of findings and business implications.
# Data & Methodology Note:
The assessment depends on the availability and completeness of the provided traffic data. Conclusions should be based only on the supplied dataset and documented assumptions. Missing data should not be reconstructed or treated as observed values.
# Learning Outcomes:
This assessment strengthened my practical experience in:
* Web scraping and structured data collection.
* Data preprocessing and feature engineering.
* Exploratory data analysis.
* Business-focused data interpretation.
* Year-over-year performance analysis.
* Communicating technical findings to stakeholders.
* Working with real-world data limitations.
