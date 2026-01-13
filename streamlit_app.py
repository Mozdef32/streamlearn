import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

# --- PAGE CONFIG ---
st.set_page_config(page_title="Executive Dashboard", page_icon="📊", layout="wide")

# --- STYLING ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("👤 Control Panel")
    st.info(f"Today is: {date.today().strftime('%B %d, 2026')}")
    st.divider()
    page = st.radio("Navigation", ["Project Overview", "Financial Growth", "Settings"])
    st.success("Status: Connected to Database")

# --- MAIN CONTENT ---
if page == "Project Overview":
    st.title("📂 Social Action Project Tracker")
    st.subheader("Division of Social Action - Provincial Monitoring")

    # 1. Metric Cards
    col1, col2, col3 = st.columns(3)
    col1.metric("Active Projects", "12", "+2 this month")
    col2.metric("Completion Rate", "68%", "5.2%")
    col3.metric("Budget Utilized", "1.2M DH", "-12k vs Forecast")

    st.divider()

    # 2. Task Progress (The 3 Tasks you mentioned earlier)
    st.subheader("🚀 Quick Task Visualization")
    
    # Dataframe for your tasks
    tasks_data = {
        "Task": ["Research", "Design", "Testing"],
        "Progress": [100, 45, 10],
        "Priority": ["High", "Medium", "Low"]
    }
    df = pd.DataFrame(tasks_data)

    # Cool Plotly Bar Chart
    fig = px.bar(
        df, 
        x="Progress", 
        y="Task", 
        orientation='h', 
        color="Priority",
        text="Progress",
        color_discrete_map={"High": "#EF553B", "Medium": "#636EFA", "Low": "#00CC96"},
        template="plotly_white"
    )
    fig.update_layout(xaxis_range=[0, 100])
    st.plotly_chart(fig, use_container_width=True)

elif page == "Financial Growth":
    st.title("📈 Halal Income Optimizer")
    st.write("Focused on high-success, low-capital digital opportunities.")
    
    # Simple Growth Simulation for your INTP brain
    st.info("Strategy: Leveraging IQ (125) for high-leverage digital services.")
    
    amount = st.slider("Monthly Investment in Skills (DH)", 0, 5000, 500)
    st.write(f"Projected digital equity growth based on {amount} DH monthly skill-up.")

# --- FOOTER ---
st.divider()
st.caption("Custom Dashboard for Administrative Excellence | Built with Streamlit & Python")
