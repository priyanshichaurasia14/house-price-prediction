import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("best_model.pkl", "rb"))

# Page Config
st.set_page_config(page_title="House Price Prediction", layout="centered")

# Title & Description
st.title("House Price Prediction App")
st.write("Enter the house details below and get an estimated price.")

# Input Fields
col1, col2 = st.columns(2)

with col1:
    sqft = st.number_input("Square Feet", min_value=500, max_value=10000, step=50)
    bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, step=1)

with col2:
    bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, step=1)
    year_built = st.number_input("Year Built", min_value=1900, max_value=2025, step=1)

neighborhood = st.selectbox("Neighborhood", ["Urban", "Suburb"])

# One-hot encoding
if neighborhood == "Urban":
    neighborhood_urban = 1
    neighborhood_suburb = 0
else:
    neighborhood_urban = 0
    neighborhood_suburb = 1

# Sidebar for USD to INR conversion
st.sidebar.title("Settings")
exchange_rate = st.sidebar.number_input("USD → INR Rate", min_value=50, max_value=120, value=83, step=1)
st.sidebar.write("Default conversion is 1 USD ≈ ₹83")

# Predict Button
if st.button("Predict Price"):
    input_data = np.array([[sqft, bedrooms, bathrooms, year_built,
                            neighborhood_suburb, neighborhood_urban]])
    
    prediction = model.predict(input_data)[0]

    # USD → INR Conversion
    prediction_inr = prediction * exchange_rate  

    st.subheader(f"Estimated Price in Rupees: ₹{prediction_inr:,.0f}")
    st.caption(f"(Base Price in USD: ${prediction:,.2f})")
