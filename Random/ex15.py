x = list()
stop = ''
maior = 0
menor = 0

while True:
    lista = int(input('Digite um valor: '))
    if lista not in x:
        x.append(lista)
    else:
        print('Número já digitado! Escolha outro valor...')
    stop = input('Deseja continuar? [S/N] '.upper())[0]
    # if lista == 0:
    #     menor = maior = lista
    if lista > maior:
        maior = lista
    if lista < menor:
        menor = lista

    if stop in 'Nn':
        break
print(f'Numeros digitados: {x}')
print(f'O maior numero digitado foi {maior}')
print(f'O menor número digitado foi {menor}')
