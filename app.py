import streamlit as st
import time

# name = st.text_input("Enter your full Name :")
# age = st.number_input("Age : ", value=None, step=1)
# city = st.selectbox("Choose city", ("Mumbai", "Pune", "Bangalore"))
# pin = st.number_input("Enter your pincode :", value=None, step=1)

num1 = st.number_input("1st number : ", value=None, step=1)
num2 = st.number_input("2nd number : ", value=None, step=1)
num3 = st.number_input("3rd number : ", value=None, step=1)



but = st.button("Addition")
if but:
  st.write("Addition of all 3 numbers is: ", num1 + num2 + num3)
  
but1 = st.button("Substraction")
if but1:
  st.write("Substraction of all 3 numbers is: ", num1 - num2 - num3)
  
but2 = st.button("Multiplication")
if but2:
  st.write("Multiplication of all 3 numbers is: ", num1 * num2 * num3)