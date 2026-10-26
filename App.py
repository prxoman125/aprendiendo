import streamlit as st
import math
st.markdown ("# Calibracion de Mira")
valor = st.number_input (label = "Ingresa el numero", min_value = 1, max_value = 100, value = 1)
st.write (f "#El numero actual es : {valor}")
