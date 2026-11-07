import streamlit as st
import sympy as sp

st.markdown("# Calibracion de Optica")
x = sp.Symbol ('x')
e = x**2 2*x**3
st.latex(sp.latex(e)) 
