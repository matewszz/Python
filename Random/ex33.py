def voto(ano):
    x = 2021 - ano
    print(f'Você possui {x} anos de idade.')
    if x >= 18 and x < 65:
        return print('VOTO OBRIGATORIO!')
    elif x >= 65:
        return print('VOTO OPCIONAL!')
    else:
        return print('VOTO NEGADO!')


ano = int(input('Em que ano você nasceu? '))
voto(ano)
