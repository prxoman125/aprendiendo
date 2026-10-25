import streamlit as st
import math as sp
st.markdown("# Calculo de MOA y MRAD")

n1 = st.slider(label = "Altura entre la mira y el cañon en centimetros", min_value = 1, max_value = 10, value = 1, step = 1)
n2 = st.slider(label = "Distancia entre el cañon y el objetivo", min_value = 1, max_value = 1000, value = 1, step = 1)
resultado = sp.atan((n1 / 100) / n2)

st.markdown(f"### El resultado es: {resultado}")
