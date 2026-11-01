import streamlit as st

# Título en el área principal
st.markdown("## Calibración Matemática")

# --- MENÚ DESPLEGABLE A LA IZQUIERDA (SIDEBAR) ---
with st.sidebar:
    st.header("⚙️ Panel de Control")
    
    # 1. Menú desplegable para elegir una opción
    opcion = st.selectbox(
        "Selecciona el método:",
        ["Regresión Lineal", "Ajuste Polinomial", "Interpolación"]
    )
    
    # 2. Entrada numérica para modificar datos
    parametro_a = st.number_input("Valor del Parámetro A:", value=1.0, step=0.1)
    
    # 3. Deslizador (Slider) para otra variable
    tolerancia = st.slider("Nivel de Tolerancia:", min_value=0.001, max_value=0.100, value=0.050, step=0.005)


# --- ÁREA PRINCIPAL (Muestra los resultados usando los datos de la izquierda) ---
st.write(f"### Resultados usando: {opcion}")

col1, col2 = st.columns(2)

with col1:
    st.metric(label="Parámetro A ingresado", value=parametro_a)

with col2:
    st.metric(label="Tolerancia matemática", value=tolerancia)
