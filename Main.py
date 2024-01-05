# import library yang dibutuhkan

import streamlit as st
from web_functions import load_data  # Fix the import statement
from Tabs import Home, Predict, Visualise, Jantung, Diabetes
Tabs = {
    "Beranda": Home,
    "Jantung" : Jantung,
    "Diabetes" : Diabetes,
    "Ginjal": Predict,
    "Visualisasi": Visualise
} 

# membuat sidebar
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Select Tab", list(Tabs.keys()))


# load dataset
kidney_dataset, X, Y = load_data()  # Add parentheses to call the function

# Kondisi call app function
if page in ["Ginjal", "Visualisasi"]:
    Tabs[page].app(kidney_dataset, X, Y)

else:
    Tabs[page].app()