import streamlit as st
import folium
from streamlit_folium import st_folium

# Set page config
st.set_page_config(page_title="Car Location Map", page_icon="📍", layout="wide")

# Custom theme and animation
st.markdown("""
    <style>
        .animated-title {
            font-size: 2.5em;
            font-weight: bold;
            color: #2E86C1;
            text-align: center;
            animation: fadeIn 2s ease-in-out;
            margin-bottom: 10px;
        }
        @keyframes fadeIn {
            0% {opacity: 0; transform: translateY(-10px);}
            100% {opacity: 1; transform: translateY(0);}
        }
    </style>
    <div class="animated-title">📍 Used Car Listings by Location</div>
""", unsafe_allow_html=True)

st.markdown("Click on each city marker to see how many used cars are listed.")

# Define city locations
locations = [
    {"city": "Mumbai", "lat": 19.0760, "lon": 72.8777, "count": 792},
    {"city": "Hyderabad", "lat": 17.3850, "lon": 78.4867, "count": 738},
    {"city": "Kochi", "lat": 9.9312, "lon": 76.2673, "count": 646},
    {"city": "Coimbatore", "lat": 11.0168, "lon": 76.9558, "count": 630},
    {"city": "Pune", "lat": 18.5204, "lon": 73.8567, "count": 611},
    {"city": "Delhi", "lat": 28.7041, "lon": 77.1025, "count": 549},
    {"city": "Kolkata", "lat": 22.5726, "lon": 88.3639, "count": 525},
    {"city": "Chennai", "lat": 13.0827, "lon": 80.2707, "count": 489},
    {"city": "Jaipur", "lat": 26.9124, "lon": 75.7873, "count": 406},
    {"city": "Bangalore", "lat": 12.9716, "lon": 77.5946, "count": 351},
    {"city": "Ahmedabad", "lat": 23.0225, "lon": 72.5714, "count": 222}
]

m = folium.Map(location=[21.146633, 79.088860], zoom_start=5)

for loc in locations:
    folium.Marker(
        location=[loc["lat"], loc["lon"]],
        popup=f"{loc['city']}: {loc['count']} cars",
        tooltip=loc["city"],
        icon=folium.Icon(color="blue", icon="car", prefix="fa")
    ).add_to(m)

st_data = st_folium(m, width=1000, height=600)
