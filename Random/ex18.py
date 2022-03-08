lista = [[],[]]
impar = par = 0

for c in range(1,8):
    x = int(input(f'Digite o {c}o numero: '))
    if x % 2 == 0:
        lista[0].append(x)
    else:
        lista[1].append(x)

lista[0].sort()
lista[1].sort()
print(f'Os números ímpares foram: {lista[1]}')
print(f'Os números pares foram: {lista[0]}')
