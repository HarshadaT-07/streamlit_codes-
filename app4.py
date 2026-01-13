import streamlit as st
import google.generativeai as genai

st.title("Welcome to my Streamlit App with Gemini AI")

user_input = st.text_input("Ask me anything!")

genai.configure(api_key="AIzaSyAhZFfWzRppbsqmPc1OQqO6Ew7hQ_CxpqI")

model = genai.GenerativeModel("models/gemini-2.5-flash")

if user_input:
    response = model.generate_content(user_input)
    st.write("Gemini AI says:")
    st.write(response.text)
 
