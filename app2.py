#deployment
import streamlit as st
from streamlit_player import st_player
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim
import config
import requests

import pickle 
model=pickle.load(open(r"model.pkl","rb"))
@st.cache(allow_output_mutation=True)

 


#recommend function

def recommend(Nitrogen,Phosphorous,Potassium,temperature, humidity,ph,rainfall):

    # Making predictions 

    prediction = model.predict( 

        [[Nitrogen,Phosphorous,Potassium,temperature, humidity,ph,rainfall]])

    return prediction



#main function for the webpage

def app():

    # front end elements of the web page
     


    # display the front end aspect

    st.markdown("<h1><center>Cropify</center></h1><br><center><i> Crop Recommendation System made with Streamlit, Machine Learning and</i> ❤️</br></center>", unsafe_allow_html = True)
    st.text("")
    st.text("")
    st_player("https://www.youtube.com/watch?v=Cmm-itIRPU8")
    st.text("")
    st.text("")
    st.text("")



     # following lines create boxes in which user can enter data required to make prediction

    Nitrogen=st.number_input("Nitrogen value")
    st.text("")

    Phosphorous=st.number_input("Phosphorous value")
    st.text("")

    Potassium=st.number_input("Potassium value")
    st.text("")

    ph=st.slider("Choose ph value",0.0,14.0)
    st.text("")

    rainfall=st.slider("Choose rainfall",0.0,300.00)
    st.text("")

    temperature=st.slider("Choose temperature",0.0,100.00)
    st.text("")

    humidity=st.slider("Choose humidity",0.0,100.00)
    
    st.text("")

    
    if st.button("Recommend Crop"):

        result=recommend(Nitrogen,Phosphorous,Potassium,temperature, humidity,ph,rainfall)

        st.success("Your crop is {}".format(result[0]))



    
    st.text("")
    st.text("")
    st.text("")
    st.markdown("<i>Thank you.   Here is a token for the love you shared</i>☮️❤️ ",unsafe_allow_html = True)
    
    st_player("https://soundcloud.com/djady87/usa-for-africa-we-are-the-world",height=150)

if __name__ == '__main__':
    app()