import time


def contador(i, f, p):
    if p < 0:
        p = p * -1
    print('~+' * 20)
    print(f'Contagem de {i} até {f} em {p}')
    if i < f:
        while i <= f:
            print(f'{i}', end=' ')
            time.sleep(0.1)
            i += p
        print('FIM!')
    else:
        while f <= i:
            print(f'{i}', end=' ')
            time.sleep(0.1)
            i = i - p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)

n1 = int(input('Cotagem de: '))
n2 = int(input('Contagem até: '))
n3 = int(input('A cada: '))

contador(n1, n2, n3)
