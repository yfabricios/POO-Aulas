class String:
    def __init__(self, entrada1, entrada2, string):
        self.a = entrada1
        self.b = entrada2
        self.str = string

    def calc(self):
        if self.str == "/":
            return self.a / self.b
        elif self.str == "-":
            return self.a - self.b
        elif self.str == "+":
            return self.a + self.b
        elif self.str == "*":
            return self.a * self.b
        else:
            return "Digite uma Operação valida"

calc1 = String(int(input('Numero: ')), int(input('Numero: ')), str(input('digite +, -, /, *: ')))
print(calc1.calc())
