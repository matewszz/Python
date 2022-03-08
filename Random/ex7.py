print('-+-' * 4)
print('CADASTRO')
print('-+-' * 4)

idade = masculino = mulheres = 0
x = ''

while x in 'Ss':
    i = int(input('\n'' Qual é a sua idade? '))
    s = input(' Qual é o sexo? [M/F] ')
    x = input('\n'' Deseja continuar? [S/N] ')
    if i > 18:
        idade += 1
    if s in 'Mm':
        masculino += 1
    if s in 'Ff' and i < 20:
        mulheres += 1
print('')
print(f'No total tem {idade} pessoa(s) que tem +18!')
print(f'Foram cadastrados {masculino} homem(s)!')
print(f'No total tem {mulheres} mulhere(s) com menos de 20 anos!')
print('FIM DO CADASTRO!')
