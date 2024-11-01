import streamlit as st
import requests
import numpy as np
import pandas as pd

st.markdown("""# Welcome to the vagetation classifier""")

with st.form(key='params_for_api'):

    Elevation = st.number_input('Please enter the elevation : ')
    Aspect = st.number_input('Please enter the aspect : ')
    Slope = st.number_input('Please enter the slope : ')
    hdth = st.number_input('Please enter the horizontal distance to nearest surface water : ')
    vdth = st.number_input('Please enter the vertical distance to nearest surface water : ')
    hdtr = st.number_input('Please enter the horizontal distance to nearest roadway : ')
    hdtf = st.number_input('Please enter the horizontal distance to nearest wildfire ignition points : ')
    wad = st.selectbox('Please select the wilderness area designation : ', ['Rawah', 'Neota','Comanche Peak', 'Cache la Poudre'])
    soil = st.selectbox('Please select the soil type : ', ['Cathedral family', 'Vanet','Haploborolis', 'Ratake family', 'Vanet family', 'Vanet',
                                                        'Gothic family', 'Supervisor','Troutville family', 'Bullwark', 'Bullwark',
                                                        'Legault family', 'Catamount family', 'Pachic Argiborolis', 'unspecified',
                                                        'Cryaquolis','Gateview family', 'Rogert family', 'Typic Cryaquolis - Borohemists complex', 'Typic Cryaquepts - Typic Cryaquolls complex', 'Typic Cryaquolls - Leighcan family, till substratum complex',
                                                        'Leighcan family, till substratum, extremely bouldery', 'Leighcan family, till substratum - Typic Cryaquolls complex', ' Leighcan family, extremely stony','Leighcan family, warm, extremely stony', 'Granile',
                                                        'Leighcan family, warm - Rock outcrop complex, extremely stony', 'Leighcan family - Rock outcrop complex, extremely stony', 'Como - Legault families complex, extremely stony',
                                                        'Como family - Rock land - Legault family complex, extremely stony', 'Leighcan - Catamount families complex, extremely stony', 'Catamount family - Rock outcrop - Leighcan family complex, extremely stony', 'Leighcan - Catamount families - Rock outcrop complex, extremely stony','Cryorthents - Rock land complex, extremely stony',
                                                        'Cryumbrepts - Rock outcrop - Cryaquepts complex', 'Bross family - Rock land - Cryumbrepts complex, extremely stony', 'Rock outcrop - Cryumbrepts - Cryorthents complex, extremely stony', 'Leighcan - Moran families - Cryaquolls complex, extremely stony',
                                                        'Moran family - Cryorthents - Leighcan family complex, extremely stony','Moran family - Cryorthents - Rock land complex, extremely stony'
                                                        ])
    hillshade_9am = st.number_input('Please enter the hillshade index at 9am : ')
    hillshade_Noon = st.number_input('Please enter the hillshade index at noon : ')
    hillshade_3pm = st.number_input('Please enter the hillshade index at 3pm : ')

    st.form_submit_button('Make prediction')


params = dict(
        Elevation = Elevation,
        Aspect = Aspect,
        Slope = Slope,
        Horizontal_Distance_To_Hydrology = hdth,
        Vertical_Distance_To_Hydrology = vdth,
        Horizontal_Distance_To_Roadways = hdtr,
        Hillshade_9am =  hillshade_9am,
        Hillshade_Noon =  hillshade_Noon,
        Hillshade_3pm = hillshade_3pm,
        Horizontal_Distance_To_Fire_Points = hdtf,
        wilderness = wad,
        Soil_Type = soil)

vegatation_api_url = 'http://127.0.0.1:8000/predict'
response = requests.get(vegatation_api_url, params=params)

prediction = response.json()

pred = prediction

st.header(f'Vegatation type is : {pred}')
