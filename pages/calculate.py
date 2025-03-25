import streamlit as st
import time

# name = st.text_input("Enter your full Name :")
# age = st.number_input("Age : ", value=None, step=1)
# city = st.selectbox("Choose city", ("Mumbai", "Pune", "Bangalore"))
# pin = st.number_input("Enter your pincode :", value=None, step=1)

st.title("This is calculation page.")

num1 = st.number_input("1st number : ", value=None, step=1)
num2 = st.number_input("2nd number : ", value=None, step=1)
num3 = st.number_input("3rd number : ", value=None, step=1)



but = st.button("Addition")
if but:
  sum = num1 + num2 + num3
  st.write(num1, "+", num2, "+", num3, "=", sum)
  st.write("Addition of all 3 numbers is: ", num1 + num2 + num3)
  st.markdown("![Alt Text](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjMyNXZwMzloYjRwdnN5bzVscXJmcDVyMTJiOHgwc24ya3RoN2loYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/MelhioWPAo6k4Q6BTp/giphy.gif)")
  
but1 = st.button("Substraction")
if but1:
  sub1 = num1-num2-num3
  sub2 = num2-num3-num1
  sub3 = num3-num1-num2
  
  if sub1 >= 0:
    st.write(num1, "-", num2, "-", num3, "=", sub1)
    st.write("Substraction of all 3 numbers is: ", sub1)
    st.markdown("![Alt Text](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjMyNXZwMzloYjRwdnN5bzVscXJmcDVyMTJiOHgwc24ya3RoN2loYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/MelhioWPAo6k4Q6BTp/giphy.gif)")
  
  elif sub2 >= 0:
    st.write(num2, "-", num3, "-", num1, "=", sub2)
    st.write("Substraction of all 3 numbers is: ", sub2)
    st.markdown("![Alt Text](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjMyNXZwMzloYjRwdnN5bzVscXJmcDVyMTJiOHgwc24ya3RoN2loYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/MelhioWPAo6k4Q6BTp/giphy.gif)")
    
  elif sub3 >= 0:
    st.write(num3, "-", num1, "-", num2, "=", sub3)
    st.write("Substraction of all 3 numbers is: ", sub3)
    st.markdown("![Alt Text](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjMyNXZwMzloYjRwdnN5bzVscXJmcDVyMTJiOHgwc24ya3RoN2loYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/MelhioWPAo6k4Q6BTp/giphy.gif)")
    
  else:
    st.write("Result is in negative figure!!!")
  
  # st.write("Substraction of all 3 numbers is: ", num2 - num1 - num3)
  # st.write("Substraction of all 3 numbers is: ", num3 - num2 - num1)
  
but2 = st.button("Multiplication")
if but2:
  mul = num1 * num2 * num3
  st.write(num1, "X", num2, "X", num3, "=", mul)
  st.write("Multiplication of all 3 numbers is: ", mul)
  st.markdown("![Alt Text](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjMyNXZwMzloYjRwdnN5bzVscXJmcDVyMTJiOHgwc24ya3RoN2loYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/MelhioWPAo6k4Q6BTp/giphy.gif)")
  

  