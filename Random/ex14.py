lista = []
menor = 0
maior = 0

for c in range (0, 5):
    lista.append(int(input(f'Digite o valor na posição {c}: ')))
    if c == 0:
        menor = maior = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]


print(f'Os número digitados foram {lista}')
print(f'O maior numero digitado foi {maior}')
print(f'O menor número digitado foi {menor}')
