# Exercício Python #028 - Jogo da Adivinhação v.1.0
'''
Escreva um programa que faça o computador "pensar" em
 um número inteiro entre 0 e 5 e peça para o usuário
 tentar descobrir qual foi o número escolhido pelo computador.
 O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint
from time import sleep


computador = randint(0, 5) # Faz o computador "Pensar"
print('-=' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO.....')
sleep(1)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('Computador: GANHEI! eu pensei no número {} e não no {}!'.format(computador, jogador))
