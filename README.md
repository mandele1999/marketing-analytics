![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Project-Complete-brightgreen)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-orange?logo=streamlit)
![Made with](https://img.shields.io/badge/Made%20with-💡%20Data%20Science-blueviolet)

![street-market](https://github.com/user-attachments/assets/9309abbb-5d85-45f7-9d80-5027d0d9520e)


# 🛍️ Marketing Campaign Response Optimizer

This project helps businesses identify customers most likely to respond positively to marketing offers. By using predictive analytics and targeted strategies, it boosts campaign effectiveness and return on investment (ROI). The solution includes response prediction, profit simulation, A/B testing planning, and deployment options.

## Project Objectives

- Predict which customers are likely to respond to a campaign.
- Focus efforts on high-value segments.
- Maximize revenue uplift while minimizing costs.
- Simulate business impact and measure performance.
- Deploy the solution for easy integration into marketing workflows.

## Key Features

- **Data Processing**: Cleaned, encoded, and feature-engineered customer behavior data.
- **Modeling**: Logistic Regression & Random Forest (AUC > 0.92).
- **Threshold Tuning**: F1 and Youden’s J used for optimal cutoff selection (0.46). _(Campaign Targeting Strategy using data-backed thresholds)_
- **Business Uplift Simulation**: Estimated uplift of $6.8K from targeted outreach.
- **Cost-Benefit Analysis**: ROI of 225% from campaign scenario; estimate net profit and ROI
- **A/B Testing Design**: Power analysis for pilot test planning.
- **Deployment Tools**:
    - REST API scoring (`/scoring_api/api.py`)
    - Streamlit web app (`/dashboard/streamlit_app.py`)

## How to Use

1. **Setup**

```text
git clone https://github.com/yourusername/marketing-analytics.git
cd marketing-analytics
pip install -r requirements.txt
```

2. **Run Scoring API**

```text
cd scoring_api
uvicorn api:app --reload
```

3. **Launch Streamlit App**

```text
cd dashboard
streamlit run streamlit_app.py
```

## 📁 Project Structure

```text

Marketing-analytics
│
├─ models/
│   └─ promo_model.pkl          ← your serialized RandomForest
│
├─ scoring_api/
│   ├─ api.py                   ← FastAPI scoring service
│   └─ requirements.txt         ← fastapi, uvicorn, scikit‑learn, pandas…
│
├─ dashboard/
│   ├─ streamlit_app.py         ← Streamlit UI that calls api.py or loads model
│   └─ requirements.txt         ← streamlit, requests, pandas…
│
├── data/                     # raw data
├── docs/                     # Documentation & glossary
│   └── glossary.md
│
├── index.ipynb
├── requirements.txt
└── README.md    
```

## Key Results / Business Impact

- Best Model: `Random Forest` (CV AUC: 0.926)
- Targeted Group Response Rate: `78.4%` vs Baseline `42.9%`
- Estimated Revenue Uplift: `$6.8K`
- Campaign ROI: `225%`

## License

[MIT License](LICENSE)

## 📘 Glossary

For clear definitions of key business and modeling terms used in this project, please refer to the [Business Glossary](./docs/glossary.md) and [About Dataset](./docs/data_description.md)

## Data Source

The dataset used in this project was obtained from [Kaggle](https://www.kaggle.com/datasets/zeesolver/consumer-behavior-and-shopping-habits-dataset). The dataset includes consumer behavior and shopping habits

### Credits: (<a href="https://www.flaticon.com/free-stickers/clothing" title="clothing stickers">Clothing stickers created by Stickers - Flaticon</a>)

