import streamlit as st
st.markdown("# Calculo de MOA y MRAD")

n1 = st.slider(label = "Numero", min_value = 0, max_value = 100, value = 0, step = 1)
n2 = st.slider(label = "Numero 2", min_value = 0, max_value = 100, value = 0, step = 1)
resultado = sp.atan((n1 / 100) / n2)

st.markdown(f"### El resultado de la suma es: {resultado}")
