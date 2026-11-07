import streamlit as st

st.markdown("# Calibracion Matematica")

st.sidebar.title("Menú de Configuración")
a = st.input_number (label = "Distancia entre la mira y el objetivo", min_value = 1, max_value = 1500, value = 1, step = 1)
