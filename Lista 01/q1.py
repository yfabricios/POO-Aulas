class Raio:
    def __init__(self, raio):
        self.pi = float(3.14)
        self.r = raio
    def calc(self):
        area = self.pi * (self.r ** 2)
        perimetro = (2 * self.pi) * self.r
        return area, perimetro

raio = Raio((float(input('Raio: '))))
print(raio.calc())