# Exercício Python #073 - Tuplas com Times de Futebol

times = ('Palmeiras', 'Atlético-MG', 'Fortaleza', 'Bragantino',
         'Athletico-PR', 'Flamengo', 'Ceará-SC', 'Atlético-GO',
         'Bahia', 'Corinthians', 'Fluminense', 'Santos',
         'Juventude', 'Internacional', 'Cuiabá', 'São Paulo',
         'Sport Recife', 'América-MG', 'Grêmio', 'Chapecoense')

print('-=' * 15)
print(f'Lista de times: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
