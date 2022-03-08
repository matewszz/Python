temporaria = []
principal = []
pessoas = 0
maior = menor = 0

while True:
    temporaria.append(str(input('Nome? ')))
    temporaria.append(float(input('Peso? ')))
    pessoas += 1
    if pessoas == 0:
        menor = maior = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()
    parar = input('Deseja continuar? [S/N]')[0]
    if parar in 'Nn':
        break

print(f'Foram cadastradas {pessoas} pessoas.')
print(f'Pessoas mais pesadas tem {maior}Kg.')
for p in principal:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'Pessoas mais leves foi {menor}Kg.')
for p in principal:
    if p[1] == menor:
        print(f'{p[0]}')
print('FIM')
