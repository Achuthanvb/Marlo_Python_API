import streamlit as st
import pandas as pd
from pymongo import MongoClient


client = MongoClient(
            "mongodb+srv://Marlo:Marlo123@cluster0.mqf08zz.mongodb.net/?retryWrites=true&w=majority")

db = client["Marlo_Company"]
products = db["Products"]


# Using object notation
with st.sidebar:
    page=st.selectbox("",['HOME','OPERATIONS'])
if page=='HOME':
    st.header("Welcome..!")
    st.subheader("You have logged in as admin..")
if page=='OPERATIONS':
    op=st.selectbox("Choose a operation",['Insert','Retrive','Delete'])

    if op=='Insert':
        uploaded_file = st.file_uploader("Choose a file")
        # Can be used wherever a "file-like" object is accepted:
        if uploaded_file==None:
            st.write("Upload the product detials")
        else:
            st.write("Uploaded")
            df=pd.read_csv(uploaded_file)
            st.dataframe(df)
        insert_button=st.button('Insert')
        if insert_button:
            # converting the dataframe into dictionary data
            df.reset_index(inplace=True)
            data_dict = df.to_dict("records")

            products.insert_many(data_dict)
            st.success("Data Saved")
    if op=='Retrive':
        if st.button("Show"):
            documents = products.find({}, {'_id': False,'index':False})

            # Convert documents to a list of dictionaries
            data_list = list(documents)

            # Display the data in a Streamlit table
            st.write("Product detials :")
            st.table(data_list)
