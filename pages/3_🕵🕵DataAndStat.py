import streamlit as st
import pandas as pd

st.header("Show Data")

df=pd.read_csv("./data/Most Popular Naruto Characters.csv")
st.write(df.head(10))

st.header("Show Chart")

st.line_chart(
   df, x="stock_index_price", y=["interest_rate", "unemployment_rate"], color=["#FF0000", "#0000FF"]  # Optional
)