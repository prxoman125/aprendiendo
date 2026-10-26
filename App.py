import streamlit as st
import math

st.markdown("# Calibracion de Mira")

st.subheader("Sistema Métrico")
valor = st.number_input(label="Ingresa el valor del objetivo (centimetros)", min_value=1.0, max_value=100.0, value=1.0, step=0.5)
valor_dos = st.number_input(label="Ingresa la distancia al objetivo (metros)", min_value=1.0, max_value=1000.0, value=1.0, step=0.5)

radianes = math.atan((valor / 100) / valor_dos)
grados = math.degrees(radianes)

st.write(f"Los radianes actuales son: {radianes:.6f}")
st.write(f"Los grados actuales son: {grados:.4f}°")

st.subheader("Sistema Imperial")
valor_tres = st.number_input(label="Ingresa el valor del objetivo (pulgadas)", min_value=1.0, max_value=39.37, value=1.0, step=0.5)
valor_cuatro = st.number_input(label="Ingresa la distancia al objetivo (yardas)", min_value=1.0, max_value=1093.61, value=1.0, step=0.5)

distancia_en_pulgadas = valor_cuatro * 36
radianes_uno = math.atan(valor_tres / distancia_en_pulgadas)
grados_uno = math.degrees(radianes_uno)

st.write(f"Los radianes actuales en sistema imperial son: {radianes_uno:.6f}")
st.write(f"Los grados actuales en sistema imperial son: {grados_uno:.4f}°")
