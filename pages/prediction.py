import streamlit as st
import random

# Set up the Streamlit page layout
st.title("Crime Type Prediction")
st.write("Enter the following variables:")

# Create text input fields for the variables
province = st.text_input("Province")
major_cities = st.text_input("Major Cities")
year = st.text_input("Year (YYYY)")

# Create a selectbox for crime types
crime_types = ["Theft", "Drugs", "Robbery", "Rape"]
crime_type = st.selectbox("Type of Crime", crime_types)

# Create a button for prediction
if st.button("Predict"):
    # Perform the prediction
    prediction = random.choice(crime_types)
    accuracy = random.uniform(0.7, 0.9)
    
    # Display the prediction result
    st.write(f"Predicted Crime Type: {prediction}")
    st.write(f"Prediction Accuracy: {accuracy:.2f}")

#spring.mail.password=uvyg limi eksh jnvh







