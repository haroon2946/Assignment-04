
import streamlit as st

def calculate_bmi(weight, height):
    """Calculate BMI using weight (kg) and height (m)."""
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def main():
    st.title("BMI Calculator 🏋️‍♂️")
    st.write("Calculate your Body Mass Index (BMI) easily!")

    # User Input
    weight = st.number_input("Enter your weight (kg):", min_value=1.0, format="%.2f")
    height = st.number_input("Enter your height (m):", min_value=0.5, format="%.2f")

    if st.button("Calculate BMI"):
        if height > 0:
            bmi = calculate_bmi(weight, height)
            st.success(f"Your BMI is: {bmi}")

            # BMI Category
            if bmi < 18.5:
                st.warning("You are Underweight! 🍏")
            elif 18.5 <= bmi < 24.9:
                st.success("You have a Normal weight! ✅")
            elif 25 <= bmi < 29.9:
                st.warning("You are Overweight! ⚠️")
            else:
                st.error("You are Obese! ❌")
        else:
            st.error("Height must be greater than zero.")

if __name__ == "__main__":
    main()