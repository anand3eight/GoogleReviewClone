import streamlit as st
import signup
import DBEntry

def loginWindow() :
    x = st.empty()
    with x.form(key='login_page'):
        st.write("<h2 align=center>LOGIN</h2>", unsafe_allow_html=True)
        username = st.text_input("Username : ")
        password = st.text_input("Password : ", type="password")
        signIn = st.form_submit_button(label='Sign In', use_container_width=True)
        signUp = st.form_submit_button(label='New User, Sign Up', use_container_width=True)
    if signIn:
        if username != "":
            if len(password) > 7 :
                st.error("Login Successful")
            else :
                st.error("Invalid Password")
        else :
            st.error("Invalid Username")
    if signUp :
            x.empty()
            signup.signupWindow()


if __name__ == "__main__" :
    loginWindow()

