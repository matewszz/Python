times = ('Palmeiras', 'Atlético-MG', "Fortaleza", "Bragantino", "Athletico-PR", "Flamengo", "Ceará", "Atlético-GO", "Bahia", "Corinthians", "Fluminense", "Santos","Juventude", "Internacional", "Cuiabá",
         "Sport", "São Paulo", "América-MG", "Grêmio", "Chapecoense")

print('-+-' * 15)
print(f' Os times são: {times}•')
print('-+-' * 15)
print(f' OS 5 PRIMEIROS COLOCADOS SÃO: {times [0:5]}')
print('-+-' * 15)
print(f' OS 4 ÚLTIMOS SÃO: {times[16:21]}')
print('-+-' * 15)
print(f' TIMES EM ORDEM ALFABETICA: {sorted(times)}')
print('-+-' * 15)
print(f' A CHAPECOENSE ESTA NA {times.index("Chapecoense")+1}• colocação.')
print('-+-' * 15)
