import streamlit as st

# Configura la página para usar todo el ancho de la pantalla
st.set_page_config(layout="wide")

# Crea dos columnas con la misma proporción (50% y 50%)
col_izquierda, col_derecha = st.columns(2)

# Columna Izquierda (Vacía)
with col_izquierda:
    st.empty()

# Columna Derecha (Vacía)
with col_derecha:
    st.empty()
