import streamlit as st
import math

st.markdown("# Calibracion de Mira")

valor = st.number_input(label="Ingresa el valor del objetivo (cm)", min_value=1.0, max_value=100.0, value=1.0, step = 1.0)
valor_dos = st.number_input(label="Ingresa la distancia al objetivo (mtrs)", min_value=1.0, max_value=1000.0, value=1.0, step = 1.0)

radianes = math.atan((valor / 100) / valor_dos)

grados = math.degrees(radianes)

st.write(f"Los radianes actuales son: {radianes:.6f}")
st.write(f"Los grados actuales son: {grados:.4f}°")
