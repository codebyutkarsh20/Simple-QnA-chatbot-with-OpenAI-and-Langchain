from langchain_community.llms import openai
from dotenv import load_dotenv
import streamlit as st
import os
from streamlit import main

load_dotenv()

## Function to load OpenAI model and get responses
def get_openai_responses(questions):
    llm = openai(
        openai_api_key=os.getenv("OPENAI_API_KEY"), 
        model_name="text-davinci-003" ,
        temperature=0.5
    )
    response = llm(questions)
    return response

## Initialize Streamlit app
st.set_page_config(page_title="QnA Demo")

st.header("Langchain Application")

input_question = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

## If ask button is clicked
if submit and input_question:
    response = get_openai_responses(input_question)
    st.subheader("The response is:")
    st.write(response)