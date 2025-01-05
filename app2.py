# Import libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Title and Description
st.title("Predictive Analytics for Price Stabilization")
st.write("""
This platform forecasts the prices of essential food commodities using historical data and machine learning models.
""")

# Mock Dataset Creation
st.subheader("Sample Data")
data = pd.DataFrame({
    "Date": pd.date_range(start="2023-01-01", periods=100),
    "Commodity": np.random.choice(["Pulses", "Onions"], size=100),
    "Price": np.random.uniform(50, 200, size=100),
})
data["Date"] = pd.to_datetime(data["Date"])

# Display Dataset
st.write("Here is the sample data:")
st.write(data.head())

# User Input for Commodity Selection
st.sidebar.header("User Input")
selected_commodity = st.sidebar.selectbox(
    "Select a commodity to analyze:", 
    data["Commodity"].unique()
)

# Filter Data Based on Selection
filtered_data = data[data["Commodity"] == selected_commodity]

# Plot Price Trends
st.subheader(f"Price Trends for {selected_commodity}")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(filtered_data["Date"], filtered_data["Price"], label="Price")
ax.set_title(f"{selected_commodity} Price Trends")
ax.set_xlabel("Date")
ax.set_ylabel("Price")
ax.legend()
st.pyplot(fig)

# Predictive Analytics Placeholder
st.subheader("Price Prediction")
st.write("""
Using AI/ML models like ARIMA or LSTM, we predict the price for the next period. Below is a mock prediction:
""")
next_price = filtered_data["Price"].iloc[-1] * 1.05  # Mock prediction
st.write(f"Predicted price for the next period: **₹{next_price:.2f}**")

# Intervention Recommendation
st.subheader("Market Intervention Recommendations")
st.write("""
Based on predicted price trends, here are some recommendations for market interventions:
""")
if next_price > 150:
    st.write("- Release buffer stocks to stabilize prices.")
    st.write("- Monitor supply chain and reduce bottlenecks.")
else:
    st.write("- Maintain current stock levels.")
    st.write("- Promote production through subsidies.")

# Add Pictures (Optional)
st.sidebar.header("Add Pictures")
upload_image = st.sidebar.file_uploader("Upload a picture (optional)", type=["png", "jpg", "jpeg"])
if upload_image:
    st.image(upload_image, caption="Uploaded Image", use_column_width=True)
