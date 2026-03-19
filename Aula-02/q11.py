def Diagonal(b, h):
    hipotenusa = (b**2 + h**2)**(1/2)
    return hipotenusa

x, y = int(input('base: ')), int(input('altura: '))
print(Diagonal(3, 4))