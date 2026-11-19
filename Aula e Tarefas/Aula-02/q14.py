import math

def MMC(x, y):
    mmc = math.lcm(x, y)
    return mmc

x, y = int(input('escreva x: ')), int(input('escreva y: '))
print(MMC(x, y))