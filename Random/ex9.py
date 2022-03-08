print('-*-' * 15)
print('SISTEMA CAIXA ELETRONICO')
print('-*-' * 15)

valor = float(input('Qual será o valor sacado? '))
cedula = 100
qtd = 0
total = valor

if valor < 1:
    print('Saque somente acima de R$1! ')

while True:
    if valor >= cedula:
        valor = valor - cedula
        qtd += 1
    else:
        if qtd > 0:
            print(F'Total de {qtd} de cedulas de R${cedula}')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        qtd = 0
        if total == 0:
            break