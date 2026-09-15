import streamlit as st
import pandas as pd
import time
from service import Service

class ManterClienteUI:
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.inserir()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()
    def listar():
        clientes = Service.cliente_listar()
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else:
            list_dic = []
            for obj in clientes: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    def inserir():
        nome = st.text_input("Informe o nome", key="cliente_nome_inserir")
        email = st.text_input("Informe o e-mail", key="cliente_email_inserir")
        fone = st.text_input("Informe o fone", key="cliente_fone_inserir")
        senha = st.text_input("Informe a senha", type="password", key="cliente_senha_inserir")
        if st.button("Inserir", key="btn_atendimento_inserir"):
            Service.cliente_inserir(nome, email, fone, senha)
            st.success("Cliente inserido com sucesso")
            time.sleep(2)
            st.rerun()
    def atualizar():
        clientes = Service.cliente_listar()
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Atualização de Clientes", clientes, key="cliente_select_atualizar")
            nome = st.text_input("Novo nome", op.get_nome(), key="cliente_nome_atualizar")
            email = st.text_input("Novo e-mail", op.get_email(), key="cliente_email_atualizar")
            fone = st.text_input("Novo fone", op.get_fone(), key="cliente_fone_atualizar")
            senha = st.text_input("Nova senha", op.get_senha(), type="password", key="cliente_senha_atualizar")
            
            if st.button("Atualizar", key="btn_cliente_atualizar"):
                id = op.get_id()
                Service.cliente_atualizar(id, nome, email, fone, senha)
                st.success("Cliente atualizado com sucesso")
                time.sleep(2)
                st.rerun()
    def excluir():
        clientes = Service.cliente_listar()
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Exclusão de Clientes", clientes)
            if st.button("Excluir"):
                id = op.get_id()
                Service.cliente_excluir(id)
                st.success("Cliente excluído com sucesso")
                time.sleep(2)
                st.rerun()
                