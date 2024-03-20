import streamlit as st
import pandas as pd
import numpy as np

# ตัวอย่างข้อมูล
#data = pd.DataFrame({
 #   "Country": ["ภาคเหนือ", "ภาคตะวันออก", "ภาคกลาง", "ภาคตะวันตก", "ภาคใต้"],
 #  "Population": [10000, 10000, 10000, 10000],
 #   "GDP": [50000,10000 , 15000, 500000]
#})

# แสดงชื่อกราฟ
st.title("แสดงข้อมูล")

# เลือกประเภทกราฟ
chart_type = st.selectbox("เลือกประเภทกราฟ", ["bar", "pie", "line"])

# แสดงกราฟ
if chart_type == "bar":
    st.bar_chart(data, x="workclass", y="age") 
elif chart_type == "pie":
   column = "workclass"
   value_counts = df[column].value_counts()
   fig, ax = plt.subplots(figsize=(10, 10))
   explode = (0,1,0,0)
   ax.pie(value_counts, labels=value_counts.index, autopct='%1.2f%%', startangle=150, data=data)
   plt.title("Pie Chart of " + column)
   st.pyplot(fig)
elif chart_type == "line":
   st.line_chart(data, x="age", y=["workclass","education"], color=["#FF0000", "#0000FF"])
