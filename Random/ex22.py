dados = {}

dados['Nome'] = input('Nome: ')
dados['media'] = float(input('Média: '))

print('-+-' * 20)

if dados['media'] >= 7:
    dados['situação'] = 'APROVADO'
elif 5 <= dados['media'] < 7:
    dados['situação'] = 'RECUPERAÇÃO'
else:
    dados['situação'] = 'REPROVADO'
for k, v in dados.items():
    print(f'{k} é igual a {v}')

