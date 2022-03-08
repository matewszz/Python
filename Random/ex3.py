soma = 0
cont = 0
x = 0
w = ''
maior = menor = 0

print('-*-' * 15)
print('Caso queira parar de adc numeros digite [999]. ')
print('-*-' * 15)


while w in 'Ss':
    x = int(input('Digite um número: '))
    w = input('Deseja continuar? [N,S] ')[0]
    cont = cont + 1
    soma = soma + x
    if cont == 1:
        maior = menor = x
    else:
        if x > maior:
            maior = x
        if x < menor:
            menor = x

print('A soma de todos os produtos é {}, e a divisão dos valores {}'.format(soma, soma / cont))
print('O maior número digitado foi {} e o menor foi {}'.format(maior, menor))

print('FIM')
