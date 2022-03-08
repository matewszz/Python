dados = {}

dados['Nome'] = str(input('Nome: '))
dados['Nascimento'] = int(input('Ano de nascimento: '))
dados['Carteira'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['Carteira'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salario'] = float(input('Salario: '))
dados['Idade'] = 2021 - dados['Nascimento']
dados['Aposentadoria'] = (dados['Contratação'] + 30) - dados['Nascimento']
print('-+-' * 30)

for k, v in dados.items():
    print(f'{k} tem valor {v}.')
