class Retangulo:

    def __init__(self, b, h):
        self.set_base(b)
        self.set_altura(h)

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
    
    def calc_diagonal(self):
        return (self.__b ** 2 + self.__h ** 2) ** (1/2)

    def __str__(self):
        return f"Base = {self.__b}, Altura = {self.__h}"
    
class Frete:

    def __init__(self, d, p):
        self.set_distancia(d)
        self.set_peso(p)

    def set_distancia(self, v):
        if v >= 0: self.__d = v
        else: raise ValueError()

    def set_peso(self, v):
        if v >= 0: self.__p = v
        else: raise ValueError()

    def get_base(self):
        return self.__d
    
    def get_altura(self):
        return self.__p
    
    def calc_frete(self):
        return 0.01 * self.__d * self.__p

    def __str__(self):
        return f"Peso = {self.__d}Kg, Distancia = {self.__p}Km"
    
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 3:
            op = UI.menu()
            if op == 1: UI.retangulo()
            if op == 2: UI.frete()
            if op == 3: UI.equa()

    @staticmethod
    def menu():
        print("1 - Retangulo")
        print("2 - Frete")
        print("3 - Equação")
        op = int(input("Informe uma opção: "))
        return op    

    @staticmethod
    def retangulo():
        print("Cálculo da área e da diagonal do retangulo")
        b = (float(input("base: ")))
        h = (float(input("altura: ")))
        x = Retangulo(b, h)
        area = x.calc_area()
        diagonal = x.calc_diagonal()
        print(x)
        print(f"Um Retangulo tem Área: {area}, e Diagonal: {diagonal} ")
        print("="*100)
    
    @staticmethod
    def frete():
        print("Cálculo do Frete")
        d = (float(input("distancia: ")))
        p = (float(input("peso: ")))
        x = Frete(d, p)
        frete = x.calc_frete()
        print(x)
        print(f"Um Frete cujo valor total é: {frete} Reais")
        print("="*100)

UI.main()