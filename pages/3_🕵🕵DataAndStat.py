import streamlit as st
import pandas as pd

st.header("Show Data")

df=pd.read_csv("./data/adultSalary.csv")
st.write(df.head(11))

st.header("Show Chart")

import streamlit as st
import pandas as pd

# Load the dataframe from the CSV file
df = pd.read_csv("./data/adultSalary.csv")

# Define the list of columns to show in the table
columns = ['age', 'workclass', 'education', 'relationship']

# Display the table
st.table(df[columns])
st.write(df.head(11))
