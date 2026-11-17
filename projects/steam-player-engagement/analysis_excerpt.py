"""Adapted, portable excerpt from the uploaded APAN5205 group final_code.ipynb.

Input CSVs are intentionally not bundled. This excerpt reproduces the
review-sentiment and first regression stages, not the complete group notebook.
"""
from pathlib import Path
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

DATA = Path(__file__).resolve().parent / "data"
reviews = pd.read_csv(DATA / "clean_review_proposal.csv")
steam = pd.read_csv(DATA / "clean_steamspy_proposal.csv")
reviews["review_date"] = pd.to_datetime(reviews["review_date"], errors="coerce")
for col in ["voted_up_int", "review_length", "author.playtime_forever"]:
    reviews[col] = pd.to_numeric(reviews[col], errors="coerce")
for col in ["median_forever", "ccu"]:
    steam[col] = pd.to_numeric(steam[col], errors="coerce")

analyzer = SentimentIntensityAnalyzer()
reviews["vader_compound"] = reviews["review"].fillna("").astype(str).map(
    lambda text: analyzer.polarity_scores(text)["compound"]
)
reviews["is_short_review"] = (reviews["review_length"] <= 5).astype(int)
summary = reviews.groupby("appid").agg(
    positive_ratio=("voted_up_int", "mean"),
    avg_vader_compound=("vader_compound", "mean"),
    short_review_share=("is_short_review", "mean"),
).reset_index()
df = summary.merge(steam, on="appid", how="inner")
df["log_median_forever"] = np.log1p(df["median_forever"].clip(lower=0))
df["log_ccu"] = np.log1p(df["ccu"].clip(lower=0))
model = smf.ols(
    "log_median_forever ~ positive_ratio + avg_vader_compound + short_review_share + log_ccu",
    data=df,
).fit(cov_type="HC3")
print(model.summary())
print("This excerpt omits the original notebook's review-trend feature; coefficients will differ.")
