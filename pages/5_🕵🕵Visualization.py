import streamlit as st
import pandas as pd
import numpy as np

# กำหนดค่าตัวแปร chart_type ด้วย selectbox เพื่อให้ผู้ใช้เลือกประเภทแผนภูมิ
chart_type = st.selectbox("เลือกประเภทแผนภูมิ", ("bar", "pie", "line"))

# โหลดข้อมูล DataFrame (หากยังไม่ได้กำหนดก่อนหน้านี้ ให้ระบุวิธีการโหลดข้อมูล)
df=pd.read_csv("./data/adultSalary.csv")# ... (เช่น อ่านจากไฟล์ CSV ด้วย pd.read_csv())

# ส่วนการสร้างแผนภูมิตามประเภทที่เลือก
if chart_type == "bar":
    st.bar_chart(
        df,  # ให้ใช้ DataFrame โดยตรง
        x="workclass",
        y="age",
        width=600,
        height=400,
        title="Bar Chart of Age by Workclass"
    )

elif chart_type == "pie":
    column = "workclass"  # กำหนดชื่อคอลัมน์สำหรับ Pie Chart
    value_counts = df[column].value_counts()  # ใช้ DataFrame โดยตรง
    fig, ax = plt.subplots(figsize=(8, 8))
    explode = (0, 1, 0, 0)
    ax.pie(
        value_counts,
        labels=value_counts.index,
        autopct='%1.2f%%',
        startangle=150
    )  # ไม่ต้องใส่ argument data
    plt.title("Pie Chart of " + column)
    st.pyplot(fig)

elif chart_type == "line":
    st.line_chart(
        df,  # ให้ใช้ DataFrame โดยตรง
        x="age",
        y=["workclass", "education"],
        hue=["workclass", "education"],  # ใช้ hue เพื่อกำหนดสีตามกลุ่ม
        legend="full"  # แสดง legend
    )

