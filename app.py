import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🏠 Boston Housing Price Prediction App")
st.write("Enter values below to get predicted housing price.")

# Input fields (you can add more if needed)
RM = st.number_input("Average number of rooms per dwelling (RM)", 0.0, 10.0, 6.0)
DIS = st.number_input("Distance to employment centers (DIS)", 0.0, 15.0, 4.0)

if st.button("Predict Price"):
    input_data = np.array([[RM, DIS]])
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted House Price: **${prediction:,.2f}**")
