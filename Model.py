import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("Cars_cleaned.csv")

# Dropdown for Company
company = st.selectbox("Select Car Company", df["Company_Name"].unique())

# Filter models based on company
models = df[df["Company_Name"] == company]["Model_Name"].unique()
model = st.selectbox("Select Car Model", models)

# Filter data for selected model
model_data = df[(df["Company_Name"] == company) & (df["Model_Name"] == model)]

# Engine options
engines = model_data["Engine_value"].dropna().unique()
if len(engines) == 1:
    engine = engines[0]  # auto-select
    st.write(f"Engine: {engine} cc (auto-selected)")
else:
    engine = st.selectbox("Select Engine Capacity (cc)", engines)

# Power options
powers = model_data["Power_value"].dropna().unique()
if len(powers) == 1:
    power = powers[0]
    st.write(f"Power: {power} bhp (auto-selected)")
else:
    power = st.selectbox("Select Power (bhp)", powers)

# Colour options
colours = model_data["Colour"].dropna().unique()
colour = st.selectbox("Select Car Colour", colours)

# Other inputs
year = st.slider("Select Year of Manufacture", 2000, 2025, 2015)
kms = st.number_input("Enter Kilometers Driven", min_value=1000, max_value=500000, step=1000)
fuel = st.selectbox("Fuel Type", model_data["Fuel_Type"].unique())
transmission = st.selectbox("Transmission", model_data["Transmission"].unique())
owner = st.selectbox("Owner Type", model_data["Owner_Type"].unique())
location = st.selectbox("Location", df["Location"].unique())
seats = st.selectbox("Seats", model_data["Seats"].dropna().unique())

# Predict Button
if st.button("Predict Price"):
    # Collect features into a dataframe for model input
    input_data = pd.DataFrame([{
        "Company_Name": company,
        "Model_Name": model,
        "Year": year,
        "Kilometers_Driven": kms,
        "Fuel_Type": fuel,
        "Transmission": transmission,
        "Owner_Type": owner,
        "Engine_value": engine,
        "Power_value": power,
        "Seats": seats,
        "Colour": colour,
        "Location": location
    }])
    
    # Predict using your ML model (replace with your trained model)
    # predicted_price = model.predict(input_data)[0]
    predicted_price = 600000  # dummy for now
    
    st.success(f"Predicted Car Price: ₹ {predicted_price:,.2f}")
