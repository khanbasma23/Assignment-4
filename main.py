import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Data Analysis Web App")

# 📂 File Upload Section
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # 🔍 Data Preview
    st.subheader("Data Preview")
    st.write(df.head())

    # 📊 Data Summary
    st.subheader("Data Summary")
    st.write(df.describe())

    # 🔍 Filter Data
    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    # 📈 Plot Data
    st.subheader("Plot Data")
    x_column = st.selectbox("Select X-axis column", columns)
    y_column = st.selectbox("Select Y-axis column", columns)

    if st.button("Generate Plot"):
        fig, ax = plt.subplots()
        ax.scatter(df[x_column], df[y_column])
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        ax.set_title("Scatter Plot")
        st.pyplot(fig)
else:
    st.write("📂 Please upload a CSV file to proceed.")
