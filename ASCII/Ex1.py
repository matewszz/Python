from random import randint
conjunto_chave = ''
cripto = ''
descripto = ''

def criptografia(palavra, cripto, conjunto_chave):
    for letra in palavra:
        numero_aleatorio = randint(1,9)
        conjunto_chave += str(numero_aleatorio)
        cripto += str(ord(letra) - numero_aleatorio )
        cripto += ' '
    cripto += conjunto_chave
    return cripto

def descriptografar(palavra, descripto):
    quebra_frase = palavra.split()
    chave = (quebra_frase[len(quebra_frase) - 1])
    c = 0
    quebra_frase.pop()
    for letra in quebra_frase:
        numero_chave = int(chave[c])
        str_int = int(letra)
        descripto += chr(str_int + numero_chave)
        c += 1
    return descripto

while True:
    opcao = input('Escolha 1 para criptografar 2 para descritografar: ')
    if opcao == '1' or opcao == '2':
        break
    else:
        print(f'O valor {opcao} é invalido.')

while True:
    palavra = input('Digite algo: ')
    if len(palavra) <= 128 or opcao == '2':
        break
    else:
        print('Limite maximo de caracteres atingido: maximo(128)')

if opcao == '1':
    resultado_final = criptografia(palavra, cripto, conjunto_chave)
    print(resultado_final)


if opcao == '2':
    resultado_final = descriptografar(palavra, descripto)
    print(resultado_final)