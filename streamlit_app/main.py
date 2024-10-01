import streamlit as st
import display
import display_image
import time
from model_load import model_loader
from model_build import model
from predict import predict

def main():
    # Display the initial landing page
    display.display_page()
    display.guide()
    
    # Upload the image
    uploaded_image = display.button()

    if uploaded_image:
    # If the image is being uploaded, we ask user to click predict button
        time.sleep(2.0)
        image_displayed = display_image.display_image(uploaded_image)
        st.image(image_displayed, 
                 caption='Image is uploaded!', use_column_width=True)
        predict_button = display.predict_button()

        # Ir the predict button is done clicked, then start doing inference
        if predict_button:
            st.write("Wait, we are recognizing who is he/she/it!")

            # Make a progress bar for each step
            # Initializing with 0
            # And progress status
            progress_bar = st.progress(0)
            status_text = st.empty()
            status_text.text("Image processed, proceeding with prediction...")
            progress_bar.progress(25)  # Update progress

            # Load the model
            model_used = model()
            model_fin = model_loader(model_path='C:/Users/Rafli/one-piece-image-classifier/streamlit_app/model_v14.pth', model=model_used)
            progress_bar.progress(50)  # Update progress

            if model_fin is not None:
                status_text.text("Model loaded successfully.")
                progress_bar.progress(75)  # Update progress

                # Run prediction
                top_pr, top_class = predict(input=image_displayed, model=model_fin)
                progress_bar.progress(100)  # Complete progress
                st.write(f"Is he/she/it {top_class}? If yes, great!!!")
            else:
                status_text.text("Model loading failed.")
        else:
            st.write("Click the button, plzz :)")

if __name__ == "__main__":
    main()
    
