import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# --- CONFIG ---
st.set_page_config(page_title="Data Insights Pro", layout="wide")

st.title("📊 Smart Data Profiler")
st.markdown("Upload any dataset to get an instant structural analysis.")

# --- FILE UPLOADER ---
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=['csv', 'xlsx'])

if uploaded_file is not None:
    # Load data
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # --- SIDEBAR FILTERS ---
    st.sidebar.header("Filter Data")
    all_columns = df.columns.tolist()
    selected_columns = st.sidebar.multiselect("Select Columns to Analyze", all_columns, default=all_columns[:5])

    # --- MAIN TABS ---
    tab1, tab2, tab3 = st.tabs(["📋 Raw Data", "📈 Statistics", "🔗 Correlations"])

    with tab1:
        st.subheader("Data Preview")
        st.dataframe(df[selected_columns].head(10), use_container_width=True)
        
        col1, col2 = st.columns(2)
        col1.write(f"**Total Rows:** {df.shape[0]}")
        col2.write(f"**Total Columns:** {df.shape[1]}")

    with tab2:
        st.subheader("Numerical Summary")
        st.write(df.describe())
        
        st.subheader("Missing Values")
        missing = df.isnull().sum()
        st.write(missing[missing > 0] if missing.sum() > 0 else "No missing values found! ✅")

    with tab3:
        st.subheader("Correlation Heatmap")
        numeric_df = df.select_dtypes(include=['number'])
        
        if not numeric_df.empty:
            corr = numeric_df.corr()
            fig = px.imshow(corr, text_auto=True, aspect="auto", 
                           color_continuous_scale='RdBu_r',
                           title="How variables relate to each other")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Add some numerical columns to see correlations.")

else:
    st.info("💡 Hint: Try uploading one of your provincial project exports or a simple budget sheet.")

# --- FOOTER ---
st.divider()
st.caption("Built for high-efficiency data analysis | Powered by Streamlit")
