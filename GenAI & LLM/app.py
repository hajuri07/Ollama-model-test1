import os
import streamlit as st
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

load_dotenv()

# (Optional) stop early if key missing
if not os.getenv("LANGCHAIN_API_KEY"):
    st.error("LANGCHAIN_API_KEY not found in .env")
    st.stop()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the question asked."),
    ("user", "{question}")
])

st.title("Fisrt model by HAjuri💪💪🥳🏌️")
input_text = st.text_input("kya hua ree meri jaaan ")

llm = ChatOllama(model="gemma3:1b", temperature=0)
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))
