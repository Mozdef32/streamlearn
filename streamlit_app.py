import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# --- PAGE SETUP ---
st.set_page_config(page_title="Global Weather Analytics", page_icon="🌤️", layout="wide")

st.title("🌏 Global Weather Data Exploooooooooorer")
st.markdown("A hobbyist tool to analyze real-time atmospheric data from any city in the world.")

# --- SIDEBAR ---
with st.sidebar:
    st.header("Search Settings")
    city = st.text_input("Enter City Name:", "Casablanca")
    unit = st.radio("Temperature Unit:", ["Celsius", "Fahrenheit"])
    st.divider()
    st.info("Data source: wttr.in (Open Source API)")

# --- DATA FETCHING ---
@st.cache_data # This keeps the app fast by not re-downloading data on every click
def get_weather_data(city):
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

data = get_weather_data(city)

if data:
    current = data['current_condition'][0]
    temp = current['temp_C'] if unit == "Celsius" else current['temp_F']
    
    # --- TOP METRICS ---
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Current Temp", f"{temp}°")
    col2.metric("Humidity", f"{current['humidity']}%")
    col3.metric("Wind Speed", f"{current['windspeedKmph']} km/h")
    col4.metric("Cloud Cover", f"{current['cloudcover']}%")

    st.divider()

    # --- FORECAST DATA ANALYSIS ---
    st.subheader(f"Next 24-Hour Trend for {city.title()}")
    
    # Extracting hourly forecast for the first day
    hourly_raw = data['weather'][0]['hourly']
    
    # Structuring data for analysis
    forecast_list = []
    for h in hourly_raw:
        forecast_list.append({
            "Time": f"{int(h['time'])//100}:00",
            "Temp": int(h['tempC']) if unit == "Celsius" else int(h['tempF']),
            "FeelsLike": int(h['FeelsLikeC']) if unit == "Celsius" else int(h['FeelsLikeF']),
            "Chance of Rain": int(h['chanceofrain'])
        })
    
    df = pd.DataFrame(forecast_list)

    # Visual 1: Temperature vs Feels Like
    fig_temp = px.line(df, x="Time", y=["Temp", "FeelsLike"], 
                      title="Temperature vs. Perceived Temperature",
                      markers=True, template="plotly_white")
    st.plotly_chart(fig_temp, use_container_width=True)

    # Visual 2: Rainfall Probability
    fig_rain = px.area(df, x="Time", y="Chance of Rain", 
                      title="Probability of Precipitation (%)",
                      color_discrete_sequence=['#00CC96'], template="plotly_white")
    st.plotly_chart(fig_rain, use_container_width=True)

else:
    st.error("Could not find data for that city. Please check the spelling.")
