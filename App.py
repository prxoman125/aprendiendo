import streamlit as st
import math

st.markdown("# Calibracion de Mira")

# Inputs de usuario
valor = st.number_input(label="Ingresa el valor del objetivo (cm/pulgadas)", min_value=1.0, max_value=100.0, value=1.0)
valor_dos = st.number_input(label="Ingresa la distancia al objetivo", min_value=1.0, max_value=1000.0, value=1.0)

# Cálculo en radianes
# Nota: Asegúrate de usar math.atan en lugar de st.atan (Streamlit no tiene función .atan)
radianes = math.atan((valor / 100) / valor_dos)

# Conversión opcional a grados para que sea más fácil de leer
grados = math.degrees(radianes)

# MOSTRAR LOS RESULTADOS CORRECTOS
st.write(f"Los radianes actuales son: {radianes:.6f}")
st.write(f"Los grados actuales son: {grados:.4f}°")
