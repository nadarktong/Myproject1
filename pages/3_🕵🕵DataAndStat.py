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

def bar_chart(
      self,
      data: Data = None,
      *,
      x: str | None = None,
      y: str | Sequence[str] | None = None,
      color: str | Color | list[Color] | None = None,
      width: int = 0,
      height: int = 0,
      use_container_width: bool = True,
) -> DeltaGenerator:
