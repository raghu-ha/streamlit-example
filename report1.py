import streamlit as st
import pandas as pd  # Example import for data analysis

# Sample data (replace with your actual data)
data = {"Product": ["A", "B", "C", "D"], "Sales": [100, 250, 180, 320]}
df = pd.DataFrame(data)

st.title("Report 1: Sales Analysis")

# Display a table
st.write("Sales Data")
st.dataframe(df)

# You can add charts, graphs, or other analysis elements here
st.bar_chart(df["Sales"])
