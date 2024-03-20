import streamlit as st
import pandas as pd
import numpy as np

# ตัวอย่างข้อมูล
data = pd.DataFrame({
"workclass": ["Private", "Private", "Private", "Government", "Private"],
"age": [30, 35, 40, 45, 50]
})

# แสดงชื่อกราฟ
st.title("กราฟแท่งแสดงอายุเฉลี่ยในแต่ละประเภทอาชีพ")

# เลือกประเภทกราฟ
chart_type = st.selectbox("เลือกประเภทกราฟ", ["bar", "pie", "line"])

# แสดงกราฟ
if chart_type == "bar":
    st.bar_chart(data, x="workclass", y="age")
if chart_type == "pie":
    column = "workclass"

    if not df["workclass"].empty:
        value_counts = pd.Categorical(df[column]).value_counts()
        fig, ax = plt.subplots(figsize=(10, 10))
        explode = (0, 1, 0, 0)  # Adjust slice explosion if needed
        ax.pie(value_counts, labels=value_counts.index, startangle=150, autopct=lambda pct: f'{pct:.1f}%')  # Format percentage string (optional)
        plt.title("Pie Chart of " + column)
        st.pyplot(fig)
    else:
        st.write