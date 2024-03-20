import json
import time 
import requests

import streamlit as st
from streamlit_lottie import st_lottie #lottieใช้สำหรับรันไฟล์
from streamlit_lottie import st_lottie_spinner

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

<body style="background-color: black;">
</body>
lottie_url_hello = "https://lottie.host/fcd01209-0ad6-4615-8477-c2d5f76624dd/fDSfJEABkm.json"
lottie_hello = load_lottieurl(lottie_url_hello)

st.header("☢ อัตราป่วยตาย ด้วยโรคหลอดเลือดสมองตีบหรืออุดตัน ของโรงพยาบาลที่ให้บริการ 🕵")
st.header("by Varut Pongsai")

#การเรียกใช้งาาน lottie file
st_lottie(lottie_hello, key="hello")
st.balloons()