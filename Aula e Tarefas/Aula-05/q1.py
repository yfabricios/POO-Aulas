class Retangulo:
    def __init__(self):
        self.__base = 0        # atributos escondidos / atributos encapsulados
        self.__altura = 0
    
    def set_base(self, valor):
        if valor < 0: 
            raise ValueError('Valor deve ser positivo')
        self.__base = valor

    def get_base(self):
        return self.__base

    def set_altura(self, valor):
        if valor < 0:
             raise ValueError('Valor deve ser positivo')
        self.__altura = valor

    def get_altura(self):
        return self.__altura

    def diagonal(self):
        return (self.__base ** 2 + self.__altura ** 2) ** (1/2)

class UI:
    @staticmethod
    def main():
        r = Retangulo()
        r.set_base(float(input('Base: ')))
        r.set_altura(float(input('altura: ')))
        print(f'O retângulo de base = {r.get_base()}, e altura = {r.get_altura()} ')
        diagonal = r.diagonal()
        print(f'tem diagonal = {diagonal}')

UI.main()