import os
import pickle
import streamlit as st  #web app
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreak by PJ',
                   layout='wide',
                   page_icon="⚕️")
diabetes_model=pickle.load(open(r"C:\Jyothirmai\internship microsoft&sap\project2\training_models\diabetes_model.sav",'rb'))
heart_model=pickle.load(open(r"C:\Jyothirmai\internship microsoft&sap\project2\training_models\heart_model.sav",'rb'))
parkinsons_model=pickle.load(open(r"C:\Jyothirmai\internship microsoft&sap\project2\training_models\parkinsons_model.sav",'rb'))


with st.sidebar:
    selected= option_menu('Prediction of Disease Outbreak System',
                          ['Diabetes Prediction','Heart Disease Prediction','Parkinsons prediction'],
                          menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)


# Diabetes Prediction Page
if selected== 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies= st.text_input('No.of Pregnancies')
    with col2:
        Glucose= st.text_input('Glucose Level')
    with col3:
        BloodPressure= st.text_input('Blood pressure Value')
    with col1:
        SkinThickness= st.text_input('Skin thickness value')
    with col2:
        Insulin= st.text_input('Insulin Level')
    with col3:
        BMI= st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction= st.text_input('Diabetes Pedegree Function value')
    with col2:
        Age= st.text_input('Age of the person')

    # code for Prediction
    diab_diagnosis=''
    if st.button('Diabetes Test Result'):
     user_input=[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
     user_input=[float(x) for x in user_input]
     diab_prediction=diabetes_model.predict([user_input])
     if diab_prediction[0]==1:
         diab_diagnosis= 'The person is diabetic'
     else:
         diab_diagnosis= 'The person is not diabetic'
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain types')
    with col4:
        trestbps = st.text_input('Resting Blood Pressure')
    with col1:
        chol = st.text_input('Serum Cholestoral in mg/dL')
    with col2:
        fbs = st.text_input('Fasting Blood Sugar >= 120 mg/dl')
    with col3:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col4:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col1:
        exang = st.text_input('Exercise Induced Angina')
    with col2:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col3:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col4:
        ca = st.text_input('No.of major vessels colored by flourosopy')
    with col1:
        thal = st.text_input('Type of thalassemia: 1= normal; 2= fixed defect; 3 = reversable defect')

   # code for Prediction
    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_model.predict([user_input])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
    st.success(heart_diagnosis)



# Parkinson's Prediction Page
if selected == "Parkinsons prediction":
    st.title("Parkinson's Disease Prediction using ML")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col1:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col2:
        RAP = st.text_input('MDVP:RAP')
    with col3:
        PPQ = st.text_input('MDVP:PPQ')
    with col4:
        DDP = st.text_input('Jitter:DDP')
    with col1:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col2:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col3:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col4:
        APQ5 = st.text_input('Shimmer:APQ5')
    with col1:
        APQ = st.text_input('MDVP:APQ')
    with col2:
        DDA = st.text_input('Shimmer:DDA')
    with col3:
        NHR = st.text_input('NHR')
    with col4:
        HNR = st.text_input('HNR')
    with col1:
        RPDE = st.text_input('RPDE')
    with col2:
        DFA = st.text_input('DFA')
    with col3:
        spread1 = st.text_input('spread1')
    with col4:
        spread2 = st.text_input('spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''    
    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        user_input = [float(x) for x in user_input]
        parkinsons_prediction = parkinsons_model.predict([user_input])
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
    st.success(parkinsons_diagnosis)