def aumentar(n):
    return n + (n * 0.1)


def diminuir(n):
    return n - (n * 0.13)


def dobro(n):
    return n * 2


def metade(n):
    return n/2


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')
