# Importing libraries
import streamlit as st
import numpy as np
import pickle
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

# Page configuration
st.set_page_config(page_title='Retail Sales Forecasting', layout='wide')
# Title of the page
st.title(":blue[Retail Sales Forecasting 🛍️]")
# options 
holiday_options = ['True','False']
type_options = ['A', 'B', 'C']
size_options = [151315, 202307,  37392, 205863,  34875, 202505,  70713, 155078,
       125833, 126512, 207499, 112238, 219622, 200898, 123737,  57197,
        93188, 120653, 203819, 203742, 140167, 119557, 114533, 128107,
       152513, 204184, 206302,  93638,  42988, 203750, 203007,  39690,
       158114, 103681,  39910, 184109, 155083, 196321,  41062, 118221]

with st.form("my_form"):
    col1,col2,col3=st.columns([5,2,5])

with col1:
    st.write(' ')
    type = st.selectbox("Type", sorted(type_options),key=3)
    store = st.number_input("Store", min_value=1, max_value=45, value=None, placeholder="Type the store number...")   
    dept = st.number_input("Department", min_value=1, max_value=99, value=None, placeholder="Type the department number...") 
    holiday = st.selectbox("Holiday", holiday_options,key=1)

with col3:               
    st.write(' ')
    size = st.selectbox("Size", size_options,key=2)
    year = st.number_input("Year", min_value=2010, max_value=2030, value=None, placeholder="Type the year...")   
    month = st.number_input("Month", min_value=1, max_value=12, value=None, placeholder="Type the month...")
    week_of_year = st.number_input("Week", min_value=1, max_value=48, value=None, placeholder="Type the week...")
    submit_button = st.form_submit_button(label="Predict")  


if submit_button:
    
    with open(r"s_model.pkl", 'rb') as file:
        loaded_model = pickle.load(file)
    with open(r's_scaler.pkl', 'rb') as f:
        scaler_loaded = pickle.load(f)

    holiday_bool = (holiday == 'True')
    type_bool = (type == 'True')

# Getting the user input
    user_input_array = np.array([[store, dept, size, year, month, week_of_year, holiday_bool, type_bool]])

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
