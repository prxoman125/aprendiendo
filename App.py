import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Configuración de la página (Debe ser la primera línea de Streamlit)
st.set_page_config(
    page_title="Calculadora Balística Avanzada",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados para un acabado profesional
st.markdown("""
    <style>
    .main-title {
        font-size: 2.5rem;
        color: #1E3A8A;
        font-weight: 700;
        text-align: center;
        margin-bottom: 20px;
    }
    .metric-container {
        background-color: #F3F4F6;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: bold;
        color: #10B981;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🎯 Calculadora Balística: MOA & MRAD</div>', unsafe_allow_html=True)
st.write("Introduce la distancia al objetivo y la desviación física observada del proyectil para calcular los ajustes necesarios en tu torreta de tiro.")

# --- BARRA LATERAL: ENTRADA DE DATOS ---
st.sidebar.header("📥 Parámetros de Tiro")

# Selección de unidades del usuario
unidad_distancia = st.sidebar.selectbox("Unidad de distancia", ["Yardas", "Metros"])
unidad_desviacion = st.sidebar.selectbox("Unidad de desviación (Caída/Deriva)", ["Pulgadas", "Centímetros"])

st.sidebar.separator()

# Inputs numéricos con rangos lógicos
if unidad_distancia == "Yardas":
    distancia = st.sidebar.number_input("Distancia al objetivo (yd)", min_value=10.0, max_value=2000.0, value=100.0, step=25.0)
else:
    distancia = st.sidebar.number_input("Distancia al objetivo (m)", min_value=10.0, max_value=2000.0, value=100.0, step=25.0)

if unidad_desviacion == "Pulgadas":
    desviacion = st.sidebar.number_input("Desviación del impacto (in)", min_value=-200.0, max_value=2000.0, value=2.0, step=0.5)
else:
    desviacion = st.sidebar.number_input("Desviación del impacto (cm)", min_value=-500.0, max_value=5000.0, value=5.0, step=1.0)

# --- PROCESAMIENTO BALÍSTICO (Conversión a sistema estándar) ---
# Convertir todo a pulgadas/yardas para el cálculo de MOA base
if unidad_distancia == "Metros":
    distancia_yardas = distancia * 1.09361
else:
    distancia_yardas = distancia

if unidad_desviacion == "Centímetros":
    desviacion_pulgadas = desviacion * 0.393701
else:
    desviacion_pulgadas = desviacion

# --- CÁLCULO DE MOA Y MRAD ---
if distancia_yardas > 0:
    # 1 MOA a 100 yardas es aprox 1.047 pulgadas
    moa_exacto = (desviacion_pulgadas / (distancia_yardas / 100.0)) / 1.04719755
    # 1 MRAD = 3.43775 MOA
    mrad_exacto = moa_exacto / 3.43775
else:
    moa_exacto = 0.0
    mrad_exacto = 0.0

# --- PANEL CENTRAL: RESULTADOS ---
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
        <div class="metric-container">
            <h3>Ajuste en MOA</h3>
            <div class="metric-value">{moa_exacto:.2f} MOA</div>
            <p style='color: gray; font-size: 0.9rem;'>Equivale a aprox. <b>{round(moa_exacto * 4)/4:.2f}</b> clicks (en torretas de 1/4 MOA)</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="metric-container">
            <h3>Ajuste en MRAD (Mils)</h3>
            <div class="metric-value">{mrad_exacto:.2f} MRAD</div>
            <p style='color: gray; font-size: 0.9rem;'>Equivale a aprox. <b>{round(mrad_exacto * 10)/10:.1f}</b> clicks (en torretas de 0.1 MRAD)</p>
        </div>
    """, unsafe_allow_html=True)

st.subheader("📊 Tabla de equivalencias de Click según la distancia actual")
st.write(f"A una distancia de **{distancia} {unidad_distancia.lower()}**, cada click desplaza el impacto de la siguiente manera:")

# Valores de referencia de clicks a esa distancia específica
if unidad_desviacion == "Pulgadas":
    val_14_moa = (1.047 * (distancia_yardas / 100)) / 4
    val_01_mrad = (3.6 * (distancia_yardas / 100)) / 10  # 1 mil a 100yd son 3.6 pulgadas
    u = "in"
else:
    # Trabajando en cm / metros
    distancia_metros = distancia if unidad_distancia == "Metros" else distancia / 1.09361
    val_14_moa = (2.908 * (distancia_metros / 100)) / 4 # 1 MOA a 100m son 2.908 cm
    val_01_mrad = (10.0 * (distancia_metros / 100)) / 10 # 1 MRAD a 100m son 10 cm
    u = "cm"

# Tabla de especificaciones de clicks en Markdown
st.markdown(f"""

| Tipo de Torreta | Corrección por Click a esta distancia |
| :--- | :--- |
| **Torreta 1/4 MOA** | `{val_14_moa:.3f} {u}` por click |
| **Torreta 1/2 MOA** | `{val_14_moa * 2:.3f} {u}` por click |
| **Torreta 0.1 MRAD (Mils)** | `{val_01_mrad:.3f} {u}` por click |
""")

# --- GRÁFICO INTERACTIVO: ESCALA DE AJUSTE ---
st.subheader("📈 Gráfico de Proyección de Ajuste")

# Generar puntos de trayectoria lineal simulada para ver la corrección angular
distancias_grafico = np.linspace(10, max(distancia * 1.5, 300), 50)
if unidad_desviacion == "Pulgadas":
    caida_moa_fija = moa_exacto * 1.04719 * (distancias_grafico / 100)
    label_y = "Desviación Proyectada (Pulgadas)"
else:
    # Si es cm usar la distancia en m
    dg_metros = distancias_grafico if unidad_distancia == "Metros" else distancias_grafico / 1.09361
    caida_moa_fija = moa_exacto * 2.908 * (dg_metros / 100)
    label_y = "Desviación Proyectada (Centímetros)"

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=distancias_grafico, 
    y=caida_moa_fija, 
    mode='lines', 
    name='Línea de Corrección Angular',
    line=dict(color='#1E3A8A', width=3)
))
fig.add_trace(go.Scatter(
    x=[distancia], 
    y=[desviacion], 
    mode='markers', 
    name='Tu Impacto Actual',
    marker=dict(color='red', size=12, symbol='cross')
))

fig.update_layout(
    xaxis_title=f"Distancia ({unidad_distancia})",
    yaxis_title=label_y,
    template="plotly_white",
    margin=dict(l=40, r=40, t=20, b=40)
)

st.plotly_chart(fig, use_container_width=True)
