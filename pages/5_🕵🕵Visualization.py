import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ตั้งค่าข้อมูลตัวอย่าง
df = pd.DataFrame({
    "age": [20, 25, 30, 35, 40],
    "workclass": ["Private", "Self-employed", "Private", "Private", "Self-employed"],
    "education": ["High School", "Bachelors", "Masters", "PhD", "Bachelors"],
})

# กำหนดตัวแปร
chart_type = "pie"  # เปลี่ยน "pie" เป็น "line" สำหรับแผนภูมิเส้น

# สร้างแผนภูมิ

if chart_type == "bar":

    # วาดแผนภูมิแท่ง
    st.bar_chart(data, x="workclass", y="age")

elif chart_type == "pie":

    # เลือกคอลัมน์และจำนวนข้อมูล
    column = "workclass"
    value_counts = df[column].value_counts()

    # กำหนดขนาดกราฟ
    fig, ax = plt.subplots(figsize=(10, 10))

    # วาดแผนภูมิวงกลม
    explode = (0, 1, 0, 0)
    ax.pie(value_counts, labels=value_counts.index, autopct='%1.2f%%', startangle=150)

    # ตั้งชื่อกราฟ
    plt.title("Pie Chart of " + column)

    # แสดงกราฟ
    plt.show()

elif chart_type == "line"

    # วาดแผนภูมิเส้น
    sns.lineplot(data=df, x="age", y=["workclass", "education"], color=["#FF0000", "#0000FF"])

    # ตั้งชื่อกราฟ
    plt.title("Line Chart of workclass and education vs age")

    # แสดงกราฟ
    plt.show()