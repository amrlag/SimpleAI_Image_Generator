import streamlit as st
import os
from dotenv import load_dotenv
import openai
#hide the default footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
load_dotenv()
#getting my API key from my .env
openai.api_key=os.getenv("OPENAI_API_KEY") 

# fonction pour générer une image avec DALL-E
def generate_image_using_openai(input_text):
    response=openai.Image.create(
        prompt=input_text,
        n=1,
        size="1024x1024"
    )
    image_url=response['data'][0]['url']
    return image_url
#using streamlit framework to design my application quickly and easily
st.title("Bienvenue sur mon générateur d'image artificiel")
st.subheader("")
txt=st.text_area(
    "MADE WITH LOVE BY AMR ♡ ♥💕❤😘",
    "L'objectif est de générer une image en fonction du texte que vous allez insérer. \n"
    "Il s'agit d'une version beta vouée à évoluer.\n"
    "Le calibrage et rendu des images peut manquer de calibrage."
)

input_text=st.text_input("Entrez votre texte ici")

if input_text is not None:
    if st.button("Valider"):
        with st.spinner('Création en cours...'):
            st.write(f'You wrote {len(input_text)} characters.')
            image_url=generate_image_using_openai(input_text)
            st.image(image_url)
