import streamlit as st
import pandas as pd
import time
from service import Service
from datetime import datetime

class ManterAtendimentoUI:
    def main():
        st.header("Cadastro de Atendimento")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterAtendimentoUI.listar()
        with tab2: ManterAtendimentoUI.inserir()
        with tab3: ManterAtendimentoUI.atualizar()
        with tab4: ManterAtendimentoUI.excluir()

    def listar():
        atendimentos = Service.atendimento_listar()
        if len(atendimentos) == 0: st.write("Nenhum atendimento cadastrado")
        else:
            list_dic = []
            for obj in atendimentos: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        horarios = Service.horario_listar()
        data = st.text_input("Informe a data", datetime.now().strftime("%d/%m/%Y %H:%M"))
        queixa_principal = st.text_input("Informe a queixa principal")
        historio_saude = st.text_input("Informe o historico de saude")
        avaliacao = st.text_input("Informe a avaliação")
        prescricao = st.text_input("Informe a prescrição")
        horario = st.selectbox("Informe o horário", horarios, index=None)
        
        if st.button("Inserir"):
            id_horario = None
            if horario != None: 
                id_horario = horario.get_id()

            data_obj = datetime.strptime(data, "%d/%m/%Y %H:%M")
            Service.atendimento_inserir(data_obj, queixa_principal, historio_saude, avaliacao, prescricao, id_horario)
            st.success("Atendimento inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        atendimentos = Service.atendimento_listar()
        if len(atendimentos) == 0: st.write("Nenhum atendimento cadastrado")
        else:
            horarios = Service.horario_listar()
            op = st.selectbox("Atualização de atendimentos", atendimentos)
            data = st.text_input("Nova data", op.get_data().strftime("%d/%m/%Y %H:%M"))
            queixa_principal = st.text_input("Nova queixa principal", op.get_queixa_principal())
            historico_saude = st.text_input("Novo historico de saude", op.get_historico_saude())
            avaliacao = st.text_input("Nova avaliaçao", op.get_avaliacao())
            prescricao = st.text_input("Nova prescrição", op.get_prescricao())
            horario = st.selectbox("Informe o novo horário", horarios, index=None)

            if st.button("Atualizar"):
                id = op.get_id()
                id_horario = None
                if horario != None:
                    id_horario = op.get_id_horario()

                data_obj = datetime.strptime(data, "%d/%m/%Y %H:%M")
                Service.atendimento_atualizar(id, data_obj, queixa_principal, historico_saude, avaliacao, prescricao, id_horario)
                st.success("Atendimento atualizado com sucesso")
                time.sleep(2)
                st.rerun()
                
    def excluir():
        atendimentos = Service.atendimento_listar()
        if len(atendimentos) == 0: st.write("Nenhum atendimento cadastrado")
        else:
            op = st.selectbox("Exclusão de Atendimentos", atendimentos)
            if st.button("Excluir"):
                id = op.get_id()
                Service.atendimento_excluir(id)
                st.success("Atendimento excluído com sucesso")
                time.sleep(2)
                st.rerun()
                