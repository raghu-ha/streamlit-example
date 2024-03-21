import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))

# Sample Data (replace with your actual data)
data = {
    'date': pd.to_datetime(['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01', '2023-06-01', '2023-07-01', '2023-08-01', '2023-09-01', '2023-10-01']),
    'Overall': [50, 60, 70, 80, 65, 75, 85, 90, 80, 70],
    'Exterr': [30, 35, 40, 45, 40, 45, 50, 55, 50, 45],
    'Internal': [20, 25, 30, 35, 30, 35, 40, 45, 40, 35]}

df = pd.DataFrame(data)

# Month and Year Selection (using selectboxes)
month_options = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
selected_month = st.selectbox("Select Month:", month_options)

year_options = [2022, 2023]  # Adjust years as needed
selected_year = st.selectbox("Select Year:", year_options)

# Filter Data (assuming 'date' column for month and year)
filtered_df = df[df['date'].dt.month == month_options.index(selected_month) + 1]
filtered_df = filtered_df[df['date'].dt.year == selected_year]

# Display Report (using the filtered data)
st.header("Report")

# **Option 1: Using st.table for basic table layout**
st.table(filtered_df[['Overall', 'Exterr', 'Internal']])  # Select specific columns for display

# **Option 2: Using st.dataframe for more control (customize as needed)**
st.dataframe(filtered_df.style.set_properties(align='center'))  # Center-align table

# Additional Charts or Information (Optional)
# ... You can add more sections here to display charts or other data based on selection
