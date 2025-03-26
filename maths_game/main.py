import streamlit as st 

st.set_page_config(page_title = "This is a Maths quiz") 
st.title("This is a Maths game quiz, Try to answer correctly!!!")

initial_text = "Your score..."
my_bar = st.progress(0, text=initial_text)
percent_complete = 0





answer1 = st.selectbox(":violet[**2 + 2**]", [2,3,4,6], None)

if answer1 == None:
  st.write("Please select answer!!")
elif answer1 == 4:
  
  st.success("Hurray!!!, Correct Answer")
  my_bar.progress(percent_complete + 10, text="In Progress...")
 
elif answer1 == 2 or 3 or 6:
  st.error("Sorry!!!, Wrong Answer.")
  my_bar.progress(percent_complete, text="In Progress...")
 
  

answer2 = st.selectbox(":violet[**2 + 3**]", [5,3,2,6], None)

if answer1 != None:

  if answer2 == None:
    st.write("Please select answer!!")
  elif answer2 == 5:
    
    st.success("Hurray!!!, Correct Answer")
    my_bar.progress(percent_complete + 20, text="In Progress...")
    
  elif answer2 == 2 or 3 or 6:
    st.error("Sorry!!!, Wrong Answer.")
    my_bar.progress(percent_complete + 10 , text="In Progress...")
else:
  st.write("Please solve above question to proceed...")
  
answer3 = st.selectbox(":violet[**5 + 5**]", [6,0,12,10], None)

if answer2 != None:

  if answer3 == None:
    st.write("Please select answer!!")
  elif answer3 == 10:
    
    st.success("Hurray!!!, Correct Answer")
    my_bar.progress(percent_complete + 30, text="In Progress...")
    
  elif answer3 == 6 or 0 or 12:
    st.error("Sorry!!!, Wrong Answer.")
    my_bar.progress(percent_complete + 20 , text="In Progress...")
else:
  st.write("Please solve above question to proceed...")
  
answer4 = st.selectbox(":violet[**10 + 3**]", [13,20,9,6], None)

if answer4 == None:
  st.write("Please select answer!!")
elif answer4 == 13:
  
  st.success("Hurray!!!, Correct Answer")
  my_bar.progress(percent_complete + 40, text="In Progress...")
  
elif answer4 == 20 or 9 or 6:
  st.error("Sorry!!!, Wrong Answer.")
  my_bar.progress(percent_complete + 30 , text="In Progress...")
  
answer5 = st.selectbox(":violet[**10 + 5**]", [13,15,20,8], None)

if answer5 == None:
  st.write("Please select answer!!")
elif answer5 == 15:
  
  st.success("Hurray!!!, Correct Answer")
  my_bar.progress(percent_complete + 50, text="In Progress...")
  
elif answer5 == 13 or 20 or 8:
  st.error("Sorry!!!, Wrong Answer.")
  my_bar.progress(percent_complete + 40 , text="In Progress...")
  
answer6 = st.selectbox(":violet[**10 + 8**]", [13,15,18,8], None)

if answer6 == None:
  st.write("Please select answer!!")
elif answer6 == 18:
  
  st.success("Hurray!!!, Correct Answer")
  my_bar.progress(percent_complete + 60, text="In Progress...")
  
elif answer6 == 13 or 15 or 8:
  st.error("Sorry!!!, Wrong Answer.")
  my_bar.progress(percent_complete + 50 , text="In Progress...")
  
answer7 = st.selectbox(":violet[**20 + 5**]", [25,15,28,30], None)

if answer7 == None:
  st.write("Please select answer!!")
elif answer7 == 25:
  
  st.success("Hurray!!!, Correct Answer")
  my_bar.progress(percent_complete + 70, text="In Progress...")
  
elif answer7 == 15 or 28 or 30:
  st.error("Sorry!!!, Wrong Answer.")
  my_bar.progress(percent_complete + 60 , text="In Progress...")
  
answer8 = st.selectbox(":violet[**10 + 5 + 10**]", [25,15,28,30], None)

if answer8 == None:
  st.write("Please select answer!!")
elif answer8 == 25:
  
  st.success("Hurray!!!, Correct Answer")
  my_bar.progress(percent_complete + 80, text="In Progress...")
  
elif answer8 == 15 or 28 or 30:
  st.error("Sorry!!!, Wrong Answer.")
  my_bar.progress(percent_complete + 70 , text="In Progress...")
  
answer9 = st.selectbox(":violet[**20 + 10 + 10**]", [5,45,40,30], None)

if answer9 == None:
  st.write("Please select answer!!")
elif answer9 == 40:
  
  st.success("Hurray!!!, Correct Answer")
  my_bar.progress(percent_complete + 90, text="In Progress...")
  
elif answer9 == 5 or 45 or 30:
  st.error("Sorry!!!, Wrong Answer.")
  my_bar.progress(percent_complete + 80 , text="In Progress...")
  
answer10 = st.selectbox(":violet[**20 + 10 + 5**]", [35,45,40,30], None)

if answer10 == None:
  st.write("Please select answer!!")
elif answer10 == 35:
  
  st.success("Hurray!!!, Correct Answer")
  my_bar.progress(percent_complete + 100, text="In Progress...")
  st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")
  
elif answer10 == 45 or 40 or 30:
  st.error("Sorry!!!, Wrong Answer.")
  my_bar.progress(percent_complete + 90 , text="In Progress...")
  

  

  




