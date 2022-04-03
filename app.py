import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from PIL import Image

image = Image.open('background.jpg')

st.image(image, caption='')
st.write("""
# Stroke Prediction App
Stroke is the 2nd leading cause of death globally, responsible for approximately 
11% of total deaths. This app which prediction whether a patient is likely to get a stroke or not is based upon the input parameters like gender, age, various diseases, and smoking status.
""")

st.sidebar.header('User Input Features')

def user_input_features():
        gender = st.sidebar.selectbox('Gender',('Male','Female'))
        age = st.sidebar.slider('Age',3,100,55)
        hypertension = st.sidebar.selectbox('Hypertension',('Yes','No'))
        heart_disease = st.sidebar.selectbox('Heart-disease',('Yes','No'))
        ever_married = st.sidebar.selectbox('Ever Married',('Yes','No'))
        work_type = st.sidebar.selectbox('Work Type',('Private','Self-employed','Govt_job','children','Never_worked'))
        Residence_type = st.sidebar.selectbox('Residence Type',('Urban','Rural'))
        avg_glucose_level = st.sidebar.slider('average glucose level',1,350,175)
        smoking_status = st.sidebar.selectbox('Smoking Status',('formerly smoked','never smoked','smokes','Unknown'))
        
        if hypertension == 'Yes':
            hypertension = 1
        else:
            hypertension = 0

        if heart_disease == 'Yes':
            heart_disease = 1
        else:
            heart_disease = 0

        encode = {"gender" : { "Male" : 1 , "Female" : 0} , "ever_married" : {"Yes" : 1 , "No" : 0} , "work_type" : {"Private" : 0 , "Self-employed" : 1 , 
                "Govt_job" : 2 , "children" : 3, "Never_worked" : 4} , "Residence_type" : {"Urban" : 1 , "Rural" : 0} , "smoking_status" : {"formerly smoked" : 0
                , "never smoked" : 1, "smokes" : 2 , "Unknown" : 3}}

        gender = encode['gender'][gender]
        ever_married = encode['ever_married'][ever_married]
        work_type = encode['work_type'][work_type]
        Residence_type = encode['Residence_type'][Residence_type]
        smoking_status = encode['smoking_status'][smoking_status]

        data = {'gender': gender,
                'age': age,
                'hypertension': hypertension,
                'heart_disease': heart_disease,
                'ever_married': ever_married,
                'work_type': work_type,
                'Residence_type' : Residence_type,
                'avg_glucose_level':avg_glucose_level,
                'smoking_status':smoking_status
                }
        features = pd.DataFrame(data, index=[0])
        return features
input_df = user_input_features()

stroke_raw = pd.read_csv('healthcare-dataset-stroke-data - healthcare-dataset-stroke-data.csv')
stroke_raw = stroke_raw.drop(columns=['bmi','id'],axis = 1)
strokes = stroke_raw.drop(columns=['stroke'],axis=1)

df = pd.concat([input_df,strokes],axis=0)

df_input = df[:1]
st.subheader('Your features')
st.write(df_input)

continuous_columns = ['age','avg_glucose_level']
df[continuous_columns] = StandardScaler().fit_transform(df[continuous_columns])
df = df[:1]
load_clf = pickle.load(open('model.pkl', 'rb'))


prediction = load_clf.predict(df)
prediction_proba = load_clf.predict_proba(df)


st.subheader('Prediction')
penguins_species = np.array(['Hurray !! You donot have stroke','Chances of having stroke are high please consult Vascular neurologists '])
st.write(penguins_species[prediction])

st.subheader('Prediction Probabilities')
st.write(prediction_proba)