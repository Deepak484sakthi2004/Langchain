
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os


import google.generativeai as genai


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

from langchain_google_genai import ChatGoogleGenerativeAI
chat = ChatGoogleGenerativeAI(model="gemini-pro")
text = st.text_area("enter a context")
if text is not None:
    res = chat.invoke("Please find the key insights from the below text in maximum of 5 bullet points and also the summary in maximum of 3 sentences and suggest any points that you feel suits or valid :"+"\n"+text)
    
    st.write(res.content)

# model = genai.GenerativeModel('gemini-pro')


# ##initialize our streamlit app

# st.set_page_config(page_title="Gemini Image Demo")

# st.header("Gemini Application")
# input=st.text_input("Input Prompt: ",key="input")


# ## If ask button is clicked

# if input:
    
#     response=model.generate_content(input)
#     st.subheader("The Response is")
#     st.write(response.text)