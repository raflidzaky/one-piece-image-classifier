import streamlit as st
import display
import display_image
import time

def main():
    display.display_page()
    display.guide()
    
    uploaded_image = display.button()

    if uploaded_image:
        time.sleep(2.0)
        image_displayed = display_image.display_image(uploaded_image)
        st.image(image_displayed, 
                 caption='Image is uploaded!', use_column_width=True)
        display.predict_button()
        
    

if __name__ == "__main__":
    main()
