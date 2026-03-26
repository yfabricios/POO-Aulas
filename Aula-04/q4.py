def soma_virgula(frase):
    soma = 0
    for carac in frase:
        if carac.isdigit():  
            soma += int(carac)
    return soma

frase = soma_virgula(str(input("Digite uma frase: ")))
print(frase)