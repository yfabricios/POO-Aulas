from datetime import datetime

class Paciente: 
    def __init__(self, id, nome, cpf, telefone, nascimento):
        self.set_id(id)
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_telefone(telefone)
        self.set_nascimento(nascimento)

    def set_id(self, v):
        if v < 0: raise ValueError()
        self.__id = v

    def set_nome(self, n):
        if n == "": raise ValueError()
        self.__nome = n

    def set_cpf(self, n):
        if n == "": raise ValueError()
        self.__cpf = n

    def set_telefone(self, n):
        if n == "": raise ValueError()
        self.__telefone = n

    def set_nascimento(self, v):
        if v > datetime.now(): raise ValueError()
        self.__nascimento = v

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_cpf(self): return self.__cpf
    def get_telefone(self): return self.__telefone
    def get_nascimento(self): return self.__nascimento

    def idade(self):
        idade = datetime.now() - self.__nascimento
        meses = idade.days % 365 // 30
        anos = idade.days // 365
        return f"{idade}, {meses}, {anos}"
    
    def __str__(self):
        return f'Id: {self.__id}, Nome: {self.__nome}, cpf: {self.__cpf}, telefone: {self.__telefone}, Nascimento: {self.__nascimento}.'

class UI:
    __pacientes = []

    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 1: UI.listar()
            if op == 1: UI.atualizar()
            if op == 1: UI.excluir()
            if op == 1: UI.pesquisar()
            if op == 1: UI.aniversariante()

    @staticmethod
    def menu():
        print('1 - Inserir')
        print('2 - Listar')
        print('3 - Atualizar')
        print('4 - Excluir')
        print('5 - Pesquisar')
        print('6 - Aniversariante')
        print('9 - Fim')
        op = int(input('Opção: '))
        return op
    
    @classmethod
    def inserir(cls):
        id = int(input('Id: '))
        nome = int(input('Nome: '))
        cpf = int(input('Cpf: '))
        telefone = int(input('Telefone: '))
        nascimento = datetime.strptime(input('Nascimento: '), "%d/%m/%Y")

        x = Paciente(id, cpf, nome, telefone, nascimento)

        cls.__pacientes.append(x)

    @classmethod
    def listar(cls):
        for x in cls.__pacientes: print(x, x.idade())
    
    @classmethod
    def atualizar(cls):
        for x in cls.__pacientes: print(x)
        id = int(input('Novo Id: '))
        for x in cls.__pacientes:
            nome = int(input('Novo Nome: '))
            cpf = int(input('Novo Cpf: '))
            telefone = int(input('Novo Telefone: '))
            nascimento = datetime.strptime(input('Novo Nascimento: '), "%d/%m/%Y")
            x.set_nome(nome)
            x.set_cpf(cpf)
            x.set_telefone(telefone)
            x.set_nascimento(nascimento)

    @classmethod
    def excluir(cls):
        for x in cls.__pacientes: print(x)
        id = int(input("Id de exclusão: "))
        for x in cls.__pacientes:
            if x.get_id == id:
                cls.__pacientes.remove(x)

    @classmethod
    def pesquisar(cls):
        i = input('Informe as inicais')
        for x in cls.__pacientes:
            if x.get_nome().startswith(i): print(x)

    @classmethod
    def aniversariante(cls):
        m = int(input('Informe o mês: '))
        for x in cls.__pacientes:
            if x.get_nascimento().mouth == m: print(x)

UI.main()
        


    















