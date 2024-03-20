import json
import time
import requests
import streamlit as st
from streamlit_lottie import st_lottie, st_lottie_spinner

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/fcd01209-0ad6-4615-8477-c2d5f76624dd/fDSfJEABkm.json"
lottie_hello = load_lottieurl(lottie_url_hello)

# Set the background color - this should be in the Streamlit app's config file, not in the code itself
# st.markdown("""<style>body {background-color: #000;}</style>""", unsafe_allow_html=True)

st.header("☢ อัตราป่วยตาย ด้วยโรคหลอดเลือดสมองตีบหรืออุดตันของโรงพยาบาลที่ให้บริการ 🕵")
st.header("by Varut Pongsai")

# Display the lottie animation
st_lottie(lottie_hello, key="hello")
st.balloons()