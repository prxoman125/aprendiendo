import streamlit as st

st.markdown("# Cálculo de MOA y MRAD")

# ---- ESTILOS CSS PERSONALIZADOS PARA CADA SLIDER ----
st.markdown("""
    <style>
    /* Estilos para el primer slider (Slider Verde) */
    div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(1) .stSlider [data-baseweb="slider"] {
        color: #2ECC71 !important;
    }
    div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(1) .stSlider div[role="slider"] {
        background-color: #2ECC71 !important;
    }

    /* Estilos para el segundo slider (Slider Morado) */
    div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(2) .stSlider [data-baseweb="slider"] {
        color: #9B59B6 !important;
    }
    div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(2) .stSlider div[role="slider"] {
        background-color: #9B59B6 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ---- CONTENEDORES Y WIDGETS ----

# Contenedor 1 (Slider Verde)
with st.container():
    n1 = st.slider(label="Número", min_value=0, max_value=10, value=5, step=1, key="slider_verde")

# Contenedor 2 (Slider Morado)
with st.container():
    n2 = st.slider(label="Número 2", min_value=0, max_value=10, value=5, step=1, key="slider_morado")

# ---- RESULTADO ----
resultado = n1 + n2
st.markdown(f"### El resultado de la suma es: {resultado}")

