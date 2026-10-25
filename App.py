import streamlit as st

# Configura la página para aprovechar el ancho
st.set_page_config(layout="wide")

# ==========================================
# INTERFAZ IZQUIERDA (MENÚ DESPLEGABLE)
# ==========================================
with st.sidebar:
    st.header("⚙️ Panel de Control")
    st.subheader("Ingresa los valores")
    
    # Ejemplo 1: Entrada de texto
    nombre = st.text_input("Nombre del proyectil:", value="Calibre .22")
    
    # Ejemplo 2: Control numérico (para tu app de balística)
    velocidad = st.number_input("Velocidad inicial (m/s):", min_value=0.0, max_value=2000.0, value=340.0)
    
    # Ejemplo 3: Menú desplegable de opciones (Selectbox)
    tipo_polvora = st.selectbox("Tipo de pólvora:", ["Lenta", "Media", "Rápida"])
    
    # Ejemplo 4: Deslizador (Slider)
    angulo = st.slider("Ángulo de disparo (°):", min_value=0, max_value=90, value=45)
    
    # Botón para activar el cálculo
    calcular = st.button("Calcular Trayectoria", type="primary")


# ==========================================
# PANTALLA PRINCIPAL (PARTE DERECHA)
# ==========================================
# De momento se mantiene vacía o con un mensaje de espera
if calcular:
    st.title("📊 Resultados del Cálculo")
    st.success("¡Valores recibidos correctamente en el código!")
    
    # Aquí puedes usar las variables que el usuario ingresó a la izquierda
    st.write(f"Proyectil: **{nombre}**")
    st.write(f"Velocidad: **{velocidad} m/s**")
    st.write(f"Pólvora: **{tipo_polvora}**")
    st.write(f"Ángulo: **{angulo}°**")
else:
    st.info("Introduce los valores en el menú de la izquierda y haz clic en 'Calcular'.")
