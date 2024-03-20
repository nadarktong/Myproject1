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

import seaborn as sns
import matplotlib.pyplot as plt

# Bar graph
plt.figure(figsize=(8, 6))
sns.barplot(x='day', y='total_bill', data=tips)
plt.xlabel('Day')
plt.ylabel('Total Bill')
plt.title('Bar Graph')
plt.show()

# Pie graph
plt.figure(figsize=(8, 6))
sns.countplot(x='day', data=tips)
plt.title('Pie Graph')
plt.pie(tips['day'].value_counts(), labels=tips['day'].unique(), autopct='%1.1f%%')
plt.show()

# Line graph
plt.figure(figsize=(8, 6))
sns.lineplot(x='total_bill', y='tip', data=tips)
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.title('Line Graph')
plt.show()

# Boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x=tips['total_bill'])
plt.title('Boxplot')
plt.show()