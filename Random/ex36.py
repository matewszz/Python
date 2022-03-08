def ajuda(msg):
    help(msg)

comando = ''
while True:
    comando = input('Função ou Biblioteca: ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)