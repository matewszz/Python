import random

numeros = []

def sorteia(numeros):
    x = soma = 0
    for c in range(0, 5):
        numeros.append(random.randint(0, 10))
    print(f'Números sorteados: {numeros}')
    for valor in numeros:
        if valor % 2 == 0:
            soma = soma + valor
    print(f'A somatoria dos numeros pares: {soma}')


sorteia(numeros)