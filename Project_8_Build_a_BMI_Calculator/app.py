
import streamlit as st

st.title("BMI Calculator")

# Input sliders for height and weight
height = st.slider("Enter your height (in cm):", 100, 250, 175)
weight = st.slider("Enter your weight (in kg):", 40, 200, 70)

# Calculate BMI
bmi = weight / ((height / 100) ** 2)

# Display BMI
st.write(f"Your BMI is {bmi:.2f}")

# BMI categories
st.write("### BMI Categories")
st.write("- Underweight: BMI is less than 18.5")
st.write("- Normal weight: BMI is between 18.5 and 24.9")
st.write("- Overweight: BMI is between 25 and 29.9")
st.write("- Obesity: BMI is 30 or greater")
