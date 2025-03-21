import streamlit as st
import time

name = st.text_input("Enter your full Name :")
age = st.number_input("Age : ", value=None, step=1)
city = st.selectbox("Choose city", ("Mumbai", "Pune", "Bangalore"))
pin = st.number_input("Enter your pincode :", value=None, step=1)

but = st.button("Submit")
if but:
  st.markdown(f""" 
  Name : {name}\n
  Age : {age}\n
  City : {city}\n
  Pincode : {pin}           
              """)