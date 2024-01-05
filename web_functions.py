## Import modul yang akan digunakan
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier  # Correct import statement
import streamlit as st

@st.cache_resource
def load_data(): 

    # Load dataset
    kidney_dataset = pd.read_csv('kidney-sudah-clean.csv')

    X = kidney_dataset[["bp","sg","al","su","rbc","pc","pcc","ba","bgr","bu","sc","sod","pot","hemo","pcv","wc","rc","htn","dm","cad","appet","pe","ane"]]  # Use kidney_dataset instead of df
    Y = kidney_dataset[['classification']]

    return kidney_dataset, X, Y  # Return kidney_dataset instead of df

@st.cache_resource
def train_model(X, Y):  # Change the function parameters to match the return values of load_data
    model = DecisionTreeClassifier(
        ccp_alpha=0.0, class_weight=None, criterion='entropy',
        max_depth=4, max_features=None, max_leaf_nodes=None,
        min_impurity_decrease=0.0, min_samples_leaf=1,
        min_samples_split=2, min_weight_fraction_leaf=0.0,
        random_state=42, splitter='best'
    )

    model.fit(X, Y)  # Use X and Y instead of x and y

    score = model.score(X, Y)  # Use X and Y instead of x and y

    return model, score

def predict(X, Y, features):
    model, score = train_model(X, Y)

    prediction = model.predict(np.array(features).reshape(1,-1))

    return prediction, score
