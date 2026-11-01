import streamlit as st
import math
st.markdown("# Calibracion Matematica")
with st.sidebar:
    st.header("Parametros de entrada")

    valor_cm = st.number_input("Altura entre la mira y el cañon en Centimetros", value = 1, step =1)
