class Triangulo:
    def __init__(self):
        self.b = 0
        self.h = 0
    def calc_area(self):
        return self.b * self.h / 2


x = Triangulo()

print(x.b, x.h)

x.b = float(input('Base do Triângulo: '))
x.h = float(input('Altura do Triângulo: '))

print(x.b, x.h)

a = x.calc_area()

print(f'A área é: {a:.2f}')

# -------------------------------------------------------------------------------------------------

y = Triangulo()

print(y.b, y.h)

y.b = float(input('Base do 2° Triângulo: '))
y.h = float(input('Altura do 2° Triângulo: '))

print(y.b, y.h)

a = y.calc_area()

print(f'A área é: {a:.2f}')