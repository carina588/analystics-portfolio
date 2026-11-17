# Steam Reviews & Player Engagement

**Collaborative applied machine-learning project**

## Business question
Do review sentiment signals explain game engagement after accounting for popularity? Does this relationship vary across genres and player segments?

## Data
The group's report describes Steam review data and SteamSpy game-level data. It reports **33,704 reviews across 100 games** in the initial review-level collection, with **83 games** retained for game-level analysis after cleaning and matching.

## Methods
- VADER sentiment analysis of review text
- Feature engineering and integration of review and game statistics
- OLS regression with robust standard errors
- Genre-stratified comparisons
- K-Means clustering of reviewer behavior

## Selected findings
- Peak concurrent users were positively associated with long-term playtime in the reported model (p < 0.001).
- Review positivity, VADER sentiment and review trend were not statistically significant predictors in that model after controls.
- Reviewer segmentation identified two behavioral groups, described in the report as **Dedicated Specialists** and **Casual Explorers**.

## Business interpretation
Review sentiment should not be treated as a substitute for engagement metrics. Segment-level behavioral differences may help product teams tailor community and retention strategies.

## Important limitations
The study is observational and cross-sectional. Associations do not establish that popularity causes engagement or that reviews have no causal effect. The limited game sample and observation period restrict generalization.

**Source:** Uploaded group final report and analysis notebook. Collaborative work; individual contributions should be clarified before claiming sole authorship. A curated notebook will be added after checking paths and dependencies.

## My contribution
I contributed to both the **analysis and coding** and the **dashboards and visualizations** as part of the project team. The project is presented as collaborative work, not as an individual-only deliverable.
