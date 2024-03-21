import streamlit as st
import pandas as pd

st.header("Show Data")

df=pd.read_csv("./data/adultSalary.csv")
st.write(df.head(10))

st.header("Show Chart")

st.write(df.head(200))

chart_type == "bar":

    # วาดแผนภูมิแท่ง
    st.bar_chart(data, x="workclass", y="age")
