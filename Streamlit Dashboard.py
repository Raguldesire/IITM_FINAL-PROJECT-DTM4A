# Importing libraries
import streamlit as st
import numpy as np
import pickle
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
import re
st.set_page_config(layout="wide")

st.write("""
<div style='text-align:center'>
    <h1 style='color:#009999;'>Retail Sales Forecasting</h1>
</div>
""", unsafe_allow_html=True)

with st.form("my_form"):
        col1, col2, col3 = st.columns([5, 2, 5])
        with col1:
            st.write(' ')
            holiday = st.text_input("Enter Holiday (Min:0 & Max:1)")
            type = st.text_input("Enter type (Min:0 & Max:2)")
            size = st.text_input("Enter Size (Min:30000 & Max:200000)")
        with col3:
            st.write(
                f'<h5 style="color:rgb(0, 153, 153,0.4);">NOTE: Min & Max given for reference, you can enter any value</h5>',
                unsafe_allow_html=True)
            store = st.text_input("Enter Store (Min:1 & Max:45)")
            dept = st.text_input("Enter dept (Min:1 & Max:99)")
            year = st.text_input("Enter year (Min:2010 & Max:2030)")
            month = st.text_input("Enter month (Min:1 & Max:12)")
            week_of_year = st.text_input("Enter week (Min:1, Max:48)")
            submit_button = st.form_submit_button(label="PREDICT WEEK SALES")
            st.markdown("""
                    <style>
                    div.stButton > button:first-child {
                        background-color: #009999;
                        color: white;
                        width: 100%;
                    }
                    </style>
                """, unsafe_allow_html=True)

        flag = 0
        pattern = "^(?:\d+|\d*\.\d+)$"
        for i in [store, dept,year,month,week_of_year]:
            if re.match(pattern, i):
                pass
            else:
                flag = 1
                break

if submit_button and flag == 1:
        if len(i) == 0:
            st.write("please enter a valid number space not allowed")
        else:
            st.write("You have entered an invalid value: ", i)

if submit_button and flag == 0:
    import pickle

    with open(r".venv\s_model.pkl", 'rb') as file:
        loaded_model = pickle.load(file)
    with open(r'.venv\s_scaler.pkl', 'rb') as f:
        scaler_loaded = pickle.load(f)

    holiday_bool = (holiday == 'True')
    type_bool = (type == 'True')

# Getting the user input
    user_input_array = np.array([[store, dept, size, year, month, week_of_year, holiday, type]])

    numeric_cols = [1, 3, 4, 5, 6]
    categorical_cols = [0, 2, 7]

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_cols),
            ('cat', OneHotEncoder(drop=None, sparse=False), categorical_cols)  
        ])

    X_preprocessed = preprocessor.fit_transform(user_input_array)

    expected_features = X_preprocessed.shape[1]

    if expected_features != 8:  
        st.write(f"Error: Expected 8 features, but got {expected_features} features.")
    else:
        
        prediction = loaded_model.predict(X_preprocessed)

        st.info("The predicted week sales is Rs. {}".format(prediction[0]))




