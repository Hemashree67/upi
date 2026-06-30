import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("fraud_model.pkl")

# App Title
st.title("UPI Fraud Detection System")

st.write("Enter transaction details below")

# Inputs
transaction_id = st.text_input(
    "Transaction ID",
    placeholder="Example: TXN123456"
)

sender_upi = st.text_input(
    "Sender UPI ID",
    placeholder="Example: rahul@upi"
)

receiver_upi = st.text_input(
    "Receiver UPI ID",
    placeholder="Example: store@paytm"
)

amount = st.text_input(
    "Transaction Amount (₹)",
    placeholder="Correct: 5000 | Wrong: five thousand"
)

transaction_time = st.text_input(
    "Transaction Hour",
    placeholder="Correct: 14 | Wrong: two pm"
)

device = st.selectbox(
    "Device Type",
    ["Android", "iPhone", "Laptop", "Unknown"]
)

location = st.selectbox(
    "Location",
    ["Bangalore", "Delhi", "Mumbai", "Chennai", "Unknown"]
)

# Convert categorical values into numbers
device_map = {
    "Android": 0,
    "iPhone": 1,
    "Laptop": 2,
    "Unknown": 3
}

location_map = {
    "Bangalore": 0,
    "Delhi": 1,
    "Mumbai": 2,
    "Chennai": 3,
    "Unknown": 4
}

# Prediction Button
if st.button("Check Fraud"):

    try:

        # Convert inputs
        amount_value = float(amount)
        time_value = int(transaction_time)

        # Validate hour
        if time_value < 0 or time_value > 23:
            st.error("Transaction Hour must be between 0 and 23")
        
        else:

            # Features for model
            features = np.array([[
                amount_value,
                time_value,
                device_map[device],
                location_map[location]
            ]])

            # Prediction
            prediction = model.predict(features)

            # Show details
            st.subheader("Transaction Details")

            st.write(f"Transaction ID: {transaction_id}")
            st.write(f"Sender UPI: {sender_upi}")
            st.write(f"Receiver UPI: {receiver_upi}")
            st.write(f"Amount: ₹{amount}")
            st.write(f"Transaction Hour: {transaction_time}")
            st.write(f"Device: {device}")
            st.write(f"Location: {location}")

            # Result
            if prediction[0] == 1:
                st.error("⚠ Fraudulent Transaction Detected!")
            else:
                st.success("✅ Safe Transaction")

    except:

        st.error("""
Invalid Input!

Correct Examples:
- Amount → 5000
- Transaction Hour → 14

Wrong Examples:
- Amount → five thousand
- Transaction Hour → two pm
""")