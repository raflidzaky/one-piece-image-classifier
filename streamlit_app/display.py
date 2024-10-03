import streamlit as st
from PIL import Image
import display_image

'''
    This module has several functions that provide utilities to support basic landing page,
    as users entered the web. Several utilities:
    1. What page that users currently in
    2. Guide for users 
    3. Upload image button, that users could upload to
    4. Button for prediction
'''

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
    # Since I want pass a value for the model, this function
    # will return the image that is being uploaded.
    # Also, this image will be displayed in display_image.py module.    
    return image

def predict_button():
    st.write("Do you want to know who is he/she?")
    # Since I want the predict button returns any value after "clicking action"
    # I make the st.button as return.
    # Hence, this value will be passed as a logic to trigger steps to predict model.
    return st.button("Yes, I want!", key="predict_button")