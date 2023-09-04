import streamlit as st
import streamlit_authenticator as stauth
from pymongo import MongoClient
import connect
import bcrypt

client = MongoClient("mongodb+srv://Marlo:Marlo123@cluster0.mqf08zz.mongodb.net/?retryWrites=true&w=majority")  # Replace with your MongoDB URI
db = client["Marlo_Company"]
user_credential = db["user_credential"]
admin_credential = db["admin_credential"]
products = db["Products"]


#st.set_page_config(page_title='Page1',layout='wide')



def email_check(email):
    if '@' not in email:
        return False
    domain=email.split("@")[1]
    if domain!='marlo.com' :
        return False
    else:return True

def verify_password(entered_password, stored_hashed_password):
    return bcrypt.checkpw(entered_password.encode('utf-8'), stored_hashed_password)



st.header("Welcome")
method=st.selectbox('Choose Login method',('User Login','Admin Login'))
if method=='User Login':
    c1,c2=st.columns(2)
    with c1:
        st.write("If already having Account , :green[SIGNIN]")
    with c2:
        st.write("Want to Create account , :red[SIGNUP]")

    tab1,tab2=st.tabs(['signin','signup'])
    with tab1:
        email = st.text_input('Email', placeholder='Enter your EmailId')
        password = st.text_input('Password', placeholder='Enter your password', type='password')



        #st.write(hashed_passwords)
        login=st.button("Login")
        if login:
            user_data = user_credential.find_one({"email_id": email, "password": password})
            if user_data:
                st.success("Login successful!")

            else:
                st.error("Invalid credentials. Please try again.")
    with tab2:
        with st.form(key='tab2', clear_on_submit=True):
            email_new = st.text_input('EmailID', placeholder='Enter your EmailId')
            username_new = st.text_input('FirstName', placeholder='Enter your username')
            password1 = st.text_input('Password1', placeholder='Enter your password', type='password')
            password2 = st.text_input('Confirm Password', placeholder='Confirm your password', type='password')


            Create_Account = st.form_submit_button("Create Account")



        if Create_Account:
            if password1 == password2 and email_check(email_new):
                user_data = {
                    'email_id':email_new,
                    "user_name": username_new,
                    "password": password1,
                }
                # Check if the user already exists
                if user_credential.find_one({"email_id": email_new}):
                    st.error("User already exists!")
                else:
                    # Insert the new user into MongoDB
                    user_credential.insert_one(user_data)
                    st.success("Registration successful!")
                    st.write('Now..You can SignIn..!')
            else:
                st.error("Email is incorrect or Passwords do not match!")








elif method=='Admin Login':
    st.write("Admin Mode")
    email = st.text_input('Email', placeholder='Enter your EmailId')
    password = st.text_input('Password', placeholder='Enter your password', type='password')

    # st.write(hashed_passwords)
    login = st.button("Login")
    if login:
        user_data = admin_credential.find_one({"ad_email": email, "password": password})
        if user_data:
            st.success("Login successful!")

        else:
            st.error("Invalid credentials. Please try again.")

