import streamlit as st
import pandas as pd

st.header("Show Data")

df=pd.read_csv("./data/adultSalary.csv")
st.write(df.head(11))

st.header("Show Chart")

import streamlit as st
import pandas as pd

df = pd.read_csv("./data/adultSalary.csv")

# show first 4 channels
st.table(df.head(4))

