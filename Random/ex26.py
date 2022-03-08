dados = {}
fem = []
cont = media = 0
idade = []
acima = []

while True:
    cont = cont + 1
    dados['Nome'] = input('Nome: ')
    dados['sexo'] = input('Sexo [M/F]: '.upper())
    dados['idade'] = int(input('Idade: '))
    continuar = input('Deseja continuar? ')
    if dados['sexo'] in 'Ff':
        fem.append(dados['Nome'])
    idade.append(dados['idade'])
    media = sum(idade) / cont
    if continuar in 'Nn':
        break

print(f'A)  Ao todo temos {cont} pessoas cadastradas.')
print(f'B)  A média de idade é de {media:5.2f} anos.')
print(f'C)  As mulheres cadastradas foram: {fem}.')
print(f'D)  As pessoas acima da média são: ')
if dados['idade'] >= media:
    for k, v in dados.items():
        print(f'{k} = {v}')
