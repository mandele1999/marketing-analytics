# scoring_api/api.
# To Run this script:
# cd scoring_api
# pip install -r requirements.txt
# uvicorn api:app --host 0.0.0.0 --port 8000

# scoring_api/api.py

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import pickle, pandas as pd, json

# 1) Load model and feature‑column list
model = pickle.load(open("../models/promo_model.pkl","rb"))
expected_cols = json.load(open("../models/feature_columns.json","r"))

app = FastAPI()

class PromoInput(BaseModel):
    age: float
    previous_purchases: float
    freq_per_year: float
    loyalty_score: float
    gender: str
    item_purchased: str
    category: str
    location: str
    size: str
    color: str
    season: str
    shipping_type: str
    payment_method: str

@app.post("/score")
def score(inputs: List[PromoInput]):
    # 1) Build raw DataFrame
    df_raw = pd.DataFrame([i.dict() for i in inputs])
    print("🔴 RAW INPUT")
    print(df_raw.to_string(index=False))

    # 2) One‑hot encode
    df_dum = pd.get_dummies(
        df_raw,
        columns=[
          'gender','item_purchased','category','location',
          'size','color','season','shipping_type','payment_method'
        ],
        drop_first=False
    )
    print("🟠 AFTER get_dummies (before reindex), columns:", df_dum.columns.tolist())
    print(df_dum.to_string(index=False))

    # 3) Reindex to match training
    df = df_dum.reindex(columns=expected_cols, fill_value=0)
    print("🟢 AFTER reindex (final features), first row non‑zeros:")
    print(df.loc[0, df.loc[0] != 0])

    # 4) Score
    scores = model.predict_proba(df)[:,1]
    return {"scores": scores.tolist()}
