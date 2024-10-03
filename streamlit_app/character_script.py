import streamlit as st
import json

def json_parser():
    # JSON's parser must met utf-8 encoding
    with open('C:/Users/Rafli/one_piece_image_classifier/character_info.json', 'r', encoding='utf-8') as f:
        description = json.load(f)
        return description 
    
def character_script(input, input_prob):
    description = json_parser()

    # Here, I tried to get key that matches the input arg (top_class from predict.py)
    char_info   = description.get(input)
    if input_prob > 0.6:
        st.markdown(f"## This is {input}") 
        if char_info:
            st.write(char_info["info"])
    else:
        st.markdown(f"## Sorry!")
        st.write('We are uncertain who is this')
        st.write(f"But, probably it is {input} with {input_prob*100:.4}% probability")
