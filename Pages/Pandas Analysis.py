import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="📊 Pandas Analysis", layout="wide")

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

    <div class='title-style'>📊 Pandas Analysis</div>
""", unsafe_allow_html=True)

df = pd.read_csv("Cars_cleaned.csv")

st.subheader("1. Basic Info")

# Display key points manually
# Display key points manually
# Row & column count
st.markdown(f"""
- 🔢 **Rows:** {df.shape[0]}  
- 📊 **Columns:** {df.shape[1]}  
""")

# Column names
st.markdown("#### 🧾 Column Names")
st.write(df.columns.tolist())

# Data types
st.markdown("#### 🧠 Data Types")
st.dataframe(pd.DataFrame(df.dtypes, columns=["Data Type"]).T)

# Memory usage using buffer
buffer = io.StringIO()
df.info(buf=buffer, memory_usage='deep')
info_str = buffer.getvalue()
mem_line = [line for line in info_str.split('\n') if "memory usage" in line.lower()]
if mem_line:
    st.markdown(f"#### 📦 Memory Usage\n- {mem_line[0]}")

# Categorical and Numeric Columns
numeric_cols = df.select_dtypes(include='number').columns.tolist()
categorical_cols = df.select_dtypes(exclude='number').columns.tolist()

st.markdown("#### 📈 Numeric Columns")
st.write(numeric_cols)

st.markdown("#### 🔤 Categorical Columns")
st.write(categorical_cols)

st.subheader("2. Summary Statistics")
st.dataframe(df.describe())

st.subheader("3. Null Values")
st.dataframe(df.isnull().sum())

st.subheader("4. Unique Value Counts")
for col in ['Fuel_Type', 'Transmission', 'Owner_Type', 'Colour', 'Company_Name','Location']:
    st.markdown(f"**{col}**: {df[col].nunique()} unique values")
    st.dataframe(df[col].value_counts())

st.subheader("5. Top 5 Most Driven Cars")
st.dataframe(df.sort_values(by='Kilometers_Driven', ascending=False)[['Name', 'Kilometers_Driven']].head())

st.subheader("6. Average Price by Company_Name")
st.dataframe(df.groupby("Company_Name")["Price"].mean().sort_values(ascending=False))
