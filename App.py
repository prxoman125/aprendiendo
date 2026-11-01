import streamlit as st
import math
st.markdown("# Calibracion Matematica")
with st.sidebar:
    st.header("Parametros de entrada")

    valor_cm = st.number_input("Altura entre la mira y el cañon en Centimetros", min_value = 1, max_value = 50, value = 1, step =1)
    distancia_mtrs = st.number_input("Distancia al objetivo y el cañon en Metros", min_value = 1, max_value = 1500, value = 1, step = 1)
a = math.atan((valor_cm / 100) / distancia_mtrs)
st.write(f"El valor de los radianes es : {a}")
