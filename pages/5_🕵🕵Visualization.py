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
elif chart_type == "pie":

    # เลือกคอลัมน์และจำนวนข้อมูล
    column = "workclass"
    value_counts = df[column].value_counts()

    # กำหนดขนาดกราฟ
    fig, ax = plt.subplots(figsize=(10, 10))

    # วาดแผนภูมิวงกลม
    explode = (0, 1, 0, 0)
    ax.pie(value_counts, labels=value_counts.index, autopct='%1.2f%%', startangle=150, data=data)

    # ตั้งชื่อกราฟ
    plt.title("Pie Chart of " + column)

    # แสดงกราฟ
    plt.show()

elif chart_type == "line":

    # วาดแผนภูมิเส้น
    sns.lineplot(data=df, x="age", y=["workclass", "education"], color=["#FF0000", "#0000FF"])

    # ตั้งชื่อกราฟ
    plt.title("Line Chart of workclass and education vs age")

    # แสดงกราฟ
    plt.show()