num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
       'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
continuar = ''



while continuar in 'Ss':
    x = int(input('Digite número entre 0 e 20: '))
    if 0 <= x <= 20:
        print(num[x])
    else:
        print('Tente novamente. Número somente entre 0 e 20.')
    continuar = input('Deseja continuar? [S/N] '.upper())



