

import streamlit as st
import pickle
import numpy as np
from sklearn.tree import DecisionTreeClassifier
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
    print(inp_species)
    print(feel.index(inp_species)+1)

    st.write(f"Your favore food is : {np.squeeze(result, -1)}")






