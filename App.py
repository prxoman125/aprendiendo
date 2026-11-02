import streamlit as st
import math
st.markdown("# Calibracion Matematica")
with st.sidebar:
    st.header("Parametros de entrada")

    valor_cm = st.number_input("Altura entre la mira y el cañon en Centimetros", min_value = 1, max_value = 50, value = 1, step =1)
    valor_mtrs = st.number_input("Distancia al objetivo y el cañon en Metros", min_value = 1, max_value = 1500, value = 1, step = 1)
    caida_cm = st.number_input("Caída de la bala en el blanco (cm)", min_value= 1, max_value=500, value=1, step=1)
    st.header("Parametros en Sistema Imperial")
    value_inch = st.number_input("Altura entre la mira y el cañon en Pulgadas", min_value = 1, max_value = 20, value = 1, step = 1)
    value_yd = st.number_input("Distancia al objetivo y el cañon en Yardas", min_value = 1, max_value = 1640, value = 1, step = 1)
    caida_inch = st.number_input("Caída de la bala en el blanco (Pulgadas)", min_value=1, max_value=200, value=1, step= 1)

st.subheader("Sistema Metrico")

a = math.atan((valor_cm / 100) / valor_mtrs)
st.write(f"El valor de los radianes es : {a}")

b = (caida_cm / 100) / valor_mtrs * 1000 
st.write(f"El valor de los Miliradianes es : {b}")

e = caida_cm / (valor_mtrs * 0.02908)
st.write(f"El valor de los MOA son : {e}")

st.subheader("Sistema Imperial")

c = math.atan((value_inch / 36) / value_yd)
st.write(f"El valor de los radianes es : {c}")

d = (caida_inch / 36) / value_yd * 1000
st.write(f"El valor de los Miliradianes es : {d}")

f = caida_inch / ((value_yd / 100) * 1.047)
st.write(f"El valor de los MOA son : {f}")
