import streamlit as st
st.markdown("# Calculo de MOA y MRAD")

n1 = st.slider(label = "Numero", min_value = 0, max_value = 10, value = 5, step = 1)
n2 = st.slider(label = "Numero 2", min_value = 0, max_value = 10, value = 5, step = 1)
resultado = n1 + n2

st.markdown(f"### El resultado de la suma es: {resultado}")
