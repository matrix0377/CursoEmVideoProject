# Exercício Python #111 - Transformando módulos em pacotes
'''
 Crie um pacote chamado utilidadesCeV que tenha dois módulos
  internos chamados moeda e dado. Transfira todas as funções
   utilizadas nos desafios 107, 108 e 109 para o primeiro
  pacote e mantenha tudo funcionando.
'''

from Desafio111.utilidadescev import moeda
# ou

p = float(input('Digite o preço: R$ '))
moeda.resumo(p, 35, 22)

