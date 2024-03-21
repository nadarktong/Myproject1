import streamlit as st
import pandas as pd

# Set up the page
st.header("Show Data")

# Load the DataFrame
df = pd.read_csv("./data/adultSalary.csv")

# Display the first 11 rows of the DataFrame
st.write(df.head(11))

st.header("Show Chart")

# Define the list of columns to show in the table
columns = ['age', 'workclass', 'education', 'relationship']

# Display the table
st.subheader("Table with 4 columns:")
st.table(df[columns].head(20))

st.subheader("Table with 20 rows:")
st.table(df.head(20))