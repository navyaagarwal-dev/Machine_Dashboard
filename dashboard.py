import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI Predictive Maintenance Dashboard", layout="wide")

# Title
st.title("AI Predictive Maintenance Dashboard")
st.write("Monitor machine health and detect anomalies in real-time.")

# System Overview
st.subheader("System Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Machines Running", "12")
col2.metric("Active Alerts", "2")
col3.metric("System Health", "92%")
col4.metric("Anomalies Detected", "3")

st.divider()

# Tabs
tab1, tab2 = st.tabs(["Machine Data Analysis", "System Status"])

# ---------------- TAB 1 ----------------
with tab1:

    st.subheader("Machine Data Analysis")

    uploaded_file = st.file_uploader("Upload a CSV file to start analysis", type=["csv"])

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.write("### Uploaded Dataset")
        st.dataframe(df)

        if "time" in df.columns and "temperature" in df.columns:

            # Anomaly Detection
            mean_temp = df["temperature"].mean()
            std_temp = df["temperature"].std()

            df["anomaly"] = abs(df["temperature"] - mean_temp) > (1 * std_temp)

            anomalies = df[df["anomaly"] == True]

            # Graph
            fig = px.line(df, x="time", y="temperature", title="Machine Temperature Trend")

            fig.add_scatter(
                x=anomalies["time"],
                y=anomalies["temperature"],
                mode="markers",
                marker=dict(color="red", size=10),
                name="Anomaly"
            )

            st.plotly_chart(fig, use_container_width=True)

            st.success("Analysis complete. Red dots show anomalies.")

        else:
            st.warning("CSV must contain 'time' and 'temperature' columns.")

# ---------------- TAB 2 ----------------
with tab2:

    st.subheader("System Status")

    colA, colB = st.columns(2)

    colA.write("### Machine Health")
    colA.success("Machine A: Normal")
    colA.warning("Machine B: High Temperature")
    colA.success("Machine C: Normal")

    colB.write("### Alerts")
    colB.error("Temperature spike detected")

    colB.warning("Vibration level approaching threshold")
