import streamlit as st

def character_script(input, input_prob):
    if input_prob > 0.6:
        st.markdown(f"## This is {input}") 
        st.write('This is a character from one piece')
    else:
        st.markdown(f"## Sorry!")
        st.write('We are uncertain who is this')
        st.write(f"But, probably it is {input} with {input_prob*100:.4}% probability")
