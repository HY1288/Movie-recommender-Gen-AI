# created the folder, opened new script
# created the virtual environment by code--> .\.venv\Scripts\activate
# install the libraries in the virtual env using cmd prompt- streamlit, google-generativeai, langchain
# code to install--> pip install streamlit langchain google-generativeai
# to view the front end---> streamlit run app.py

import streamlit as st
import langchain
from langchain import PromptTemplate, LLMChain

# langchain-google-genai
from langchain_google_genai import ChatGoogleGenerativeAI

# Design the page...
st.title("Movie Recommender System using Google Gemini 🎬🍿🥤")
# st.subheader("Please enter the Movie Name")
user_input=st.text_input("Enter a movie title, genre or keywords (e.g. sci-fi)")


# to view your page type-- streamlit run app.py

# LLM Model
demo_template='''Based on the input, here are some recommendations\
    for {user_input}:\n'''
template= PromptTemplate(input_variable=['user_input'], template=demo_template)

# Initialize the Gemini Pro Model

llms= ChatGoogleGenerativeAI(model='gemini-pro', api_key="AIzaSyAuOv1wKhVj_iJzQa5sB9Fp2NOggn1Bvn0")

#generate the recommendations when the user provide input
if user_input:
    prompt=template.format(user_input=user_input)
    recommendations= llms.predict(text=prompt)
    st.write(f"Recommendations for You:\n{recommendations}")
else:
    st.write(" ")

