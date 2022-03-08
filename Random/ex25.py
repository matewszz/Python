dados = {}
gol = []
while True:
    dados['jogador'] = input('Nome do jogador: ')
    dados['partidas'] = int(input(f'Quantas partidas {dados["jogador"]} jogou? '))
    for c in range(0, dados['partidas']):
        gol.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    dados['gols'] = gol[:]
    dados['total'] = sum(dados['gols'])
    parar = input('Deseja Parar? [S/N]: ')[0]
    if parar in "Nn":
        break


print("-+-" * 25)
print(dados.items())
print("-+-" * 25)

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}. ')
print("-+-" * 25)
