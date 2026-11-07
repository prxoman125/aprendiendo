import streamlit as st

st.markdown("# Calibracion Matematica")

st.sidebar.title("Menú de Configuración")
distancia = st.sidebar.slider("Distancia (m)", 0, 1000, 100)
unidad = st.sidebar.radio("Unidades", ["MOA", "MRAD"])
