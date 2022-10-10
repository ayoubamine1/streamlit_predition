

import streamlit as st
import pickle
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import pandas as pd 
data = pd.read_cv('https://github.com/ayoubamine1/streamlit_predition/blob/e6a2e72ab2975752a38a8ba113d40ac727c66697/feelings.csv')

loaded_model = pickle.load(open('model.sav', 'rb'))

feel = ['Fatigued','Sleepy','Hungry','Angry','Lonely','Sad','Happy','Bored','Overweight','Underweight','High Glucose','Headache']

st.header("Food Prediction App")
age = st.text_input("Enter the Age: ", key="age")
inp_species = st.radio(
        'Name of the fish:',
        np.unique(feel))


#feel = st.text_input("Enter the Feeling: ",key="feeling")


if st.button('Make Prediction'):
    result = loaded_model.predict([[age, feel.index(inp_species)+1]])
    st.write(f"Your favore food is : {np.squeeze(result, -1)}")
    row = {'age':10,'feeling':'without','food':tajine}
    data.append(row,inplace= True)







