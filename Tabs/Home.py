import streamlit as st

def app():
    # Judul halaman aplikasi
    st.title("Aplikasi Prediksi Penyakit")

    # Add your content and functionality here
    st.write("Selamat datang di aplikasi Prediksi penyakit. Anda dapat melakukan Prediksi Penyakit Jantung, Diabetes, dan Ginjal.")
    
    # You can include various Streamlit components like st.text_input, st.button, st.plot, etc. based on your application logic.
    # Example:
    user_input = st.text_input("Masukkan data pengguna:", "")
    if st.button("Proses"):
        st.write("Hasil prediksi:", predict_disease(user_input))  # Replace with your actual prediction logic

# Function to simulate the prediction logic
def predict_disease(user_input):
    # Replace this with your actual prediction logic
    # This is just a placeholder
    return f"Prediksi untuk input '{user_input}'"
