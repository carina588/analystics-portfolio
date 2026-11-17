# Credit Card Transaction Network Anomaly Detection

**Academic graph analytics case study**

## Research question
Can unusual cardholder–vendor relationships reveal transaction behavior that standard tabular summaries might miss?

## Dataset and period
The uploaded notebook analyzes Oklahoma purchase-card transactions, using monthly PageRank analysis from **July 2013 through June 2014**.

## Approach
- Construct a cardholder–vendor transaction network
- Calculate PageRank separately by month
- Identify sharp score changes and unusual network relationships
- Generate a shortlist for investigation

## Interpretation
A flagged transaction or network connection is a **review candidate, not confirmed fraud**. The notebook does not establish fraudulent activity or causal explanations.

## Source
Uploaded `Credit_Card_Graph_Anomaly_Assignment_Download.ipynb`. The complete notebook and reproducibility details will be added after dependency and data-path review.
