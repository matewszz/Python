while True:
    x = int(input('Quer ver a tabuada de qual número? '))
    if x < 0:
        break
    for c in range(1, 11):
        print(f'{x} * {c} =', c * x)
print('Fim')
