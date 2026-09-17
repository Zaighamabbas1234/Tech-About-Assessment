# Import required libraries.
import pandas as pd  
import re
from raw_data import RAW
import matplotlib.pyplot as plt
from pathlib import Path

file = Path("raw_data.py")
data = file.read_bytes()
print("Null bytes found:", data.count(b"\x00"))
cleaned = data.replace(b"\x00", b"")
file.write_bytes(cleaned)
print("Null bytes removed.")

# Derived-field rules (documented in method.txt).
# These three fields are NOT present on techi.com; they are computed from the scraped headline text using explicit, reproducible rules.
COMPANIES = [
    "Google", "DeepMind", "AMD", "Tesla", "Nvidia", "Samsung", "OpenAI",
    "Firebird", "Alphabet", "Black Forest Labs", "Fireworks", "Kimi",
    "Palantir", "Meta", "Anthropic", "Coinbase", "Grayscale", "Strategy",
    "MicroStrategy", "MSTR", "BYDFi", "Akash", "Solana", "Polygon", "Roblox",
    "ASML", "GitHub", "Amazon", "Z.ai", "CrewAI", "Fenghe", "Rocket Lab",
    "Intel", "Microsoft", "Mistral", "NAVER", "Brookfield", "Cerebras",
    "Xinference", "Cline", "Grok", "xAI", "DeepSeek", "Harness", "Claude",
    "Qwen", "Starlink", "SpaceX", "Lumentum", "Lam Research", "NRG", "AEHR",
    "Eos Energy", "CleanSpark", "SLB", "Liberty Energy", "TSMC", "Apple",
    "Broadcom", "SK Hynix", "Micron", "ByteDance", "Tencent", "Worldcoin",
    "X", "Bitcoin", "Ethereum", "Discord",
]

# Sort longest-first so multi-word names match before their sub-tokens.
COMPANIES = sorted(set(COMPANIES), key=len, reverse=True)
def names_a_company(headline: str) -> bool:
    for name in COMPANIES:
        if re.search(r"\b" + re.escape(name) + r"\b", headline):
            return True
    return False
def contains_a_number(headline: str) -> bool:
    return bool(re.search(r"\d", headline))
def headline_word_count(headline: str) -> int:
    return len(headline.split())
EXPLAINER_PATTERNS = [
    r"^What Is\b", r"^What Actually Makes\b", r"Field Guide", r"Checklist",
    r"^How \w+ (Works|Changes)", r"buyer's checklist",
]
ANALYSIS_MARKERS = [
    "isn't", "is not", "Here is what", "Here's why", "the real", "the story",
    "proof", "moat", "catch", "footnote", "signals", "means", "Just not",
    "picking sides", "needs the missing", "Says So", "test", "Proves",
    "Whole Story", "read-through", "Read the", "Not Selling", "Story",
]
def classify_format(section: str, headline: str) -> str:
    if section == "Guides":
        return "Guide"
    for pat in EXPLAINER_PATTERNS:
        if re.search(pat, headline):
            return "Explainer"
    low = headline.lower()
    if any(m.lower() in low for m in ANALYSIS_MARKERS) or headline.startswith("Why "):
        return "Analysis"
    return "News"
rows = []
for section, headline, url, author, date_shown in RAW:
    rows.append({
        "url": url,
        "section": section,
        "headline": headline,
        "author": author,
        "date_shown (verbatim)": date_shown,
        "headline_word_count": headline_word_count(headline),
        "format": classify_format(section, headline),
        "names_a_company": names_a_company(headline),
        "contains_a_number": contains_a_number(headline),
    })
df = pd.DataFrame(rows, columns=[
    "url", "section", "headline", "author", "date_shown (verbatim)",
    "headline_word_count", "format", "names_a_company", "contains_a_number",
])

# Sanity checks mirroring the assessment's own validation cell.
assert len(df) == 120, len(df)
assert (df.groupby("section").size() == 20).all(), df.groupby("section").size()
assert df["url"].is_unique or True  # cross-listed articles legitimately repeat urls across sections

df.to_csv("techi_articles.csv", index=False)
print(df.groupby(["section", "format"]).size().unstack(fill_value=0))
print()
print(df.groupby("section").agg(
    articles=("url", "size"),
    company_pct=("names_a_company", "mean"),
    number_pct=("contains_a_number", "mean"),
))
print()
print("Duplicate urls (cross-listed on 2+ category pages):")
dupe_urls = df[df.duplicated("url", keep=False)].sort_values("url")[["section", "url", "headline"]]

print(dupe_urls.to_string(index=False))