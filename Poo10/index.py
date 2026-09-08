from Poo10.templates.manterprofissionalui import ManterProfissionalUI
from templates.manterclienteui import ManterClienteUI
from templates.manterservicoui import ManterServicoUI
from templates.manterhorarioui import ManterHorarioUI
import streamlit as st

class IndexUI:
    def main():
        op = st.sidebar.selectbox("Menu", ["Clientes", "Serviços", "Horários", "Profissionais"])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Serviços": ManterServicoUI.main()
        if op == "Horários": ManterHorarioUI.main()
        if op == "Profissionais": ManterProfissionalUI.main()


IndexUI.main()