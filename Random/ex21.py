import random

x = int(input(F'Quantos jogos vc deseja fazer? '))
for c in range(0, x):
    print(f'JOGO:{c}: ', [random.randint(1, 60)], [random.randint(1, 60)], [random.randint(1, 60)], [random.randint(1, 60)], [random.randint(1, 60)], [random.randint(1, 60)])
