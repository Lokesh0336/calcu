import streamlit as st

st.title('Calculator')

num1 = st.number_input('Enter first number', value=0)
num2 = st.number_input('Enter second number', value=0)
operation = st.selectbox('Select operation', ['+', '-', '*', '/'])

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2 if num2 != 0 else 'Error: Division by zero'

st.write(f'Result: {result}')

