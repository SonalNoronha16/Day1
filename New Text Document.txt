import streamlit as st
import numpy as np
import pickle

# Load model and tools
model = pickle.load(open("models/fraud_model.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))
le_location = pickle.load(open("models/location_encoder.pkl", "rb"))
le_device = pickle.load(open("models/device_encoder.pkl", "rb"))

st.title("💳 AI Fraud Detection Dashboard")

amount = st.number_input("Transaction Amount", min_value=0.0)
location = st.selectbox("Location", ["Mumbai", "Delhi", "Bangalore", "Chennai"])
device = st.selectbox("Device", ["Mobile", "Laptop", "Tablet"])
prev = st.slider("Previous Transactions", 1, 100)

if st.button("Check Fraud"):
    loc = le_location.transform([location])[0]
    dev = le_device.transform([device])[0]

    data = scaler.transform([[amount, loc, prev, dev]])
    pred = model.predict(data)[0]

    if pred == 1:
        st.error("🚨 Fraudulent Transaction Detected!")
    else:
        st.success("✅ Safe Transaction")
