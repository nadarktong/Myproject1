import streamlit as st
import pandas as pd
import plotly.express as px

chart_type = st.selectbox("เลือกประเภทแผนภูมิ", ("bar", "pie", "line"))

df=pd.read_csv("./data/adultSalary.csv")
df['workclass'] = df['workclass'].astype('category')

if chart_type == "bar":
    st.plotly_chart(
        px.bar(
            df,  
            x="workclass",
            y="age",
            labels={"workclass": "Workclass", "age": "Age"},
            title="Bar Chart of Age by Workclass"
        )
    )

elif chart_type == "pie":
    column = "workclass" 
    value_counts = df[column].value_counts()  
    fig = px.pie(
        value_counts,
        labels=value_counts.index,
        values=value_counts.values,
        title="Pie Chart of " + column
    )  
    st.plotly_chart(fig)

elif chart_type == "line":
    st.plotly_chart(
        px.line(
            df,  
            x="age",
            y=["workclass", "relationship"],
            labels={"age": "Age", "workclass": "Workclass", "relationship": "relationship"},
            color_discrete_sequence=["red", "green"],
            title="Line Chart of Age and Relationship by Workclass"
        )
    )