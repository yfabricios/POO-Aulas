class Atributos:
    def __init__(self, distancia, horas, minutos):
        self.dist = distancia
        self.hr = horas
        self.min = minutos/60
    def calc(self):
        vm = self.dist / (self.hr + self.min)
        return print(vm, 'km/h')

atributos = Atributos(float(input('Distancia: ')), float(input('Horas: ')), float(input('Minutos: ')))
atributos.calc()