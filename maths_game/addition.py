# import streamlit as st 
# import random
# import pandas as pd

# st.title("Do the Addition")

# num1 = random.randint(1,20)
# num2 = random.randint(1,20)
# sum1 = num1 + num2

# def change_number():
#     st.session_state["num1"] = random.randint(1,50)
#     st.session_state["num2"] = random.randint(1,50)
    
#     return


# with st.form('Form', clear_on_submit=False):
#     st.write(num1, "+", num2)
#     inputted_idx = st.text_input('Input the number written above')
    
#     submit = st.form_submit_button('Submit')
    
#     if submit:
#       st.write(sum1)

# st.button("Next question", on_click=change_number)
    
import streamlit as st
import random

operation = st.selectbox(
    "Choose Operation to perform",
    ["add", "substract", "multiply", "divide"],
)

if "rand_num1" not in st.session_state:
    st.session_state["rand_num1"] = random.randint(0, 20)

if "rand_num2" not in st.session_state:
    st.session_state["rand_num2"] = random.randint(0, 20)

if st.toggle("Generate my numbers"): # I think this looks nicer than a checkbox here
    if st.button("Next"):
        st.session_state["rand_num1"] = random.randint(0, 20)
        st.session_state["rand_num2"] = random.randint(0, 20)
    num1 = st.session_state["rand_num1"]
    num2 = st.session_state["rand_num2"]
    
    if operation == "add":
      st.write(f"Your random numbers are: `{num1}` + `{num2}`.")
    elif operation == "substract":
      st.write(f"Your random numbers are: `{num1}` - `{num2}`.")
    elif operation == "multiply":
      st.write(f"Your random numbers are: `{num1}` X `{num2}`.")
    elif operation == "divide":
      st.write(f"Your random numbers are: `{num1}` / `{num2}`.")
    ans = st.number_input("Your answer", value=None)
      
    


else:
    num1 = st.number_input(
        "What is the first number?", min_value=0, max_value=20, key="num1"
    )
    num2 = st.number_input(
        "What is the second number?", min_value=0, max_value=20, key="num2"
    )

if st.button("submit"):
    if operation == "add":
        num = num1 + num2
        if num == ans:
          st.success("you are correct!!!")
          st.balloons()
        else:
          st.error("Wrong!!")
    elif operation == "substract":      
        num = num1 - num2
        if num == ans:
          st.success("You are correct!!!")
          st.snow()
        else:
          st.error("Wrong!!")
    elif operation == "multiply":
        num = num1 * num2
        if num == ans:
          st.success("You are correct!!!")
          st.balloons()
        else:
          st.error("Wrong!!")
    elif operation == "divide":
        num = num1 / num2
        if num == ans:
          st.success("You are correct!!!")
          st.snow()
        else:
          st.error("Wrong!!")
          

    st.write(f"Correct answer is {num}.")
