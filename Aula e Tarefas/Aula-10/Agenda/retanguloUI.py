import streamlit as st
from retangulo import Retangulo

class RetanguloUI:
    def main():
        st.header('calculos com retangulo')
        b = st.text_input("base: ")
        h = st.text_input("altura: ")
        if st.button('Calcular'):
            r = Retangulo(float(b), float(h))
            st.write(r)
            st.write(f'Area = {r.calc_area()}')
            st.write(f'Area = {r.calc_diagonal()}')
