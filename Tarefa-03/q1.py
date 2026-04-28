class Viagem:
    def __init__(self, dest, dist, lt):
        self.set_destino(dest)
        self.set_distancia(dist)
        self.set_litros(lt)

    def set_destino(self, d):
        self.__dest = d

    def set_distancia(self, d):
        if d >= 0: self.__dist = d
        else: raise ValueError()

    def set_litros(self, l):
        if l >= 0: self.__lt = l
        else: raise ValueError()

    def get_destino(self):
        return self.__dest

    def get_distancia(self):
        return self.__dist

    def get_litros(self):
        return self.__lt

    def calc_consumo(self):
        return self.__dist / self.__lt

    def __str__(self):
        return f"Seu destino é: {self.__dest}, Distancia = {self.__dist}Km, Litros = {self.__lt}l"

class Pais:
    def __init__(self, n, p, a):
        self.set_nome(n)
        self.set_populacao(p)
        self.set_area(a)

    def set_nome(self, v):
        self.__n = v

    def set_populacao(self, v):
        if v >= 0: self.__p = v
        else: raise ValueError()

    def set_area(self, v):
        if v >= 0: self.__a = v
        else: raise ValueError()

    def get_nome(self):
        return self.__n

    def get_populacao(self):
        return self.__p

    def get_area(self):
        return self.__a

    def calc_densidade(self):
        return self.__p / self.__a

    def __str__(self):
        return f"Seu destino é: {self.__n}, População = {self.__p}, area = {self.__a}km"
    
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 2:
            op = UI.menu()
            if op == 1: UI.viagem()
            if op == 2: UI.pais()

    @staticmethod
    def menu():
        print("1 - Viagem")
        print("2 - Pais")
        op = int(input("Informe uma opção: "))
        return op    

    @staticmethod
    def viagem():
        print("Cálculo da área e da diagonal do retangulo")
        dest = (str(input("destino: ")))
        dist = (float(input("distancia: ")))
        litro = (float(input("litros: ")))
        x = Viagem(dest, dist, litro)
        consumo = x.calc_consumo()
        print(x)
        print(f"Seu Consumo é: {consumo}")
        print("="*100)

    def pais():
        print("Cálculo da área e da diagonal do retangulo")
        n = (str(input("Nome: ")))
        p = (float(input("População: ")))
        a = (float(input("Área: ")))
        x = Pais(n, p, a)
        densidade = x.calc_densidade()
        print(x)
        print(f"Sua Densidade é: {densidade}")
        print("="*100)

UI.main()