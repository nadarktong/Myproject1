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

chart_type = "bar"
data = df.copy()

st.bar_chart(data, x="sex", y="income")

import matplotlib.pyplot as plt
import pandas as pd

# เลือกคอลัมน์ที่ต้องการแสดง
column = "workclass"

# แยกข้อมูลตามคอลัมน์
value_counts = df[column].value_counts()

# กำหนดขนาดกราฟ
fig, ax = plt.subplots(figsize=(10, 10))

# วาดกราฟวงกลม
ax.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=90)

# เพิ่มชื่อกราฟ
plt.title("Pie Chart of " + column)

# แสดงกราฟบน Streamlit
st.pyplot(fig)



import matplotlib.pyplot as plt
import pandas as pd

# โหลดไฟล์ CSV
df = pd.read_csv("./data/adultSalary.csv")

# เลือกคอลัมน์
columns = ["age", "workclass", "salary"]

# แยกข้อมูลตามประเภทของงาน
df_grouped = df.groupby("workclass")

# วาดกราฟเส้นสำหรับแต่ละประเภทของงาน
for workclass, df_workclass in df_grouped:
  plt.plot(df_workclass["age_column"], df_workclass["salary_column"], label=workclass)


# เพิ่มชื่อกราฟ
plt.title("Line Chart of Age vs Salary by Workclass")

# เพิ่ม labels แกน x และ y
plt.xlabel("Age")
plt.ylabel("Salary")

# เพิ่ม legend
plt.legend()

# แสดงกราฟบน Streamlit
st.pyplot(fig)

