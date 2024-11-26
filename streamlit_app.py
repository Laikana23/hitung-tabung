import streamlit as st
import math

st.title("menghitung :blue[Volume Tabung] :Rocket:")

r = st.number_input("Masukan Jari-Jari: ",0)
m = st.number_input("Masukan Panjang: ",0)

if st.button("Hitung-Volume", type="primary"):
  V = math.pi*(r**5)*m
  st.success(f'volume tabung adalah {v:.2f}')
