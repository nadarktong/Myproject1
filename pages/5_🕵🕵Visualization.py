import streamlit as st
import pandas as pd


# ตัวอย่างข้อมูล
data = pd.DataFrame({
    "Country": ["ไทย", "อเมริกา", "จีน", "ญี่ปุ่น"],
    "Population": [70000000, 330000000, 1400000000, 125000000],
    "GDP": [500000000000, 25000000000000, 15000000000000, 5000000000000]
})

import matplotlib.pyplot as plt
# แสดงชื่อกราฟ
st.title("ข้อมูลประเทศ")

# เลือกประเภทกราฟ
chart_type = st.selectbox("เลือกประเภทกราฟ", ["bar", "pie", "line", "scatter"])

# แสดงกราฟ
if chart_type == "bar":
    st.bar_chart(data, x="Country", y="Population")
elif chart_type == "pie":
    labels = "ไทย", "อเมริกา", "จีน", "ญี่ปุ่น"
    sizes =  [70000000, 330000000, 1400000000, 125000000]
    explode = (0, 0.1,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    st.pyplot(fig1)
elif chart_type == "line":
    st.line_chart(data, x="Country", y="Population")


# แสดงข้อมูล GDP
st.write("ข้อมูล GDP")
st.table(data[["Country", "GDP"]])
