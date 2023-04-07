import streamlit as st
import time
import login
import DBEntry

def signupWindow() :
    x = st.empty()
    with x.form(key='signup_page'):
        st.write("<h2 align = center>SIGN UP</h2>", unsafe_allow_html=True)
        name = st.text_input("Name : ")
        country = st.text_input("Country : ")
        username = st.text_input("Username : ")
        password = st.text_input("Password : ", type="password")
        confirm_password = st.text_input("Confirm Password : ", type="password")
        signUp = st.form_submit_button(label='Sign Up', use_container_width=True)

    if signUp :
        if name == "" :
            st.error("Invalid Name")
        elif country == "" :
            st.error("Invalid Country")
        elif username == "" :
            st.error("Invalid Username")
        elif len(password) < 8 or password != confirm_password :
            st.error("Re-Enter Password")
        else :
            user = dict()
            user["Name"] = name
            user["Country"] = country
            user["Username"] = username
            user["Password"] = password
            DBEntry.insertUser(user)
            x.error("Signup Successful, Redirecting to Login Page")
            time.sleep(3)
            x.empty()
            login.loginWindow()


if __name__ == "__main__" :
    signupWindow()