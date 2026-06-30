UPI Fraud Detection System

*Project Overview
A Simple Machine Learning application built using Python, Pandas, and Scikit-learn to
detect and flag fraudulent UPI transactions. It features a complete pipeline from model
training to an interactive user interface built with Streamlit.
* File Structure
├── transactions.csv # Dataset containing transaction details
├── train_model.py # Python script to train the Random
Forest model
├── fraud_model.pkl # Saved machine learning model file
└── app.py # Streamlit web app for real-time
predictions

* Tech Stack
 Language: Python
 Data Analysis: Pandas
 Machine Learning: Scikit-learn (Random Forest Classifier)
 Web App Interface: Streamlit

*How to Run
1. Install Dependencies
pip install pandas scikit-learn streamlit joblib
2. Train the Model
Run the script to train your model using the data from transactions.csv:
python train_model.py
3. Launch the Web Application
Start the interactive dashboard where you can manually input transaction metrics and
check if they are fraudulent:
streamlit run app.py
