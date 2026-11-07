import streamlit as st
import sympy as sp

st.markdown("# Calibración de Óptica")
x = sp.Symbol('x')
e = x**2

# Convierte la ecuación a texto LaTeX estándar
eq_latex = sp.latex(e)

# Ejemplos de tamaños (Elige el que mejor se adapte a tu diseño):
st.latex(rf"{{\Large {eq_latex}}}")  # Grande
st.latex(rf"{{\huge {eq_latex}}}")  # Muy grande
st.latex(rf"{{\Huge {eq_latex}}}")  # Gigante
