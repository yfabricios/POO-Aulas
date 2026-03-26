class Maior:
    def __init__(self, entrada1, entrada2):
        self.a = entrada1
        self.b = entrada2
    def max(self):
        if self.a == self.b:
            return "Numeros iguais"
        else:
            return max(self.a, self.b)

max1 = Maior(int(input('Numero: ')), int(input('Numero: ')))
print(max1.max())





# a = int(input('Numero: '))
# b = int(input('Numero: '))

# max = max(a, b)
# if a == b:
#     print('Numeros iguais')
# else:
#     print(max)