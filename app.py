# api.py
from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()
model = pickle.load(open("promo_model.pkl","rb"))

@app.post("/score")
def score(customers: list[dict]):
    df = pd.DataFrame(customers)
    probs = model.predict_proba(df)[:,1]
    return {"scores": probs.tolist()}
