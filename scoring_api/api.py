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
feature_cols = json.load(open("../models/feature_columns.json","r"))

app = FastAPI()

class Customer(BaseModel):
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
def score(customers: List[Customer]):
    # Build DataFrame
    df = pd.DataFrame([c.dict() for c in customers])

    # 2) One‑hot encode using the same columns you used in training
    df = pd.get_dummies(
        df,
        columns=['gender', 'item_purchased', 'category', 'location', 'size', 'color', 'season', 'shipping_type', 'payment_method'], drop_first=True)

    # 3) Reindex to exactly the columns the model expects
    df = df.reindex(columns=feature_cols, fill_value=0)

    # 4) Score
    probs = model.predict_proba(df)[:,1]
    return {"scores": probs.tolist()}