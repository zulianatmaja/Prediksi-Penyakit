import warnings
import matplotlib.pyplot as plt
import seaborn as sns  # Import seaborn
from sklearn.metrics import confusion_matrix
from sklearn import tree
import streamlit as st

from web_functions import train_model

def app(kidney_dataset, X, Y):  # Removed 'self' parameter

    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.title("Visualisasi Prediksi Penyakit Ginjal")

    if st.checkbox("Plot Confusion Matrix"):
        model, score = train_model(X, Y)
        cm = confusion_matrix(Y, model.predict(X))
        plt.figure(figsize=(10, 6))
        sns.heatmap(cm, annot=True, fmt='g', cmap='Blues', xticklabels=['nockd', 'ckd'], yticklabels=['nockd', 'ckd'])
        st.pyplot()

    if st.checkbox("Plot Decision Tree"):
        model, score = train_model(X, Y)
        dot_data = tree.export_graphviz(
            decision_tree=model, max_depth=4, out_file=None, filled=True, rounded=True,
            feature_names=X.columns, class_names=['nockd', 'ckd']
        )

        st.graphviz_chart(dot_data)
