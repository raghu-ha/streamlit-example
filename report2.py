import streamlit as st
import matplotlib.pyplot as plt  # Example import for plotting

# Sample data (replace with your actual data)
x = [1, 2, 3, 4, 5]
y = [4, 6, 5, 8, 2]

st.title("Report 2: Line Chart Example")

# Create a line chart
plt.figure(figsize=(8, 5))
plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sample Line Chart")
plt.grid(True)

# Convert Matplotlib chart to Streamlit image
st.image(plt.gcf())
