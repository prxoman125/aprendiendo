import streamlit as st
import math
st.markdown("# Calibracion Matematica")
with st.sidebar:
    st.header("Calibracion Matematica")

opcion = st.selectbox(
    "Selecciona o ingresa el valor:",
    ["Altura entre el cañon y la mira en Centimetros", "Distancia en Metros"]
)
