import streamlit as st
import pandas as pd
import plotly.express as px

chart_type = st.selectbox("Select chart type", ("bar", "pie", "line"))

df=pd.read_csv("./data/adultSalary.csv")

if chart_type == "bar":
    st.plotly_chart(
        px.bar(
            df,  
            x="sex",
            y="age",
            labels={"sex": "Sex", "age": "Age"},
            title="Bar Chart of Age by Sex"
        )
    )

elif chart_type == "pie":
    column = "sex" 
    value_counts = df[column].value_counts()  
    fig = px.pie(
        value_counts,
        labels=value_counts.index,
        values=value_counts.values,
        title="Pie Chart of Sex"
    )  
    st.plotly_chart(fig)

elif chart_type == "line":
    st.plotly_chart(
        px.line(
            df,  
            x="sex",
            y=["age", "income"],
            labels={"sex": "Sex", "age": "Age", "income": "Income"},
            color_discrete_sequence=["red", "green", "blue"],
            title="Line Chart of Age and Income by Sex"
        )
    )