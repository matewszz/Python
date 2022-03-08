total = 0
cont = 0
barato = ''
menor = 0

while True:
    produto = input('Digite o nome do produto: ')
    valor = float(input('Valor do produto: R$'))
    x = input('\n''Deseja continuar? [S/N] ')
    total = valor + total
    if valor > 1000:
        cont = cont + 1
    if x in 'Nn':
        break
    if cont == 1:
        menor = valor
        barato = produto
print(f'Total gasto nas compras foi de R${total:.1f}!')
print(f'{cont} produto(s) custam mais de R$1000.')
print(f'Produto mais barato foi {barato} no valor de {menor}.')

print('Fim')
