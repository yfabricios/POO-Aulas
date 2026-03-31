class Conta_Agua:

    def __init__(self, mes, ano, consumo):
        self.m = mes
        self.a = ano
        self.cons = consumo

    def calc(self):
        if self.cons <= 10:
            tarifa = 38
        
        elif 11 <= self.cons <= 20:
            tarifa = 38 + (self.cons - 10) * 5
        
        elif self.cons >= 21:
            tarifa = 88 + (self.cons - 20) * 6
        
        print(f'{self.m}/{self.a} da conta e total consumido em m3 é {tarifa} reias')

conta_agua = Conta_Agua(int(input('mes: ')), int(input('ano: ')), int(input('consumo: ')))
conta_agua.calc()

        


    