import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Streamlit App UI
st.title("📊 Simple Dta Visualizer - tessst")
st.write("Upload a CSV file to visualize its data.")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview", df.head())

    # Select columns
    numeric_cols = df.select_dtypes(include=["number"]).columns
    col1 = st.selectbox("Choose X-axis", numeric_cols)
    col2 = st.selectbox("Choose Y-axis", numeric_cols)

    # Choose chart type
    chart_type = st.selectbox("Choose Chart Type", ["Scatter", "Line", "Bar"])

    # Plot the selected chart
    fig, ax = plt.subplots()
    if chart_type == "Scatter":
        sns.scatterplot(data=df, x=col1, y=col2, ax=ax)
    elif chart_type == "Line":
        sns.lineplot(data=df, x=col1, y=col2, ax=ax)
    elif chart_type == "Bar":
        sns.barplot(data=df, x=col1, y=col2, ax=ax)

    st.pyplot(fig)