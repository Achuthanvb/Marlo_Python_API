import streamlit as st
import pandas as pd
from pymongo import MongoClient


client = MongoClient(
            "mongodb+srv://Marlo:Marlo123@cluster0.mqf08zz.mongodb.net/?retryWrites=true&w=majority")

db = client["Marlo_Company"]
products = db["Products"]


st.header("Product View")

documents = products.find({}, {'_id': False,'index':False})

  # Convert documents to a list of dictionaries
data_list = pd.DataFrame(documents)


st.write("Product detials :")


lis=[]
for i in data_list.iloc[:,0]:
    lis.append(i)

options=st.selectbox("Select Product",lis)
na=data_list.columns[0]
query = {na: options}
xx=pd.DataFrame(products.find(query,{'_id': False,'index':False}))

name=(xx.iloc[0][0])

barcode=(xx.iloc[0][1])
brand=(xx.iloc[0][2])
description=(xx.iloc[0][3])
price=(xx.iloc[0][4])
available=(xx.iloc[0][4])

c1,c2,c3=st.columns([3,1,3])
with c1:
    st.header(xx.iloc[0][0])
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')

    st.subheader('Ratings:')

    rating=st.slider("-------",min_value=0,max_value=5,step=1)
    st.subheader("Review:")
    review_cmt=st.text_area('-------',placeholder="Type review comment")

    save_rr=st.button("Save")
    
    if save_rr:
        st.session_state.Save=True
        products.update_many(query,{"$set":{"rating":rating,"Review":review_cmt}})
        st.success("Saved")


with c3:
    st.write("Brand")
    st.code(brand, language="markdown")
    st.write("Price")
    st.code(price, language="markdown")
    st.write("Description")
    st.code(description, language="markdown")
    st.write("Available")
    st.code(available, language="markdown")
    st.write("Barcode")
    st.code( barcode,language="markdown")

