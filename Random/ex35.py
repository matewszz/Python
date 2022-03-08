def ficha(nome='', gols=0):
    nome = n
    if g == '':
        gols = 'ñ foi informado'
    else:
        gols = g
    print(f'O jogador {nome} marcou o total de {gols} gol(s).')


n = (input('Nome do jogador: '))
g = (input('Gols: '))
ficha()