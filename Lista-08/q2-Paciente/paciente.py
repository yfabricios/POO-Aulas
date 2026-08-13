from datetime import datetime

class Paciente:
    def __init__(self, nome, cpf, telefone, nasc):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__nasc = nasc

    def idade(self):
        hoje = datetime.now()
        idade = hoje.year - self.__nasc.year - ((hoje.month, hoje.day) < (self.__nasc.month, self.__nasc.day ))
        return idade

    def __str__(self):
        return f'Nome: {self.__nome}, CPF: {self.__cpf}, Telefone {self.__telefone}, Nascimento: {self.__nasc}'
    
    def to_json(dic):
        return Paciente(dic["id"], dic["nome"], dic["email"], dic["fone"])

    @staticmethod
    def from_json(dic):
        return Paciente(dic["id"], dic["nome"], dic["email"], dic["fone"])        

        