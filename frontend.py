import streamlit as st 
import requests 
import pandas as pd 
import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client["ai_db"]
collection=db["ai_col"]

st.set_page_config(page_title="Ai consultant",layout="wide")

st.title("AI powered Consultation")

tab1, tab2 = st.tabs(["📝 Consultation", " Data"])

with tab1:
    st.header("Patient Information")

    with st.form("Patient_form"):
        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("enter the Name")
            age = st.number_input("Age: ",1,80)
        with col2:
            weight = st.number_input("Weight (kg)",0.0,200.0)
            his = st.text_area("Medical History")
            sym = st.text_area("Current Symptoms : ")
            sub=st.form_submit_button("Analyze patient")

        if sub:
            with st.spinner("Analysing the patient data"):
                dt = {
                    "Name": name,
                    "Age": age,
                    "Weight": weight,
                    "History": his,
                    "Symptoms": sym
                }

                res = requests.post("http://127.0.0.1:8000/predict", json=dt)
                response=res.json()
                collection.insert_one(dt)

                st.markdown("AI Insights")
                st.write(response["Ai response"])


with tab2:
    list_=list(collection.find())
    if list_:
        st.dataframe(pd.DataFrame(list_))



