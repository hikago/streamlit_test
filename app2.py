import streamlit as st

st.set_page_config(page_title="Demo", page_icon="", layout="wide")
st.title("hello, Streamlit Community Cloud!")
name = st.text_input('Your Name?')
st.write(f"Nice to meet you")