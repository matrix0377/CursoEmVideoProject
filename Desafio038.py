# Exercício Python #038 - Comparando números
'''
Escreva um programa que leia dois números inteiros e
compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''

n1 = int(input('Primeiro número: '))
n2 = int(input('Primeiro número: '))
if n1 > n2:
    print('  ---->  \033[33mO PRIMEIRO número é maior\033[m')
elif n2 > n1:
    print(' ---->   \033[33mO SEGUNDO valor é o maior\033[m')
else:
    print('  ---->   \033[34mOs dois são IGUAIS\033[m')

