class Atributos:

    def __init__(self, nome, num_conta, saldo):
        self.nm = nome
        self.num_cont = num_conta
        self.sald = saldo

    def calc(self, metodo, valor):
        if metodo == "d":
            self.sald += valor
            return f"Depósito realizado {self.nm}! Novo saldo: R$ {self.sald:.2f}"
        
        elif metodo == "s":
            self.sald -= valor
            return f"Depósito realizado {self.nm}! Novo saldo: R$ {self.sald:.2f}"

        else:
            return "Digite uma Operação valida"

atributos = Atributos(str(input('nome do titular: ')), int(input('Numero da Conta: ')), int(input('Informe seu Saldo: ')))
print(atributos.calc(str(input('Escreva "d" para Deposito ou "s" para saque: ')), float(input('Valor: '))))