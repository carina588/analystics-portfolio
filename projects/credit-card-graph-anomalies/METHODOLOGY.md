# Methodology and interpretation

## Network representation
The project models payment-card transaction relationships as a graph, where cardholders and vendors are represented as distinct node types and observed transactions establish connections. Monthly graphs allow changes in connectivity to be compared over time.

## Analytical workflow
1. Load and validate transaction records, retaining the fields needed to identify cardholder, vendor, date and transaction magnitude.
2. Partition records by month, then construct the network for each period.
3. Compute PageRank scores and compare their month-to-month trajectories.
4. Flag unusually large score changes for investigation.
5. Review flagged entities with transaction-level context instead of interpreting scores alone.

## Why PageRank?
PageRank captures the structural importance of nodes based on their network connections. A sharp increase may indicate an emerging high-connectivity vendor or a change in transaction behavior. It is not inherently suspicious.

## Validation and caveats
- PageRank is a graph-centrality measure, **not a calibrated fraud probability**.
- A change in node score may reflect legitimate seasonality, procurement changes, or shifts in the number of active cards.
- Thresholds should be sensitivity-tested, with flagged examples reviewed against independent evidence.
- Without confirmed fraud labels, this is unsupervised anomaly detection rather than supervised fraud classification.

The source notebook uses local data paths; a portable notebook and results summary will follow after data-source review.
