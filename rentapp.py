import xgboost as xgb
import streamlit as st
import pandas as pd
from PIL import Image
import pickle
import joblib

xgb_model = joblib.load('final_xgboost_model.pkl')

st.set_page_config(
    layout='wide',
    page_title='Lagos House Rent Prediction',
    page_icon='img.jfif',
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: shown;}
            footer {visibility: hidden;}
            footer:after {
                          content:'Created by TrailBlazersNG Team'; 
                          visibility: visible;
                          display: block;
                          position: relative;
                          #background-color: white;
                          padding: 4px;
                          top: 2px;
                          }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)


st.markdown("<h1 style='text-align: center; color: black;'> Lagos House Rent Prediction</h1>", unsafe_allow_html=True)
image = Image.open('image3.jpg')
st.image(image, caption='PHOTO FROM ROYALTY-FREE STOCK PHOTO')


Location = st.selectbox('HOUSE LOCATION', ['Ikoyi', 'Yaba', 'Lekki', 'Ajah', 'Victoria Island', 'Ikeja',
                                           'Ilupeju', 'Isolo', 'Shomolu', 'Ketu', 'Surulere', 'Amuwo odofin',
                                           'Abule Egba', 'Oshodi', 'Apapa', 'Ikorodu', 'Ojodu', 'Alimosho',
                                           'Egbeda', 'Ikotun', 'Idimu', 'Ogba', 'Igando', 'Akowonjo',
                                           'Ibeju/Lekki', 'Akoka', 'Ebute-metta', 'Ago Palace', 'Gbagada',
                                           'Oworoshonki', 'Maryland', 'Ojo', 'Ayobo', 'Agege', 'Marina',
                                           'Obalende', 'Lagos Island', 'Mushin', 'Magodo', 'Ojota', 'Ogudu',
                                           'Epe', 'Bariga', 'Ejigbo', 'Badagry', 'Iganmu'])
House_type = st.selectbox('HOUSE_TYPE', ["FLAT", "HOUSE", "DUPLEX", "BUNGALOW"])
Number_of_bedrooms = st.number_input('BEDROOMS', min_value=1, max_value=9, value=1)
Number_of_toilets = st.number_input('TOILETS', min_value=1, max_value=9, value=1)
Number_of_bathrooms = st.number_input('BATHROOMS', min_value=1, max_value=9, value=1)


def predict(Number_of_bedrooms, Number_of_bathrooms, Number_of_toilets, Location, House_type):
    if Location == 'Lekki':
        Location = 1
    elif Location == 'Ajah':
        Location = 2
    elif Location == 'Ojodu':
        Location = 3
    elif Location == 'Ikoyi':
        Location = 4
    elif Location == 'Ikeja':
        Location = 5
    elif Location == 'Yaba':
        Location = 6
    elif Location == 'Surulere':
        Location = 7
    elif Location == 'Gbagada':
        Location = 8
    elif Location == 'Isolo':
        Location = 9
    elif Location == 'Victoria Island':
        Location = 10
    elif Location == 'Alimosho':
        Location = 11
    elif Location == 'Ketu':
        Location = 12
    elif Location == 'Shomolu':
        Location = 13
    elif Location == 'Ogba':
        Location = 14
    elif Location == 'Magodo':
        Location = 15
    elif Location == 'Ikorodu':
        Location = 16
    elif Location == 'Ogudu':
        Location = 17
    elif Location == 'Ago Palace':
        Location = 18
    elif Location == 'Egbeda':
        Location = 19
    elif Location == 'Agege':
        Location = 20
    elif Location == 'Abule Egba':
        Location = 21
    elif Location == 'Amuwo odofin':
        Location = 22
    elif Location == 'Maryland':
        Location = 23
    elif Location == 'Ikotun':
        Location = 24
    elif Location == 'Oshodi':
        Location = 25
    elif Location == 'Ibeju/Lekki':
        Location = 26
    elif Location == 'Ilupeju':
        Location = 27
    elif Location == 'Akoka':
        Location = 28
    elif Location == 'Oworoshonki':
        Location = 29
    elif Location == 'Akowonjo':
        Location = 30
    elif Location == 'Ejigbo':
        Location = 31
    elif Location == 'Idimu':
        Location = 32
    elif Location == 'Ebute-metta':
        Location = 33
    elif Location == 'Apapa':
        Location = 34
    elif Location == 'Mushin':
        Location = 35
    elif Location == 'Ojota':
        Location = 36
    elif Location == 'Ojo':
        Location = 37
    elif Location == 'Igando':
        Location = 38
    elif Location == 'Lagos Island':
        Location = 39
    elif Location == 'Ayobo':
        Location = 40
    elif Location == 'Badagry':
        Location = 41
    elif Location == 'Bariga':
        Location = 42
    elif Location == 'Epe':
        Location = 43
    elif Location == 'Iganmu':
        Location = 44
    elif Location == 'Obalende':
        Location = 45
    elif Location == 'Marina':
        Location = 46

    if House_type == 'FLAT':
        House_type = 1
    elif House_type == 'HOUSE':
        House_type = 2
    elif House_type == 'DUPLEX':
        House_type = 3
    elif House_type == 'BUNGALOW':
        House_type = 4

    prediction = xgb_model.predict(
        pd.DataFrame([[Number_of_bedrooms, Number_of_bathrooms, Number_of_toilets, Location, House_type]],
                     columns=['BEDROOMS', 'BATHROOMS', 'TOILETS', 'LOCATION', 'HOUSE_TYPE']))
    return prediction


if st.button('Predict Price'):
    price = predict(Number_of_bedrooms, Number_of_bathrooms, Number_of_toilets, Location, House_type)
    st.success(f'The predicted rent of the property is {price[0]:.2f}')

st.title('Contributors')
st.text("""
        This app was developed by:
        """)
st.write('- Kehinde Olalekan (https://github.com/KENNYDGREAT2)')
st.write('- Babajide Alao (https://github.com/BabajideAlao-knn)')
st.write('- Paul Adegbite (https://github.com/octopuspaul110)')
st.write('- Alinta Innocent (https://github.com/aliNtainnocent)')
st.write('- Michael Onabanjo (https://github.com/Onabanjomicheal)')

st.info('During #DSRoom Project challenge under the mentorship of Samson Afolabi (https://twitter.com/samsonafo)')