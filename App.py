import streamlit as st
import math

st.markdown("# Calibracion de Mira")

valor = st.number_input(label="Ingresa el valor del objetivo (cm)", min_value=1.0, max_value=100.0, value=1.0, step = 1.0)
valor_dos = st.number_input(label="Ingresa la distancia al objetivo (mtrs)", min_value=1.0, max_value=1000.0, value=1.0, step = 1.0)

valor_tres = st.number_input(label="Ingresa el valor del objetivo (inch)", min_value=1.0, max_value=100.0, value=1.0, step = 1.0)
valor_cuatro = st.number_input(label="Ingresa la distancia al objetivo (yardas)", min_value=1.0, max_value=1000.0, value=1.0, step = 1.0)

radianes = math.atan((valor / 100) / valor_dos)
radianes_uno = mat.atan((valor_tres * 0.393701) / valor_cuatro * 1.09361)

grados = math.degrees(radianes)
grados_uno = math.degrees(radianes_uno)

st.write(f"Los radianes actuales son: {radianes:.6f}")
st.write(f"Los grados actuales son: {grados:.4f}°")
st.write(f"Los radianes actuales en sistema imperial son: {grdos_uno:.6f}")
st.write(f"Los grados actuales en sistema imperial son: {grdos_uno:.4f}")
