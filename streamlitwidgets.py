import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name=st.text_input("Enter your name: ")

if name:
    st.write(f"Hello,{name}")

age=st.slider("Select your age: ",0,100,25)

st.write(f"your age is {age}.")

options=["Python","Java","SQL","C"]
choice=st.selectbox("choose your fav language: ",options)
st.write(f"you selected {choice}.")

uploaded_file=st.file_uploader("Choose a cdv file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)