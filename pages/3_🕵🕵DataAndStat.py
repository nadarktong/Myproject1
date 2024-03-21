import streamlit as st
import pandas as pd

st.header("Show Data")

df = pd.read_csv("./data/adultSalary.csv")

st.write(df.head(11))

st.header("Show Chart")

columns = ['age', 'workclass', 'education', 'relationship']

st.subheader("Table with 4 columns:")
st.table(df[columns].head(20))
