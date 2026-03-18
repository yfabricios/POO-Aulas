a = int(input('digite um numero: '))
b = int(input('digite um numero: '))
c = int(input('digite um numero: '))
d = int(input('digite um numero: '))

sp = 0
si = 0

if a % 2 == 0:
    sp += a
else:
    si += a
# -------------------------
if b % 2 == 0:
    sp += b
else:
    si += b
# ---------------------------
if c % 2 == 0:
    sp += c
else:
    si += c
# ----------------------------
if d % 2 == 0:
    sp += d
else:
    si += d

print('A soma dos pares é:', sp)
print('A soma dos impares é: ', si)