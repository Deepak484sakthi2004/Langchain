
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os


import google.generativeai as genai


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')


##initialize our streamlit app

st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")
input=st.text_input("Input Prompt: ",key="input")


## If ask button is clicked

if input:
    
    response=model.generate_content(input)
    st.subheader("The Response is")
    st.write(response.text)