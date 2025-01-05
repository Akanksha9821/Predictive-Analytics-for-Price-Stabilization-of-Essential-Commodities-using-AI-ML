# Predictive Analytics for Price Stabilization of Essential Commodities using AI/ML

This repository contains a predictive analytics solution aimed at stabilizing the prices of essential commodities using advanced AI/ML techniques. The project leverages time series forecasting models like **PMD ARIMA** and **Prophet** for accurate commodity price predictions and a Streamlit-based web application for user interaction.

---

## Features
- **Machine Learning Models:**  
  - **PMD ARIMA**: Automatically optimizes ARIMA hyperparameters for accurate time series forecasting.  
  - **Prophet**: A robust forecasting model designed for seasonal trends and long-term predictions.  
- **Interactive Web App:** User-friendly interface powered by Streamlit (`app2.py`).  
- **Price Trends Analysis:** Insights and visualizations to aid in stabilizing commodity prices.  

---

## Folder Structure
- **`app2.py`**: Streamlit application for interaction with the predictive models.  
- **`trained_model.zip`**: Contains the pretrained models and associated files.  

---

## Requirements
- Python 3.7 or later  
- Required libraries:  
  - `streamlit`  
  - `pandas`  
  - `numpy`  
  - `pmdarima`  
  - `prophet` (formerly `fbprophet`)  
  - Any other dependencies specified in your project  





## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/Predictive-Analytics-for-Price-Stabilization.git
cd Predictive-Analytics-for-Price-Stabilization
```
### 2. Set Up the Environment

Install the necessary dependencies:

### 3. Extract the Model

Unzip the `trained_model.zip` into the project directory. Ensure the models are accessible in the same folder as `app2.py`.

### 4. Run the Application

Start the Streamlit app:

```bash
streamlit run app2.py
```
