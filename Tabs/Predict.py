import streamlit as st
from web_functions import predict

def app( kidney_dataset, X, Y):
    st.title("Prediksi Penyakit Ginjal")

    col1, col2, col3 = st.columns(3)

    with col1:
        bp = st.text_input ('blood pressure')
        sg = st.text_input ('specific gravity')
        al = st.text_input ('albumin')
        su = st.text_input ('sugar')
        rbc = st.text_input ('red blood cells')
        pc = st.text_input ('pus cell')
        pcc = st.text_input ('pus cell clumps')
        ba = st.text_input ('bacteria')
    with col2:
        bgr = st.text_input ('blood glucose random')
        bu = st.text_input ('blood urea')
        sc = st.text_input ('serum creatinine')
        sod = st.text_input ('sodium')
        pot = st.text_input ('potassium')
        hemo = st.text_input ('hemoglobin')
        pcv = st.text_input ('packed cell volume')
        wc = st.text_input ('white blood cell count')
    with col3:
        rc = st.text_input ('red blood cell count')
        htn = st.text_input ('hypertension')
        dm = st.text_input ('diabetes mellitus')
        cad = st.text_input ('coronary artery disease')
        appet = st.text_input ('appetite')
        pe = st.text_input ('pedal edema')
        ane = st.text_input ('anemia')

    features = [bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe, ane]

    # Tombol Prediksi
    if st.button("Prediksi Penyakit Ginjal"):
        prediction, score = predict(X, Y, features)
        score = score
        st.info("Prediksi Sukses...")

        if prediction == 1:
            st.warning("Orang tersebut rentan terkena penyakit Ginjal")
        else:
            st.success("Orang tersebut relatif aman dari penyakit Ginjal")

        st.write("Model yang digunakan memiliki tingkat akurasi", (score*100), "%")

# Sample usage
# df, X, Y = ...  # You need to define df, X, and Y
# app(df, X, Y)
