import pickle
import numpy as np
import streamlit as st

# load save model
def app():
    model = pickle.load(open('penyakit_jantung.sav', 'rb'))

    st.title("Prediksi Penyakit Jantung")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Umur')
    with col2:
        sex = st.text_input('Jenis Kelamin')
    with col3:
        cp = st.text_input('Jenis Nyeri Dada')
    with col1:
        trestbps = st.text_input('Tekanan Darah')
    with col2:
        chol = st.text_input('Nilai Kolesterol')
    with col3:
        fbs = st.text_input('Gula Darah')
    with col1:
        restecg = st.text_input('Hasil Elektrokadiografi')
    with col2:
        thalach = st.text_input('Detak Jantung Maksimum')
    with col3:
        exang = st.text_input('Induksi Angina')
    with col1:
        oldpeak = st.text_input('ST Depression')
    with col2:
        slope = st.text_input('Slope')
    with col3:
        ca = st.text_input('Nilai CA')
    with col1:
        thal = st.text_input('Nilai Thal')

    # Convert user inputs to numeric values
    age = float(age) if age else 0.0
    sex = float(sex) if sex else 0.0

    # Code for prediction
    heart_diagnosis = ''

    # membuat tombol prediksi
    if st.button('Prediksi Penyakit Jantung'):
        # Convert the input values to a 2D array of numeric values
        input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]], dtype=float)

        heart_prediction = model.predict(input_data)

        if heart_prediction[0] == 1:
            heart_diagnosis = 'Pasien Terkena Penyakit Jantung'
        else:
            heart_diagnosis = 'Pasien Tidak Terkena Penyakit Jantung'

        st.success(heart_diagnosis)

# import pickle
# import streamlit as st

# # Load the diabetes model
# diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# # Set up the layout of the app
# st.title('Prediksi Penyakit Diabetes')

# col1, col2, col3 = st.columns(3)

# with col1:
#     Pregnancies = st.text_input('Pregnancies')
# with col2:
#     Glucose = st.text_input('Glucose')
# with col3:
#     BloodPressure = st.text_input('Blood Pressure')
# with col1:
#     SkinThickness = st.text_input('Skin Thickness')
# with col2:
#     Insulin = st.text_input('Insulin')
# with col3:
#     BMI = st.text_input('BMI')
# with col1:
#     DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
# with col2:
#     Age = st.text_input('Age')

# # Code for prediction
# diab_diagnosis = ''

# # Make prediction when the button is clicked
# if st.button('Prediksi Penyakit Diabetes'):
#     # Replace commas with periods and convert to float
#     input_data = [
#         float(Pregnancies.replace(',', '.')),
#         float(Glucose.replace(',', '.')),
#         float(BloodPressure.replace(',', '.')),
#         float(SkinThickness.replace(',', '.')),
#         float(Insulin.replace(',', '.')),
#         float(BMI.replace(',', '.')),
#         float(DiabetesPedigreeFunction.replace(',', '.')),
#         float(Age.replace(',', '.'))
#     ]

#     # Convert the input values to a 2D array of numeric values
#     diab_prediction = diabetes_model.predict([input_data])

#     if diab_prediction[0] == 1:
#         diab_diagnosis = 'Pasien Terkena Penyakit Diabetes'
#     else:
#         diab_diagnosis = 'Pasien Tidak Terkena Penyakit Diabetes'

#     st.success(diab_diagnosis)
