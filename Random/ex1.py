# USANDO UM LAÇO DENTRO DE OUTRO LAÇO #

print('GERADOR DE PA')
print('-*-*-' * 10)

primeiro = int(input('Primeiro termo da PA: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = mais + total
    while cont <= total:
        print('{} -> '.format(termo), end='')
        cont = cont + 1
        termo = termo + razão
    mais = int(input('\n''Quantos termos vc qe mostrar a mais? '))
print('Foi demonstrado {} razões!'.format(cont - 1))