def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f = f * c
    print(f'Resultado: {f}')


num = int(input('Fatorial de: '))
fatorial(num)
