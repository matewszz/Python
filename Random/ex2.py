x = 0
cont = 0
soma = 0

while x != 999:
    x = int(input('Digite um número: '))
    cont = cont + 1
    soma = soma + x
print('Voce digitou {} numeros e a soma entre eles é {}.'.format(cont - 1, soma - 999))