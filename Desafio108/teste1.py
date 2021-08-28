# Exercício Python #108 - Formatando Moedas em Python
'''
 Crie um módulo chamado moeda.py que tenha as funções incorporadas
  aumentar(), diminuir(), dobro() e metade(). Faça também um programa
   que importe esse módulo e use algumas dessas funções.
'''

import moeda1
#from Desafio108 import moeda1

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda1.moeda(p)} é {moeda1.moeda(moeda1.metade(p))}')
print(f'O dobro de {moeda1.moeda(p)} é {moeda1.moeda(moeda1.dobro(p))}')
print(f'Aumentando 10%, temos R$ {moeda1.moeda(moeda1.aumentar(p, 10))}')

