import streamlit as st

# Streamlit App Title
st.set_page_config(page_title="Calculator App", page_icon="🧮")
st.title("🧮 Simple Calculator")
st.write("A basic calculator built with Streamlit")

# Input Fields
num1 = st.number_input("Enter first number", value=0.0, step=1.0)
num2 = st.number_input("Enter second number", value=0.0, step=1.0)

# Operation Selection
operation = st.selectbox("Select Operation", ("Addition", "Subtraction", "Multiplication", "Division"))

# Calculation
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"The result of addition is: {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"The result of subtraction is: {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"The result of multiplication is: {result}")
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.success(f"The result of division is: {result}")
        else:
            st.error("Error: Division by zero is not allowed!")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
