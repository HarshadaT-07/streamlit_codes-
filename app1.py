import streamlit as st
st.title("Some basic commands in streamlit")
name=st.text_input("Enter your name")

if st.button("submit"):
    st.write("hello",name)