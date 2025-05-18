import streamlit as st
import json
from streamlit_lottie import st_lottie

# Initialize session state for theme and sidebar visibility
if "theme" not in st.session_state:
    st.session_state.theme = "light"
if "sidebar_visible" not in st.session_state:
    st.session_state.sidebar_visible = False

# Set page configuration based on sidebar visibility
st.set_page_config(
    page_title="Cars EDA Project",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded" if st.session_state.sidebar_visible else "collapsed"
)

# Function to toggle sidebar visibility
def toggle_sidebar():
    st.session_state.sidebar_visible = not st.session_state.sidebar_visible
    st.rerun()

# Apply theme-specific styles
if st.session_state.theme == "dark":
    st.markdown("""
        <style>
            .stApp {
                background-color: #0f0f0f;
                color: #ffffff;
            }
            .main-title {
                font-size: 48px;
                font-weight: bold;
                text-align: center;
                background: linear-gradient(to right, #ff8c00, #e52e71);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 10px;
                animation: fadeIn 1s ease-in-out;
            }
            .subtitle {
                font-size: 20px;
                text-align: center;
                color: #cccccc;
                margin-bottom: 30px;
                animation: fadeIn 1.3s ease-in-out;
            }
            .section-header {
                font-size: 28px;
                font-weight: 600;
                color: #00ced1;
                margin-top: 40px;
                margin-bottom: 10px;
                animation: fadeIn 1.5s ease-in-out;
            }
            .footer-note {
                font-size: 16px;
                color: #aaaaaa;
                text-align: center;
                margin-top: 50px;
                animation: fadeIn 1.6s ease-in-out;
            }
            @keyframes fadeIn {
                from {opacity: 0; transform: translateY(-10px);}
                to {opacity: 1; transform: translateY(0);}
            }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
            .stApp {
                background-color: #ffffff;
                color: #000000;
            }
            .main-title {
                font-size: 48px;
                font-weight: bold;
                text-align: center;
                background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 10px;
                animation: fadeIn 1s ease-in-out;
            }
            .subtitle {
                font-size: 20px;
                text-align: center;
                color: #333333;
                margin-bottom: 30px;
                animation: fadeIn 1.3s ease-in-out;
            }
            .section-header {
                font-size: 28px;
                font-weight: 600;
                color: #2980B9;
                margin-top: 40px;
                margin-bottom: 10px;
                animation: fadeIn 1.5s ease-in-out;
            }
            .footer-note {
                font-size: 16px;
                color: #666666;
                text-align: center;
                margin-top: 50px;
                animation: fadeIn 1.6s ease-in-out;
            }
            @keyframes fadeIn {
                from {opacity: 0; transform: translateY(-10px);}
                to {opacity: 1; transform: translateY(0);}
            }
        </style>
    """, unsafe_allow_html=True)

# Main content area
st.markdown('<div class="main-title">🚗 Cars Exploratory Data Analysis (EDA) Project</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Understand the Used Car Market with Data-Driven Insights</div>', unsafe_allow_html=True)

# Load and display Lottie animation
with open("Animation - 1747509304518.json") as anim_file:
    car_animation = json.load(anim_file)

st_lottie(car_animation, speed=1, loop=False, height=300, key="car_animation")

# Problem Statement
st.markdown('<div class="section-header">🔍 Problem Statement</div>', unsafe_allow_html=True)
st.markdown("""
The **used car market** is booming 🚀, yet buyers and sellers often lack reliable insights to navigate pricing, quality, and demand.

This project delivers a comprehensive **Exploratory Data Analysis (EDA)** on real used car listings. It reveals meaningful **trends, anomalies, and value drivers** across key features:

- 📍 **Location**
- 📅 **Manufacturing Year**
- 🛣️ **Mileage**
- ⛽ **Fuel Type**
- 💰 **Price**

### 💡 Objectives:
- Analyze and visualize core market factors
- Help buyers/sellers set **fair prices**
- Enable **data-driven decision-making** with confidence
""")

# Footer
st.markdown("---")
st.markdown('<div class="footer-note">📊 Explore the data to uncover insights into the used car market.</div>', unsafe_allow_html=True)


# Sidebar content
if st.session_state.sidebar_visible:
    with st.sidebar:
        st.header("Sidebar")
        # Theme toggle button in the sidebar
        if st.button("🌙 Toggle Theme"):
            st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"
            # st.rerun()
def toggle_sidebar():
    st.session_state.sidebar_visible = not st.session_state.sidebar_visible
    st.session_state._force_rerun = True  # Dummy flag to force rerun

# Toggle sidebar button in the main content area
st.button("Toggle Sidebar", on_click=toggle_sidebar)