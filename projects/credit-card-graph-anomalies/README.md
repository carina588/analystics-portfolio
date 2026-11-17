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

## Run the notebook

[Open the curated analysis notebook](credit_card_graph_anomalies.ipynb). Install dependencies from [requirements.txt](requirements.txt) and place the original `purchase_credit_card.csv.zip` inside `data/`. This notebook is a privacy-conscious adaptation of the uploaded assignment: it excludes identifying output tables, uses portable paths, and generates an aggregate monthly anomaly chart when executed. The notebook has not yet been executed end-to-end in this published environment.

**Reported results from the original notebook:** 442,458 transactions over 12 months, 39 flagged node-months (27 cardholder and 12 vendor), and 466 large adjacent-month percentile movements. These are not counts of confirmed fraud cases.
