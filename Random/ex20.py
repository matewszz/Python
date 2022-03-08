pares = maiorl2 = maior3 = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Adicione um valor para [{l},{c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'{[matriz[l][c]]}', end='')
        if matriz[l][c] % 2 == 0:
            pares = pares + matriz[l][c]
    print()
print('-+-' * 23)

print(F'A soma dos valores pares é de {pares}.')
for l in range(0, 3):
    maior3 = maior3 + matriz[l][2]
print(f'A soma da terceira coluna é de {maior3}.')
for c in range(0, 3):
    if matriz[1][c] > maiorl2:
        maiorl2 = matriz[1][c]
print(f'O maior número da segunda linha é o {maiorl2}.')
print('-+-' * 23)
