import Projeto

x = float(input('Digite um valor: '))

print(f'A metadade de {Projeto.moeda(x)} é {Projeto.moeda(Projeto.metade(x))}.')
print(f'O dobro de {Projeto.moeda(x)} é {Projeto.moeda(Projeto.dobro(x))}.')
print(f'Aumentando 10% de {Projeto.moeda(x)}, temos {Projeto.moeda(Projeto.aumentar(x))}.')
print(f'Diminuindo 13% de {Projeto.moeda(x)}, temos {Projeto.moeda(Projeto.diminuir(x))}.')
