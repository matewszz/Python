def area(largura, comprimeto):
    a = l * c
    print(f'O tamanho do terreno de {largura}x{comprimeto} é de {a} m²')


print('-' * 20)
print('Tamanho do terreno')
l = float(input('Largura[m]: '))
c = float(input('Comprimento[m]: '))
area(l, c)
