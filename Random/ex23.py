import random
import time
from operator import itemgetter

jogadores = {'Jogador1': random.randint(1, 6),
             'Jogador2': random.randint(1, 6),
             'Jogador3': random.randint(1, 6),
             'Jogador4': random.randint(1, 6)}

print('VALORES SORTEADOS!!!')
ranking = []
for k, v in jogadores.items():
    print(f'O {k} tirou o valor {v} no dado!')
    time.sleep(1)
print('-+-' * 25)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}• lugar: {v[0]} com {v[1]}')
