# 🛍️ Marketing Campaign Response Predictor

This project aims to identify customer groups most likely to respond positively to a marketing promotion using predictive modeling. It includes logistic regression, random forest modeling, threshold optimization, cost-benefit simulation, A/B testing setup, and API and Streamlit interface deployment.

## Project Objectives
- Predict the likelihood of customer response to a promotional offer.
- Identify and target high-response segments to maximize ROI.
- Simulate and validate business impact through cost-benefit analysis.
- Prepare for real-world deployment and integration.

## Key Features
Data Processing: Cleaned, encoded, and feature-engineered customer behavior data.

Modeling: Logistic Regression & Random Forest (AUC > 0.92).

Threshold Tuning: F1 and Youden’s J used for optimal cutoff selection (0.46).

Business Uplift Simulation: Estimated uplift of $6.8K from targeted outreach.

Cost-Benefit Analysis: ROI of 225% from campaign scenario.

A/B Testing Design: Power analysis for pilot test planning.

Deployment Options:

REST API scoring (/scoring_api/api.py)

Streamlit web app (/dashboard/streamlit_app.py)

```graphql
‑Marketing-analytics
│
├─ models/
│   └─ promo_model.pkl          ← your serialized RandomForest
│
├─ scoring_api/
│   ├─ api.py                   ← FastAPI scoring service
│   └─ requirements.txt         ← fastapi, uvicorn, scikit‑learn, pandas…
│
└─ dashboard/
    ├─ streamlit_app.py         ← Streamlit UI that calls api.py or loads model
    └─ requirements.txt         ← streamlit, requests, pandas…
```
