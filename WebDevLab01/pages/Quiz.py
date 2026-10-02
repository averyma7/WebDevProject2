import streamlit as st
st.write("Geography Quiz!!! :)")

if "quizScore" not in st.session_state:
    st.session_state.quizScore = 0
    
#Question One

def textQ(question, answer):
    userAnswer = st.text_input(question)
    if userAnswer:
        if userAnswer.lower() == answer.lower():
            st.success("Correct!")
            st.session_state.quizScore += 1
            return True
        else:
            st.error("Incorrect.")
            return False
    return None
if textQ("What is the capital of Italy?", "Rome"):
    st.write("Yippeeee!!!")


#Question Two

def MCQ(question, choices, answer):
    st.write(question)
    choiceSelect = st.radio("Choose one:", choices) #NEW
    if st.button("Submit", key = "button1"): #NEW
        if choiceSelect == answer:
            st.success("Correct!")
            st.session_state.quizScore += 1
            return True
        else:
            st.error("Incorrect.")
            return False
        return None

options = ["Melbourne", "Kangaroo City", "Canberra", "Sydney"]
if MCQ("What is the capital of Australia?", options, "Canberra"):
    st.write("Awesome Sauce!")

#Question Three

def MultiSelect(question, options, answers):
    st.write(question)
    choiceSelect = st.multiselect("Select all that apply:", options) #NEW
    if st.button("Submit", key = "button2"):
        if set(choiceSelect) == set(answers):
            st.success("Correct!")
            st.session_state.quizScore += 1
            return True
        else:
            st.error("Incorrect.")
            return False
        return None

options = ["Ljubljana", "Tripoli", "Victoria", "Port Moresby"]
correct = ["Tripoli", "Victoria"]
if MultiSelect("Which of the following are capitals of countries in Africa?", options, correct):
    st.write("Hooray!!!")

#Question Four

def MCQ(question, choices, answer):
    st.write(question)
    choiceSelect = st.radio("Choose one:", choices)
    if st.button("Submit", key = "button3"):
        if choiceSelect == answer:
            st.success("Correct!")
            st.session_state.quizScore += 1
            return True
        else:
            st.error("Incorrect.")
            return False
        return None

options = ["Venezuela", "South Sudan", "Kiribati", "Equatorial Guinea"]
if MCQ("Which of the following countries changed their official capital in 2026?", options, "Equatorial Guinea"):
    st.write("Yayyyyy")

#Question Five 

def MultiSelect(question, options, answers):
    st.write(question)
    choiceSelect = st.multiselect("Select all that apply:", options)
    if st.button("Submit", key = "button4"):
        if set(choiceSelect) == set(answers):
            st.success("Correct!")
            st.session_state.quizScore += 1
            return True
        else:
            st.error("Incorrect.")
            return False
        return None

options = ["Bolivia", "Belarus", "Vietnam", "South Africa","Sri Lanka"]
correct = ["Bolivia", "South Africa", "Sri Lanka"]
if MultiSelect("Which of the following countries have multiple capitals?", options, correct):
    st.write("Good job!!")

if st.button("Complete Quiz", key = "button5"):
    if st.session_state.quizScore >= 4:
        st.balloons()
        st.write("Result: Geography Master!!")
    elif st.session_state.quizScore < 4:
        st.write("Result: Subpar Geography Knowledge :'(")

'''
quizScore = 0
#Question One

def textQ(question, answer):
    global quizScore
    userAnswer = st.text_input(question)
    if userAnswer:
        if userAnswer.lower() == answer.lower():
            st.success("Correct!")
            quizScore += 1
            return True
        else:
            st.error("Incorrect.")
            return False
    return None
if textQ("What is the capital of Italy?", "Rome"):
    st.write("Current score:", quizScore)


#Question Two

def MCQ(question, choices, answer):
    global quizScore
    st.write(question)
    choiceSelect = st.radio("Choose one:", choices) #NEW
    if st.button("Submit", key = "button1"): #NEW
        if choiceSelect == answer:
            st.success("Correct!")
            quizScore += 1
            return True
        else:
            st.error("Incorrect.")
            return False
        return None

options = ["Melbourne", "Kangaroo City", "Canberra", "Sydney"]
if MCQ("What is the capital of Australia?", options, "Canberra"):
    st.write("Current score:", quizScore)

#Question Three

def MultiSelect(question, options, answers):
    global quizScore
    st.write(question)
    choiceSelect = st.multiselect("Select all that apply:", options) #NEW
    if st.button("Submit", key = "button2"):
        if set(choiceSelect) == set(answers):
            st.success("Correct!")
            quizScore += 1
            return True
        else:
            st.error("Incorrect.")
            return False
        return None

options = ["Ljubljana", "Tripoli", "Victoria", "Port Moresby"]
correct = ["Tripoli", "Victoria"]
if MultiSelect("Which of the following are capitals of countries in Africa?", options, correct):
    st.write("Current score:", quizScore)

#Question Four

def MCQ(question, choices, answer):
    global quizScore
    st.write(question)
    choiceSelect = st.radio("Choose one:", choices)
    if st.button("Submit", key = "button3"):
        if choiceSelect == answer:
            st.success("Correct!")
            quizScore += 1
            return True
        else:
            st.error("Incorrect.")
            return False
        return None

options = ["Venezuela", "South Sudan", "Kiribati", "Equatorial Guinea"]
if MCQ("Which of the following countries changed their official capital in 2026?", options, "Equatorial Guinea"):
    st.write("Current score:", quizScore)

#Question Five 

def MultiSelect(question, options, answers):
    global quizScore
    st.write(question)
    choiceSelect = st.multiselect("Select all that apply:", options)
    if st.button("Submit", key = "button4"):
        if set(choiceSelect) == set(answers):
            st.success("Correct!")
            quizScore += 1
            return True
        else:
            st.error("Incorrect.")
            return False
        return None

options = ["Bolivia", "Belarus", "Vietnam", "South Africa","Sri Lanka"]
correct = ["Bolivia", "South Africa", "Sri Lanka"]
if MultiSelect("Which of the following countries have multiple capitals?", options, correct):
    st.write("Current score:", quizScore)

if quizScore >= 4:
    st.write("Result: Geography Master!!")
elif quizScore < 4:
    st.write("Result: Subpar Geography Knowledge :'(")

'''
    
    
