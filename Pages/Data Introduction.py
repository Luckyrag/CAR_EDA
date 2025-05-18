import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(page_title="🚗 Car Data Overview", layout="wide")

# Inject custom CSS for animations and theme
st.markdown("""
    <style>
        /* Page fade-in */
        .main {
            animation: fadeIn 1.5s ease-in;
        }

        @keyframes fadeIn {
            0% {opacity: 0; transform: translateY(-10px);}
            100% {opacity: 1; transform: translateY(0);}
        }

        /* Animated title */
        .animated-title {
            font-size: 3em;
            font-weight: 700;
            color: #ff4b4b;
            text-align: center;
            margin-top: 20px;
            margin-bottom: 30px;
            animation: fadeIn 2s ease-in-out;
        }

        /* Section headers */
        h2 {
            color: #1f77b4;
        }

        /* Themed section borders */
        .stDataFrame {
            border: 2px solid #ddd !important;
            border-radius: 10px;
        }
    </style>

    <div class="animated-title">📄 Car Data Introduction</div>
""", unsafe_allow_html=True)

# Load data
raw_df = pd.read_csv("Cars (1).csv")
clean_df = pd.read_csv("Cars_cleaned.csv")

# Section 1: Raw Data
st.markdown("### 🔍 Raw Dataset")
st.dataframe(raw_df)

st.markdown("---")

# Section 2: Cleaned Data
st.markdown("### ✅ Cleaned Dataset")
st.dataframe(clean_df)

st.markdown("---")

# Section 3: Differences
st.markdown("### 🧠 Key Differences")
st.markdown("""
- ✅ **Missing Values** handled  
- 🧹 **Columns cleaned** (data types, units removed)  
- 📊 **Consistent formatting** (e.g., bhp, kmpl as numeric)  
- 🏷️ **Separated brand/model** in clean data  
- 🎨 **Theme & animation added for better UX**
""")
