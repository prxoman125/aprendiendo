import streamlit as st
import sympy as sp

st.markdown("# Calibración de Óptica")
x = sp.Symbol('x')
e = x**2 + 2*x**2

eq_latex = sp.latex(e)

st.latex(rf"{{\Huge {eq_latex}}}")  # Gigante
