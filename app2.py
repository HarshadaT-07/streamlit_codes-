import streamlit as st

st.title("Some basic commands line slider button etc")
age=st.slider("enter your age", 1, 100)
city=st.selectbox("Choose your city",["delhi", "Pune","Mumbai","Banglore"])

if st.button("show details"):
    st.write("age",age)
    st.write("city",city)