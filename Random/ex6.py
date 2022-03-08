import random

soma = cont = 0

print(10 * '-+-')
print('VAMOS JOGAR PAR OU ÍMPAR')
print(10 * '-+-')
while True:
    pc = random.randint(0, 11)
    y = input('Escolha PAR ou ÍMPAR [P/I] ')[0]
    x = int(input('Escolha um número: '))
    soma = x + pc
    print(f'O pc escolheu o número {pc} e vc {x} e os valores somados foi {soma}.')
    if soma % 2 == 0:
        print('É um número PAR!')
    else:
        print('É um número ÍMPAR')
    if y == 'p' and soma % 2 == 0:
        print('VOCÊ VENCEU!!!')
    else:
        print(f'GAMER OVER! Você venceu {cont} vezes!')
        break
    cont += 1
print('FIM')



