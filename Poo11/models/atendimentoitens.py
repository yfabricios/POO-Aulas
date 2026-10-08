from datetime import datetime

class AtendimentoItens:
    def __init__(self, id, id_atendimento, id_servico, qtd, valor):
        self.set_id(id)
        self.set_id_atendimento(id_atendimento)
        self.set_id_servico(id_servico)
        self.set_qtd(qtd)
        self.set_valor(valor)

    def __str__(self):
        return f"{self.__id} - {self.__data.strftime('%d/%m/%Y %H:%M')} - {self.__queixa_principal}"

    def get_id(self): return self.__id
    def get_id_atendimento(self): return self.__id_atendimento
    def get_id_servico(self): return self.__id_servico
    def get_qtd(self): return self.__qtd
    def get_valor(self): return self.__valor

    def set_id(self, id): self.__id = id
    def set_id_atendimento(self, id_atendimento): self.__data = id_atendimento
    def set_id_servico(self, id_servico): self.__queixa_principal = id_servico
    def set_qtd(self, qtd): self.__historico_saude = qtd 
    def set_valor(self, valor): self.__avaliacao = valor

    def to_json(self):
        dic = {"id":self.__id, "id_atendimento":self.__id_atendimento, "queixa_principal":self.__queixa_principal, "historico_saude":self.__historico_saude, "avaliacao":self.__avaliacao, "prescricao":self.__prescricao, "id_horario":self.__id_horario}
        return dic

    @staticmethod
    def from_json(dic):
        return AtendimentoItens(dic["id"], datetime.strptime(dic["data"], "%d/%m/%Y %H:%M"), dic["queixa_principal"], dic["historico_saude"], dic["avaliacao"], dic["prescricao"], dic["id_horario"])
    