import streamlit as st

st.title('Price Prediction for Essential Commodities')

st.write("This app predicts the price trends of essential commodities based on historical data.")

# Example: Getting user input
commodity = st.selectbox('Select a commodity', ['Onion', 'Pulses', 'Wheat'])
days = st.slider('Days for prediction', min_value=1, max_value=30)

# Placeholder for your model code
st.write(f"Predicted price trend for {commodity} over {days} days will be displayed here.")
