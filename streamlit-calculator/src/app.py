import streamlit as st
from utils.calculator import add, subtract, multiply, divide

def main():
    st.title("Simple Calculator")
    
    # User input for numbers
    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)
    
    # User input for operation
    operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])
    
    # Calculate and display result
    if st.button("Calculate"):
        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            if num2 != 0:
                result = divide(num1, num2)
            else:
                result = "Error: Division by zero"
        
        st.write(f"Result: {result}")

if __name__ == "__main__":
    main()