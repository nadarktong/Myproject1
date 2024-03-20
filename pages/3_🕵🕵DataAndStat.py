import streamlit as st
import pandas as pd

st.header("Show Data")

df=pd.read_csv("./data/adultSalary.csv")
st.write(df.head(10))

st.header("Show Chart")

st.line_chart(
  df, x="age", y=["workclass","education"], color=["#FF0000", "#0000FF"]  # Optional
)

st.write(df.head(200))

chart_type = "bar"
data = df.copy()

st.bar_chart(data, x="workclass", y="age")


import matplotlib.pyplot as plt
import pandas as pd

column = "workclass"
value_counts = df[column].value_counts()
fig, ax = plt.subplots(figsize=(10, 10))
ax.pie(value_counts, labels=value_counts.index, autopct='%2.2f%%', startangle=90)
plt.title("Pie Chart of " + column)
st.pyplot(fig)




