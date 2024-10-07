import streamlit as st
import json

def json_parser():
    '''
        This function will parse character informations that is mapped as a json.
        It will open the json file and load its value to "description". 
        Input: None
        Output: The value of json (characters' dictionary) that stored in "description
    '''
    # JSON's parser must met utf-8 encoding
    with open('character_info.json', 'r', encoding='utf-8') as f:
        description = json.load(f)
        return description 
    
def character_script(input, input_prob):
    '''
        This function will return the character information, based off what model has predicted. 
        As model predicted the character, the character's name will be used as key to parse its informations.
        Input:
            1. input: This argument will be passed by top 1 model's prediction. 
            2. input_prob: This argument will be passed by top 1's probability. It will be used as a logic to
                           prevent edge-cases (such as submitting non-related images)
        Output: This will return an character informations.
    '''
    description = json_parser()

    # Here, I tried to get key that matches the input arg (top_class from predict.py)
    char_info   = description.get(input)
    if input_prob > 0.6:
        st.markdown(f"## This is {input}") 
        if char_info:
            # Since the character information is stored in inside-key, 
            # hence it is needed to slice the "info" inside-key.
            st.write(char_info["info"])
    elif 0.6 > input_prob > 0.1:
        st.markdown(f"## Sorry!")
        st.write('We are uncertain who is this')
        st.write(f"But, probably it is {input} with {input_prob*100:.4}% probability")
    else:
        st.markdown(f"## Sorry!")
        st.write("We think this is not a One Piece character. Are we wrong?")
