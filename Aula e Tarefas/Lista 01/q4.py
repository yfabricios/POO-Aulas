class Cinema:
    def __init__(self, dia, horario):
        self.d = dia
        self.hora = horario

    def calc(self, idade):

        if 1 <= idade <= 18: 
            if self.d == 'segunda' or self.d == 'terça' or self.d == 'quinta':
                return f'O valor da entrada é R$ 8,00'
            
            elif self.d == 'quarta':
                return f'O valor da entrada é R$ 8,00'
            
            elif self.d == 'sexta' or self.d == 'sabado' or self.d == 'domingo':
                if self.hora >= 17:
                    return f'O valor da entrada é R$ 15,00'
                else:
                    return f'O valor da entrada é R$ 10,00'
            
        if 19 <= idade <= 200:
            if self.d == 'segunda' or self.d == 'terça' or self.d == 'quinta':
                return f'O valor da entrada é R$ 16,00'
            
            elif self.d == 'quarta':
                return f'O valor da entrada é R$ 8,00'
            
            elif self.d == 'sexta' or self.d == 'sabado' or self.d == 'domingo':
                if self.hora >= 17:
                    return f'O valor da entrada é R$ 30,00'
                else:
                    return f'O valor da entrada é R$ 20,00'

cinema = Cinema(str(input('Escreva o dia da Semana: ')), int(input('Escreva um Horário: ')))
print(cinema.calc(int(input('Escreva sua Idade para vê se tem Meia-Inteira para Você: '))))