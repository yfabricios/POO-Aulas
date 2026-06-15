# # H = int(input('Horas: '))
# # M = int(input('Minutos: '))
# # S = int(input('Segundo: '))
# # T = int(input('Segundos adiantados: '))

# # H = int(0 <= H <= 23)
# # M = int(0 <= M <= 59)
# # S = int(0 <= S <= 59)
# # T = int(0 <= T <= 10 ** 9)

# # print(H)

# H = int(input())
# M = int(input())
# S = int(input())
# T = int(input())

# # 1. Converte todo o horário inicial para segundos
# segundos_totais = (H * 3600) + (M * 60) + S

# # 2. Adiciona o tempo de adiamento (T)
# segundos_totais = segundos_totais + T

# # 3. Ignora os dias inteiros que se passaram usando o resto da divisão (%)
# # 24 horas tem exatamente 86400 segundos
# segundos_totais = segundos_totais % 86400

# # 4. Transforma o total de segundos de volta para Horas, Minutos e Segundos
# novo_H = segundos_totais // 3600
# resto_segundos = segundos_totais % 3600

# novo_M = resto_segundos // 60
# novo_S = resto_segundos % 60

# # 5. Exibe o resultado linha por linha
# print(novo_H)
# print(novo_M)
# print(novo_S)