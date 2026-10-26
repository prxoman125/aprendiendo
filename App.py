import streamlit as st
import math
st.markdown ("# Calibracion de Mira")
valor = st.number_input (label = "Ingresa el numero", min_value = 1, max_value = 100, value = 1)
valor_dos = st.number_input (label = "Ingresa el numero", min_value = 1, max_value = 1000, value = 1)
formula = math.atan ((valor / 100) / valor_dos)
st.write(f"Los radianes actuales son: {valor}")

