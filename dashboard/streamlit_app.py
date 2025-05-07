# dashboard/streamlit_app.py ---Calling the scoring 

# To run this script:
# cd dashboard
# pip install -r requirements.txt
# streamlit run streamlit_app.py

import streamlit as st
import requests
# from pydantic import BaseModel

st.title("Promo Response Scorer (via API)")

# Collect inputs
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", 18, 100, 30)
prev = st.number_input("Previous purchases", 0, 100, 5)
freq = st.number_input("Freq per year", 1, 52, 12)
loyalty = st.slider("Loyalty score", 0.0, 2.0, 1.0)
item_purchased = st.selectbox("Item purchased", ["T-shirt", "Sneakers", "Jacket"])
category = st.selectbox("Category", ["Clothing", "Footwear", "Outerwear"])
location = st.selectbox("Location", ["Urban", "Suburban", "Rural"])
size = st.selectbox("Size", ["S", "M", "L", "XL"])
color = st.selectbox("Color", ["Red", "Blue", "Black", "White", "Cyan", "Gray"])
season = st.selectbox("Season", ["Spring", "Summer", "Autumn", "Winter"])
shipping_type = st.selectbox("Shipping type", ["Standard", "Express"])
payment_method = st.selectbox("Payment method", ["Credit Card", "PayPal", "Bank Transfer"])

# Call API
if st.button("Get Score"):
    payload = [{
        "gender": gender,
        "age": age,
        "previous_purchases": prev,
        "freq_per_year": freq,
        "loyalty_score": loyalty,
        "item_purchased": item_purchased,
        "category": category,
        "location": location,
        "size": size,
        "color": color,
        "season": season,
        "shipping_type": shipping_type,
        "payment_method": payment_method
    }]

    resp = requests.post("http://localhost:8000/score", json=payload)
    st.write("Status code:", resp.status_code)
    st.write("Response body:", resp.text)

    if resp.status_code == 200:
        try:
            score = resp.json()["scores"][0]
            st.success(f"Predicted response probability: {score:.2%}")
        except ValueError:
            st.error("API did not return valid JSON.")
    else:
        st.error(f"API error {resp.status_code}: see console for details.")
#--------------------------------------------------------------------

# This is a simple Streamlit app that collects user input and sends it to the FastAPI scoring API.
# ------If you prefer no API call, in streamlit_app.py simply do the following:------
# import streamlit as st
# import pickle
# import pandas as pd

# # Load model
# with open("../models/promo_model.pkl","rb") as f:
#     model = pickle.load(f)

# # (same inputs as above…)

# if st.button("Get Score"):
#     df = pd.DataFrame([{
#         "age": age,
#         "previous_purchases": prev,
#         "freq_per_year": freq,
#         "loyalty_score": loyalty
#     }])
#     score = model.predict_proba(df)[:,1][0]
#     st.write(f"Predicted response probability: {score:.2%}")
