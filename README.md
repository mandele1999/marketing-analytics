
```text
‑promo/
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
