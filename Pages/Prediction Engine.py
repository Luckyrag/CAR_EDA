import streamlit as st
import pandas as pd
import joblib
import urllib.parse

# =========================
# 🎨 Page Configuration
# =========================
# Page Config
# ----------------------------
st.set_page_config(page_title="🚗 Car Price Prediction", layout="wide")



# Custom style and animation
st.markdown("""
    <style>
        .title-style {
            font-size: 2.5em;
            color: #17A589;
            font-weight: bold;
            animation: fadeIn 2s ease-in-out;
            text-align: center;
        }

        @keyframes fadeIn {
            0% {opacity: 0; transform: translateY(-20px);}
            100% {opacity: 1; transform: translateY(0);}
        }
    </style>

    <div class='title-style'>✨ Prediction Engine & Smart Recommendation ✨</div>
""", unsafe_allow_html=True)


# =========================
# 📦 Load Model & Data
# =========================
@st.cache_resource
def load_model():
    return joblib.load("car_price_model.pkl")

@st.cache_data
def load_data():
    return pd.read_csv("Cars_cleaned.csv")

model = load_model()
df = load_data()

# =========================
# 🖼️ Car Image API
# =========================
def create_car_image_url(car, angle="29", color=None):
    """
    Generate dynamic car images from imagin.studio API
    """
    base_url = "https://cdn.imagin.studio/getimage"
    params = {
        "customer": "hrjavascript-mastery",  # Free demo key
        "make": car["Company_Name"],
        "modelFamily": car["Model_Name"].split()[0],
        "modelYear": str(int(car["Year"])),
        "angle": angle,
        "paintDescription": color or car.get("Colour", "White"),
    }
    return f"{base_url}?{urllib.parse.urlencode(params)}"

# =========================
# 📝 Input Section
# =========================
st.header("🎯 Prediction Engine")
st.markdown("Fill in the car details below to estimate its **resale price** and get smart recommendations.")

company = st.selectbox("Company", sorted(df["Company_Name"].unique()))
models_available = df[df["Company_Name"] == company]["Model_Name"].unique()
model_name = st.selectbox("Model", sorted(models_available))
year = st.slider("Year", int(df["Year"].min()), int(df["Year"].max()), 2015)
fuel_type = st.selectbox("Fuel Type", df["Fuel_Type"].unique())
transmission = st.selectbox("Transmission", df["Transmission"].unique())
owner = st.selectbox("Owner Type", df["Owner_Type"].unique())

engine_opts = df[(df["Company_Name"] == company) & (df["Model_Name"] == model_name)]["Engine_value"].unique()
engine_value = st.selectbox("Engine (CC)", sorted(engine_opts))

power_opts = df[(df["Company_Name"] == company) & (df["Model_Name"] == model_name)]["Power_value"].unique()
power_value = st.selectbox("Power (bhp)", sorted(power_opts))

location = st.selectbox("Location", sorted(df["Location"].unique()))
colour_opts = df[(df["Company_Name"] == company) & (df["Model_Name"] == model_name)]["Colour"].unique()
colour = st.selectbox("Colour", sorted(colour_opts))

kms = st.number_input("Kilometers Driven", min_value=500, max_value=300000, step=500, value=50000)

predict_btn = st.button("🔮 Predict Price")

# =========================
# 📊 Prediction Section
# =========================
if predict_btn:
    # Prepare input
    input_dict = {
        "Company_Name": company,
        "Model_Name": model_name,
        "Year": year,
        "Fuel_Type": fuel_type,
        "Transmission": transmission,
        "Owner_Type": owner,
        "Kilometers_Driven": kms,
        "Engine_value": engine_value,
        "Power_value": power_value,
        "Location": location,
        "Colour": colour,
    }
    input_df = pd.DataFrame([input_dict])

    # Predict
    predicted_price = model.predict(input_df)[0]
    st.success(f"💰 Predicted Price for {company} {model_name} ({year}): **₹{predicted_price:.2f} Lakh**")

    # =========================
    # 🤖 Recommendation System
    # =========================
    st.header("✨ Smart Recommendations")
    st.markdown("Here are some **similar cars** you might want to explore:")

    rec_df = df[(df["Company_Name"] == company) & (df["Model_Name"] != model_name)]
    if rec_df.empty:
        st.info("No recommendations available.")
    else:
        recommendations = rec_df.sample(n=min(4, len(rec_df)), random_state=42).reset_index(drop=True)

        cols = st.columns(len(recommendations))
        for i, rec in recommendations.iterrows():
            with cols[i]:
                preview_url = create_car_image_url(rec, angle="29", color=rec["Colour"])
                st.image(preview_url, use_container_width=True)
                st.markdown(f"**{rec['Company_Name']} {rec['Model_Name']}**")
                st.write(f"Year: {int(rec['Year'])}")
                st.write(f"Fuel: {rec['Fuel_Type']} | Engine: {rec['Engine_value']} CC")
                st.write(f"Power: {rec['Power_value']} bhp | Owner: {rec['Owner_Type']}")
                st.write(f"📍 {rec['Location']}")
                st.info(f"💰 Price: ₹{rec['Price']} Lakh")


