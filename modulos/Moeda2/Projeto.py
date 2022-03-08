def resumo(n, a, r):
    print(f'Valor analisado: \tR$ {n:.2f}'.replace('.', ','))
    print(f'Metadade do valor: \tR$ {n/2:.2f}'.replace('.', ','))
    print(f'Dobro do valor: \tR$ {n*2:.2f}'.replace('.', ','))
    print(f'{a}% de aumento: \tR$ {n + (n * a/100):.2f}'.replace('.', ','))
    print(f'{r}% de redução: \tR$ {n - (n * r/100):.2f}'.replace('.', ','))

