
def somar_frase(frase):
    soma = 0
    for carac in frase:
        if carac.isdigit():  
            soma += int(carac)
    return soma

frase_principal = somar_frase(str(input("Digite uma frase: ")))
print(frase_principal)