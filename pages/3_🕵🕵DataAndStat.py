import streamlit as st
import pandas as pd

st.header("Show Data")

df=pd.read_csv("./data/Most Popular Naruto Characters.csv")
st.write(df.head(10))

st.header("Show Chart")

st.line_chart(
   df, x="published_at", "updated_at", y=["author"], color=["#FF0000", "#0000FF"]  # Optional
)
st.write(df.head(200))

import matplotlib.pyplot as plt

data = {'Category': ['A', 'B', 'C', 'D'],
        'Values': [25, 18, 32, 22]}

plt.bar(data['Category'], data['Values'])
plt.xlabel('Category')
plt.ylabel('Values')
plt.title('Bar Graph')
plt.show()