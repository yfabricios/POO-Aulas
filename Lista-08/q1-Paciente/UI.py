from datetime import datetime
import streamlit as st
from paciente import Paciente

class UI:
    def main():
        st.header('Paciente Cadastro')
        nome = st.text_input("Nome: ")
        cpf = st.text_input("CPF: ")
        telefone = st.text_input("Telefone: ")
        nasc = st.text_input("Nascimento: ")
        
        if st.button('Calcular'):
            r = Paciente(str(nome), str(cpf), str(telefone), datetime.strptime(nasc, "%d/%m/%Y"))
            st.write(r)
            st.write(f'Idade: {r.idade()} anos')

