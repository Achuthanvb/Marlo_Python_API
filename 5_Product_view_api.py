import streamlit as st
import pandas as pd
from pymongo import MongoClient


client = MongoClient(
            "mongodb+srv://Marlo:Marlo123@cluster0.mqf08zz.mongodb.net/?retryWrites=true&w=majority")

db = client["Marlo_Company"]
products = db["Products"]

st.header("Products")

sorted_p=products.find().sort('rating',-1)


st.sidebar.header("Product Cart")
page_size = 2
sort_order = st.radio("Sort Order", ("High to Low", "Low to High"))

if sort_order=='Low to High':
    sort_key=1
elif sort_order=='High to Low':
    sort_key=-1

current_page = st.number_input("Current Page", min_value=1, value=1)

skip = (current_page - 1) * page_size
query = products.find().skip(skip).limit(page_size).sort('rating', sort_key)

products_lis = list(query)
for product in products_lis:
    st.write(product)
    st.write("-------------")
