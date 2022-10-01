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
    bin_str = (png_file)
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

Location = st.selectbox('House Location:', ['Ikoyi', 'Yaba', 'Lekki', 'Ajah', 'Victoria island', 'Ikeja',
                             'Ilupeju', 'Isolo', 'Shomolu', 'Ketu', 'Surulere', 'Amuwo odofin',
                             'Abule egba', 'Oshodi', 'Apapa', 'Ikorodu', 'Ojodu', 'Ipaja',
                             'Egbeda', 'Ikotun', 'Idimu', 'Ogba', 'Igando', 'Akowonjo',
                             'Ikate-lekki', 'Ikota-lekki', 'Chevron-lekki', 'Phase1-lekki',
                             'Phase2-lekki', 'Vgc-lekki', 'Ibeju-lekki', 'Osapa london lekki',
                             'Agungi lekki', 'Opebi-ikeja', 'Allen avenue-ikeja', 'Gra-ikeja',
                             'Oregun-ikeja', 'Akoka-yaba', 'Alagomeji-yaba', 'Adekunle-yaba',
                             'Abule oja-yaba', 'Abule ijesha-yaba', 'Onike-yaba', 'Jibowu-yaba',
                             'Sabo-yaba', 'Iwaya-yaba', 'Ebute metta-yaba', 'Fola agoro-yaba',
                             'Ago palace-okota', 'Okota', 'Phase1-gbagada', 'Phase2-gbagada',
                             'Ifako-gbagada', 'Oworonshoki-gbagada', 'Soluyi-gbagada',
                             'Medina-gbagada', 'Gbagada', 'Anthony village-maryland',
                             'Mende-maryland', 'Maryland', 'Ikotun-igando', 'Ojo', 'Ayobo',
                              'Akesan', 'Fagba-agege', 'Cement-agege', 'Oko oba-agege',
                             'Ifako-agege', 'Iju ishaga-agege', 'Orile-agege', 'Agege',
                             'Marina-lagos island', 'Obalende-lagos island', 'Lagos island',
                             'Ilasamaja-mushin', 'Mushin', 'Phase1-magodo', 'Phase2-magodo',
                             'Ojota', 'Ogudu', 'Alapere-ketu', 'Mile12-ketu', 'Shangisha-ketu',
                             'Ikosi-ketu', 'Epe', 'Alimosho', 'Bariga', 'Ejigbo', 'Sangotedo',
                             'Badagry', 'Iganmu-orile'])

House_type = st.selectbox('Type of House:', ["FLAT", "HOUSE", "DUPLEX", "BUNGALOW"])
Number_of_bedrooms = st.number_input('Number of bedroom:', min_value=1, max_value=9, value=1)
Number_of_toilets = st.number_input('Number of toilet:', min_value=1, max_value=9, value=1)
Number_of_bathrooms = st.number_input('Number of bathrooms:', min_value=1, max_value=9, value=1)


def predict(Number_of_bedrooms, Number_of_bathrooms, Number_of_toilets, Location, House_type):
    
    new_location = {'Ikoyi': 0,'Yaba': 1,'Lekki': 2,'Ajah': 3,'Victoria island': 4,
                    'Ikeja': 5,'Ilupeju': 6,'Isolo': 7,'Shomolu': 8,'Ketu': 9,
                    'Surulere': 10,'Amuwo odofin': 11,'Abule egba': 12,'Oshodi': 13,
                    'Apapa': 14,'Ikorodu': 15,'Ojodu': 16,'Ipaja': 17,'Egbeda': 18,
                    'Ikotun': 19,'Idimu': 20,'Ogba': 21,'Igando': 22,'Akowonjo': 23,
                    'Ikate-lekki': 24,'Ikota-lekki': 25,'Chevron-lekki': 26,
                    'Phase1-lekki': 27,'Phase2-lekki': 28,'Vgc-lekki': 29,
                    'Ibeju-lekki': 30,'Osapa london lekki': 31,
                    'Agungi lekki': 32,'Opebi-ikeja': 33,'Allen avenue-ikeja': 34,
                    'Gra-ikeja': 35,'Oregun-ikeja': 36,'Akoka-yaba': 37,
                    'Alagomeji-yaba': 38,'Adekunle-yaba': 39,'Abule oja-yaba': 40,
                    'Abule ijesha-yaba': 41,'Onike-yaba': 42,'Jibowu-yaba': 43,
                    'Sabo-yaba': 44,'Iwaya-yaba': 45,'Ebute metta-yaba': 46,
                    'Fola agoro-yaba': 47,'Ago palace-okota': 48,'Okota': 49,
                    'Phase1-gbagada': 50,'Phase2-gbagada': 51,'Ifako-gbagada': 52,
                    'Oworonshoki-gbagada': 53,'Soluyi-gbagada': 54,
                    'Medina-gbagada': 55,'Gbagada': 56,
                    'Anthony village-maryland': 57, 'Mende-maryland': 58,
                    'Maryland': 59,'Ikotun-igando': 60,'Ojo': 61,'Ayobo': 62,
                    'Akesan': 63,'Fagba-agege': 64,'Cement-agege': 65,
                    'Oko oba-agege': 66,'Ifako-agege': 67,'Iju ishaga-agege': 68,
                    'Orile-agege': 69,'Agege': 70,'Marina-lagos island': 71,
                    'Obalende-lagos island': 72,'Lagos island': 73,
                    'Ilasamaja-mushin': 74,'Mushin': 75,'Phase1-magodo': 76,
                    'Phase2-magodo': 77,'Ojota': 78,'Ogudu': 79,'Alapere-ketu': 80,
                    'Mile12-ketu': 81,'Shangisha-ketu': 82,'Ikosi-ketu': 83,
                    'Epe': 84,'Alimosho': 85,'Bariga': 86,'Ejigbo': 87,
                    'Sangotedo': 88,'Badagry': 89,'Iganmu-orile': 90}

    for i in new_location:
        if Location == i:
            Location = new_location[i]

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
    st.write('The predicted price of the property is: ₦{:,.2f}'.format(price[0]))

st.title('Contributors')
st.text("""
        This app was developed by:
        """)
st.write('- Michael Onabanjo (https://github.com/Onabanjomicheal)')
st.write('- Babajide Alao (https://github.com/BabajideAlao-knn)')
st.write('- Paul Adegbite (https://github.com/octopuspaul110)')
st.write('- Alinta Innocent (https://github.com/aliNtainnocent)')
st.write('- Kehinde Olalekan (https://github.com/KENNYDGREAT2)')

st.info('During #DSRoom Project challenge under the mentorship of Samson Afolabi (https://twitter.com/samsonafo)')