#TO RUN THIS CODE,TYPE THIS COMMAND IN YOUR ANACONDA PROMPT
#--->streamlit run "paste path of the file"

#MULTPLE DISEASE PREDICTION SYSTEM 
#CREATED USING TRAINED ML MODELS

import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="HEALTH ASSISTANT",
                   layout="wide",
                   page_icon="hospital")

os.path.dirname(os.path.abspath(__file__))

Heart_disease = pickle.load(open(
    "C:/Users/haris/Documents/spyder/MDPS/models/heart disease model.sav", "rb"))

parkinsons_disease = pickle.load(
    open("C:/Users/haris/Documents/spyder/MDPS/models/parkinsons model.sav", "rb"))

diabetes = pickle.load(
    open("C:/Users/haris/Documents/spyder/MDPS/models/diabetes model.sav", "rb"))

breast_cancer = pickle.load(open(
    "C:/Users/haris/Documents/spyder/MDPS/models/Breast cancer model.sav", "rb"))

Lungs_cancer = pickle.load(
    open("C:/Users/haris/Documents/spyder/MDPS/models/lungs cancer model.sav", "rb"))

with st.sidebar:
    selected = option_menu("MULTIPLE DISEASE PREDICTIVE SYSTEM",
                           ["HEART DISEASE PREDICTION",
                            "PARKINSONS PREDICTION PREDICTION",
                            "DIABETES PREDICTION",
                            "BREAST CANCER PREDICTION",
                            "LUNGS CANCER PREDICTION"],
                           menu_icon=["virus"],
                           icons=["heart", "person", "file-earmark-medical",
                                  "gender-female", "lungs-fill"],
                           default_index=0)

if(selected == "HEART DISEASE PREDICTION"):
    st.title("HEART DISEASE PREDICTON SYSTEM")

    col_1, col_2, col_3, = st.columns(3)

    with col_1:
        Age = st.text_input("Age of the person")

    with col_2:
        Sex = st.text_input("Sex")

    with col_3:
        Cp = st.text_input("Chest Pain rate")

    with col_1:
        Trestbps = st.text_input("Resting BP of person")

    with col_2:
        Chol = st.text_input("Serum Cholestrol level")

    with col_3:
        Fbs = st.text_input("Fasting Blood sugar level")

    with col_1:
        Restecg = st.text_input("resting ECG results")

    with col_2:
        Thalach = st.text_input("maximum heart rate achieved")

    with col_3:
        Exang = st.text_input("exercise induced angina")

    with col_1:
        Oldpeak = st.text_input("oldpeak induced by exang")

    with col_2:
        Slope = st.text_input("slope of the peak exercise")

    with col_3:
        Ca = st.text_input("colored by flourosopy")

    with col_1:
        Thal = st.text_input("Normal")

    heart_diagnosis = " "

    if st.button("HEART DISEASE TEST RESULTS"):
        user_input = [Age, Sex, Cp, Trestbps, Chol, Fbs,
                      Restecg, Thalach, Exang, Oldpeak, Slope, Ca, Thal]
        user_input = [float(x) for x in user_input]

        heart_prediction = Heart_disease.predict([user_input])
        if heart_prediction[0] == 1:
            heart_diagnosis = "The person have heart disease"
        else:
            heart_diagnosis = "The person does not have  heart disease"

    st.success(heart_diagnosis)


if(selected == "PARKINSONS PREDICTION PREDICTION"):
    st.title("PARKINSONS DISEASE PREDICTION SYSTEM")

    col_1, col_2, col_3, col_4 = st.columns(4)

    with col_1:
        MDVPFoHz = st.text_input(" MDVP:Fo(Hz)")

    with col_2:
        MDVPFhiHz = st.text_input(" MDVP:Fhi(Hz)")

    with col_3:
        MDVPFloHz = st.text_input("MDVP:Flo(Hz)")

    with col_4:
        MDVPJitterpercent = st.text_input("MDVP:Jitter(%)")

    with col_1:
        MDVPJitterAbs = st.text_input("MDVP:Jitter(Abs)")

    with col_2:
        MDVPRAP = st.text_input("MDVP:RAP")

    with col_3:
        MDVPPPQ = st.text_input("MDVP:PPQ")

    with col_4:
        JitterDDP = st.text_input("Jitter:DDP")

    with col_1:
        MDVPShimmer = st.text_input("MDVP:Shimmer")

    with col_2:
        MDVPShimmerdB = st.text_input("MDVP:Shimmer(dB)")

    with col_3:
        ShimmerAPQ3 = st.text_input("Shimmer:APQ3")

    with col_4:
        ShimmerAPQ5 = st.text_input("Shimmer:APQ5")

    with col_1:
        MDVPAPQ = st.text_input("MDVP:APQ")

    with col_2:
        ShimmerDDA = st.text_input("Shimmer:DDA")

    with col_3:
        NHR = st.text_input("NHR")

    with col_4:
        HNR = st.text_input("HNR")

    with col_1:
        RPDE = st.text_input("RPDE")

    with col_2:
        DFA = st.text_input("DFA")

    with col_3:
        spread1 = st.text_input("spread1")

    with col_4:
        spread2 = st.text_input("spread2")

    with col_1:
        D2 = st.text_input("D2")

    with col_2:
        PPE = st.text_input("PPE")

    parkinson_diagnosis = ""

    if st.button("PARKINSONS DISEASE RESULTS"):
        parkinson_result = parkinsons_disease.predict([[MDVPFoHz, MDVPFhiHz, MDVPFloHz, MDVPJitterpercent, MDVPJitterAbs, MDVPRAP, MDVPPPQ,
                                                      JitterDDP, MDVPShimmer, MDVPShimmerdB, ShimmerAPQ3, ShimmerAPQ5, MDVPAPQ, ShimmerDDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])

        if (parkinson_result[0] == 1):
            parkinson_diagnosis = " The person was affected by parkinsons disease"

        else:
            parkinson_diagnosis = "The person was not affected by parkinsons disease"

    st.success(parkinson_diagnosis)


if(selected == "DIABETES PREDICTION"):
    st.title("DIABETES PREDICTION SYSTEM")

    col_1, col_2, col_3 = st.columns(3)

    with col_1:
        Pregnancies = st.text_input("Number of Pregnancies")

    with col_2:
        Glucose = st.text_input("Glucose level")

    with col_3:
        BloodPressure = st.text_input("BloodPressure Level")

    with col_1:
        SkinThickness = st.text_input("SkinThickness level")

    with col_2:
        Insulin = st.text_input("Insulin")

    with col_3:
        BMI = st.text_input("BMI Level")

    with col_1:
        DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction")

    with col_2:
        Age = st.text_input("Age Of The Person")

    diabetes_diagnosis = " "

    if st.button("DIABETES TEST RESULTS"):
        diabetes_result = diabetes.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diabetes_result[0] == 1):
            diabetes_diagnosis = "The person has diabetes"
        else:
            diabetes_diagnosis = "The person has no diabetes"

    st.success(diabetes_diagnosis)


if(selected == "BREAST CANCER PREDICTION"):
    st.title("BREAST CANCER PREDICTION SYSTEM")

    col_1, col_2, col_3, col_4 = st.columns(4)

    with col_1:
        meanradius = st.text_input("mean radius")

    with col_2:
        meantexture = st.text_input("mean texture")

    with col_3:
        meanperimeter = st.text_input("mean perimeter")

    with col_4:
        meanarea = st.text_input("mean area")

    with col_1:
        meansmoothness = st.text_input("mean smoothness")

    with col_2:
        meancompactness = st.text_input("mean compactness")

    with col_3:
        meanconcavity = st.text_input("mean concavity")

    with col_4:
        meanconcavepoints = st.text_input("mean concave points")

    with col_1:
        meansymmetry = st.text_input("mean symmetry")

    with col_2:
        meanfractaldimension = st.text_input("mean fractal dimension")

    with col_3:
        radiuserror = st.text_input("radius error")

    with col_4:
        textureerror = st.text_input("texture error")

    with col_1:
        perimetererror = st.text_input("perimeter error")

    with col_2:
        areaerror = st.text_input("area error")

    with col_3:
        smoothnesserror = st.text_input("smoothness error")

    with col_4:
        compactnesserror = st.text_input("compactness error")

    with col_1:
        concavityerror = st.text_input("concavity error")

    with col_2:
        concavepointserror = st.text_input("concave points error")

    with col_3:
        symmetryerror = st.text_input("symmetry error")

    with col_4:
        fractaldimensionerror = st.text_input("fractal dimension error")

    with col_1:
        worstradius = st.text_input("worst radius")

    with col_2:
        worsttexture = st.text_input("worst texture")

    with col_3:
        worstperimeter = st.text_input("worst perimeter")

    with col_4:
        worstarea = st.text_input("worst area")

    with col_1:
        worstsmoothness = st.text_input("worst smoothness")

    with col_2:
        worstcompactness = st.text_input("worst compactness")

    with col_3:
        worstconcavity = st.text_input("worst concavity")

    with col_4:
        worstconcavepoints = st.text_input("worst concave points")

    with col_1:
        worstsymmetry = st.text_input("worst symmetry")

    with col_2:
        worstfractaldimension = st.text_input("worst fractal dimension")

    breast_cancer_diagnosis = ""

    if st.button("BREAST CANCER TEST RESULTS"):
        user_input = [meanradius, meantexture, meanperimeter, meanarea, meansmoothness, meancompactness, meanconcavity, meanconcavepoints, meansymmetry, meanfractaldimension, radiuserror, textureerror, perimetererror, areaerror, smoothnesserror, compactnesserror,
                      concavityerror, concavepointserror, symmetryerror, fractaldimensionerror, worstradius, worsttexture, worstperimeter, worstarea, worstsmoothness, worstcompactness, worstconcavity, worstconcavepoints, worstsymmetry, worstfractaldimension]
        user_input = [float(x) for x in user_input]
        cancer_result = breast_cancer.predict([user_input])

        if (cancer_result[0] == 1):
            breast_cancer_diagnosis = "The person was not affected by breast cancer"
        else:
            breast_cancer_diagnosis = "The person was affected by breast cancer"

    st.success(breast_cancer_diagnosis)


if(selected == "LUNGS CANCER PREDICTION"):
    st.title("LUNGS CANCER PREDICTION SYSTEM")

    col_1, col_2, col_3, = st.columns(3)

    with col_1:
        GENDER = st.text_input("gender")

    with col_2:
        AGE = st.text_input("Age of the person")

    with col_3:
        SMOKING = st.text_input("Smoking status")

    with col_1:
        YELLOW_FINGERS = st.text_input("Yellow fingers")

    with col_2:
        ANXIETY = st.text_input("Anxiety status")

    with col_3:
        PEER_PRESSURE = st.text_input("Peer pressure status")

    with col_1:
        CHRONIC_DISEASE = st.text_input("Chronic disease status")

    with col_2:
        FATIGUE = st.text_input("Fatigui status")

    with col_3:
        ALLERGY = st.text_input("Allergy status")

    with col_1:
        WHEEZING = st.text_input("Wheezing status")

    with col_2:
        ALCOHOL_CONSUMING = st.text_input("Alcohol consuming status")

    with col_3:
        COUGHING = st.text_input("Cough status")

    with col_1:
        SHORTNESS_OF_BREATH = st.text_input("Breathe status")

    with col_2:
        SWALLOWING_DIFFICULTY = st.text_input("Swallowing difficulty status")

    with col_3:
        CHEST_PAIN = st.text_input("Chest pain status")

    lungs_diagnosis = ""

    if st.button("LUNGS CANCER TEST RESULTS"):
        user_input = [GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE,
                      ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]
        user_input = [float(x) for x in user_input]

        lungs_prediction = Lungs_cancer.predict([user_input])
        if lungs_prediction[0] == 1:
            lungs_diagnosis = 'The person is having lungs cancer'
        else:
            lungs_diagnosis = 'The person does not have lungs cancer'

    st.success(lungs_diagnosis)
