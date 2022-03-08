def maior(* num):
    cont = maior = 0
    print('~+' * 25)
    print('\nAnalisando os valores passados: ')
    for valor in num:
        print(f'{valor}', end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont = cont + 1
    print(f'Foram informados {cont} valores. ')
    print(f'O maior valor informando foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()