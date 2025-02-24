
import streamlit as st
import pandas as pd

st.title("Simple Data Dashboard!")

# File uploader for CSV files
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    st.write("File uploaded successfully!")
    # Read the uploaded CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the first few rows of the DataFrame
    st.subheader("Data Preview")
    st.write(df.head())

    # Display summary statistics of the DataFrame
    st.subheader("Data Summary")
    st.write(df.describe())

    # Allow the user to filter data based on a selected column and value
    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    # Filter the DataFrame based on the selected column and value
    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    # Allow the user to plot data
    st.subheader("Plot Data")
    x_column = st.selectbox("Select X-axis column", columns)
    y_column = st.selectbox("Select Y-axis column", columns)

    # Generate a line chart
    if st.button("Generate plot"):
        st.line_chart(filtered_df[[x_column, y_column]].set_index(x_column))
else:
    st.write("Waiting for a file...")

