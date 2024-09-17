import streamlit as st
from PIL import Image
import display_image

def display_page():
    # Func for landing page introduction
    st.title("Ahoy! Welcome to One Piece Image Recognizer!")
    st.write("❓ This site provide a service for you to recognize One Piece characters!")
    st.write("✅ And you will get informations about them!")
    st.write("However, in this version, is limited to 18 characters only :D")
    st.write('---'*5)
    st.write('  ')
    st.write('  ')

def guide():
    # Func for user guide
    st.write('Just upload a random One Piece character images via this button')
    st.write('Gotta make sure that you upload .png/.jpg/.jpeg picture! ;D')
    st.write(' ')
    
def button():
    image = st.file_uploader('Upload image here', type=['png', 'jpg', 'jpeg'],
                             accept_multiple_files=False,
                             key='up145'
                            )      
    return image

def predict_button():
    st.write("Do you want to know who is he/she?")
    st.button("Yes, I want!")