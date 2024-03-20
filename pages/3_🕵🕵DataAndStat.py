import streamlit as st
import pandas as pd

st.header("Show Data")

df=pd.read_csv("./data/adultSalary.csv")
st.write(df.head(10))

st.header("Show Chart")

st.line_chart(
  df, x="age", y=["workclass", "education"], color=["#FF0000", "#0000FF"]  # Optional
)

st.write(df.head(200))
