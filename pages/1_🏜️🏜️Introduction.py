import json
import time
import requests
import streamlit as st

st.set_page_config(
    page_title="Data visualization Project",
    page_icon= ":bar_chart:",
)
st.sidebar.success("เลือกรายการด้านบน.")

st.header("# 🍀🍀🍀 การทำจินตทัศน์ข้อมูล....! 👋  🧑🏽‍🏫 ")
st.subheader("1.หลักการและเหตุผล")
st.info("""
        เพื่อช่วยให้ผู้ใช้เข้าใจข้อมูลได้ง่ายขึ้น รวดเร็วขึ้น และมีประสิทธิภาพมากขึ้น
       """)
st.subheader("2.วัตถุประสงค์")
st.info("""
        เพื่อนำเสนอข้อมูลในรูปแบบที่เข้าใจได้ง่ายด้วยวิธีการจินตทัศน์ข้อมูล
        """)
st.balloons()