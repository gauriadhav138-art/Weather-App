import streamlit as st
import requests 
from dotenv import load_dotenv
load_dotenv()
import os
API_KEY = os.getenv('WEATHER_API_KEY')

st.set_page_config(page_title='Weather App',page_icon="⛅")
st.title("Weather App⛅")
st.write('Enter the city and click on the button to fetch the data')
city=st.text_input('Enter the city name')
if(st.button('fetch weather Data')):
    API_URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(API_URL)

    if(response.status_code==200):
        st.success('Weather data fetched successfully')
        data=response.json()
        # extract the data in variables
        temperature=data['main']['temp']
        humidity=data['main']['humidity']
        wind_speed=data['wind']['speed']
        condition=data['weather'][0]['main']
        country= data['sys']['country']
        name= data['name']
        # display the result
        st.header(f'{name},{country}')
        col1,col2 = st.columns(2)

        col1.metric('Temperature',f'{temperature}℃🌡️ ')
        col2.metric('Humidity',f'{humidity}%💦')
        col1.metric('Wind-Speed',f'{wind_speed}m/s🍃')
        col2.metric('Condition',f'{condition}☁️ ')
    else:
        st.error('Invalid City Name')   
