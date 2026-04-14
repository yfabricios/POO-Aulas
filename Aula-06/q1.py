# Entidade
class Triangulo:
    def __init__(self):
        self.__b = 0.0
        self.__h = 0.0
    def set_base(self, v):
        if v >= 0: self.__b = v
        else: raise ValueError()
    def set_altura(self, v):
        if v >= 0: self.__h = v
        else: raise ValueError()
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h
    def calc_area(self):
        return self.__b * self.__h / 2

class Circulo:
    def __init__(self):
        self.__raio = 0.0
    def set_raio(self, v):
        if v >= 0: self.__raio = v
        else: raise ValueError()
    def get_raio(self):
        return self.__raio
    def calc_area(self):
        return (self.__raio * 3.14) ** 2
    def calc_circunferencia(self):
        return (self.__raio * 2 * 3.14)

class Viagem:
    def __init__(self):
        self.__distancia = 0.0
        self.__tempo = 0.0
    def set_distancia(self, d):
        if d >= 0: self.__distancia = d
        else: raise ValueError()
    def set_tempo(self, t):
        if t >= 0: self.__tempo = t
        else: raise ValueError()
    def get_distancia(self):
        return self.__distancia
    def get_tempo(self):
        return self.__tempo
    def velocidade_media(self):
        return self.__distancia / self.__tempo

class Conta_Bancaria:
    def __init__(self):
        self.__nome = str
        self.__num_conta = 0.0
        self.__saldo = 0.0
    def get_nome(self):
        return self.__nome
    def set_num_conta(self, v):
        if v >= 0: self.__num_conta = v
        else: raise ValueError()
    def get_num_conta(self):
        return self.__num_conta
    def set_saldo(self, v):
        if v >= 0: self.__saldo = v
        else: raise ValueError()
    def get_saldo(self):
        return self.__saldo
    def metodos(self, metodo, valor):
        if metodo == "d":
            self.sald += valor
            return valor

        elif metodo == "s":
            self.sald -= valor
            return valor

        else: raise ValueError("Digite uma Operação valida")

def conta_bancaria():
        print("Cálculo da Velocidade Media")
        x = Conta_Bancaria()
        x.set_num_conta(float(input("Informe o Número da Conta: ")))     # método de instância
        x.set_saldo(float(input("Informe o seu Saldo: ")))     # método de instância
        metodos = x.metodos()
        print(f"Conta Bancaria de {x.get_nome()}, tem numero de conta: {x.get_num_conta()}, Saldo Antigo: {x.get_saldo}.\n  Novo Valor Bancario = {metodos})
    
    




# Interface com usuário (User Interface) - prints, inputs
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.triangulo()
            if op == 2: UI.circulo()
            if op == 3: UI.viagem()
            if op == 4: UI.conta_bancaria()

    @staticmethod
    def menu():
        print("1-Triângulo 2-Círculo 3-Viagem 4-Conta Bancária 5-Ingresso 9-Fim")
        op = int(input("Informe uma opção: "))
        return op    

    @staticmethod
    def triangulo():
        print("Cálculo da área do triângulo")
        x = Triangulo()
        x.set_base(float(input("Informe o valor da base: ")))     # método de instância
        x.set_altura(float(input("Informe o valor da altura: ")))
        area = x.calc_area()
        print(f"Um triângulo com base {x.get_base()} e altura {x.get_altura()} tem área = {area}")

    @staticmethod
    def circulo():
        print("Cálculo da área e circunferencia do Circulo")
        x = Circulo()
        x.set_raio(float(input("Informe o valor da raio: ")))     # método de instância
        area = x.calc_area()
        circunferencia = x.calc_circunferencia()
        print(f"Um Circulo com raio {x.get_raio()}, tem área = {area}, e circunferencia = {circunferencia}")

    @staticmethod
    def viagem():
        print("Cálculo da Velocidade Media")
        x = Viagem()
        x.set_distancia(float(input("Informe o valor da distancia: ")))     # método de instância
        x.set_tempo(float(input("Informe o valor do tempo: ")))     # método de instância
        vel_med = x.velocidade_media()
        print(f"Uma Velocidade Media com distancia = {x.get_distancia()}, e tempo = {x.get_tempo()}. Tem Velocidade Media = {vel_med}km/h")

    @staticmethod
    

UI.main()