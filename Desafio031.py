# Exercício Python #031 - Custo da Viagem
'''
Desenvolva um programa que pergunte a distância
de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km
e R$0,45 para viagens mais longas.
'''

distância = float(input('qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distância}Km.')
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print(f'E o preço da sua passagem será de R${preço:.2f}')

