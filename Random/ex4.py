cont = soma = 0

while True:
    x = int(input('Digite um número: '))
    if x == 999:
        break
    cont += 1
    soma = soma + x
print(f'Você digitou {cont} números e a soma entre eles é {soma}.')