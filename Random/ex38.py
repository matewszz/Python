m50 = maior = m = 0

qtd = int(input('Quantas pessoas deseja cadastrar? '))

for c in range(0, qtd):
    x = int(input(f'Idade {c+1}: '))
    if x >= 50:
        m50 += 1
    m = m + x
    if x >= maior:
        maior = x

print(f'Qtd de pessoas +50: {m50}')
print(f'Media de idades: {m/qtd:.2f}')
print(f'Mais velha: {maior}')
