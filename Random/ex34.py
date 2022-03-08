def fatorial(n):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return print(f'{f}')


x = int(input('Fatorial do número: '))
fatorial(x)
