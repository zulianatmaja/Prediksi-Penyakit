import pickle
import numpy as np
import streamlit as st
def app():

    # Load the diabetes model
    diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

    # Set up the layout of the app
    st.title('Prediksi Penyakit Diabetes')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose')
    with col3:
        BloodPressure = st.text_input('Blood Pressure')
    with col1:
        SkinThickness = st.text_input('Skin Thickness')
    with col2:
        Insulin = st.text_input('Insulin')
    with col3:
        BMI = st.text_input('BMI')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
    with col2:
        Age = st.text_input('Age')

    # Code for prediction
    diab_diagnosis = ''

    # Make prediction when the button is clicked
    if st.button('Prediksi Penyakit Diabetes'):
        # Replace commas with periods and convert to float
        input_data = [
            float(Pregnancies.replace(',', '.')),
            float(Glucose.replace(',', '.')),
            float(BloodPressure.replace(',', '.')),
            float(SkinThickness.replace(',', '.')),
            float(Insulin.replace(',', '.')),
            float(BMI.replace(',', '.')),
            float(DiabetesPedigreeFunction.replace(',', '.')),
            float(Age.replace(',', '.'))
        ]

        # Convert the input values to a 2D array of numeric values
        diab_prediction = diabetes_model.predict([input_data])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'Pasien Terkena Penyakit Diabetes'
        else:
            diab_diagnosis = 'Pasien Tidak Terkena Penyakit Diabetes'

        st.success(diab_diagnosis)
