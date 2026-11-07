import streamlit as st
import sympy as sp

st.markdown("# Calibracion de Optica")
x = sp.Symbol ('x')
e = sp.Rational (2,3)
st.latex(sp.latex(e)) 
