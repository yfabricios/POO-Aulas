from typing_extensions import Self


class dados_pais:
    def __init__(self, populacao, pais, km):
        self.pais = pais
        self.popula = populacao
        self.km = km
    def calc(self):
        soma = self.popula / self.km
        print(f"densidade demográfica do {self.pais} é de {soma:.2f} hab/km2")
        
dados = dados_pais(str(input("digite o nome do país: ")), int(input("digite o a população do país: ")), int(input("digite a área em km ao quadrado do país: ")))
dados.calculo()
