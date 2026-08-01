import streamlit as st
import joblib
model=joblib.load("Employee_Attrition_model.joblib")
st.title("Employee Attrition Prediction System")
age=st.number_input("Age",min_value=18,max_value=65,value=30)