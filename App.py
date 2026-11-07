import streamlit as st
import sympy as sp

st.markdown("# Calibración de Óptica")
x = sp.Symbol('x')
e = x**2

# Convierte la ecuación a texto LaTeX estándar
eq_latex = sp.latex(e)

st.latex(rf"{{\Huge {eq_latex}}}")  # Gigante
