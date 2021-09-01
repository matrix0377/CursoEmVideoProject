# Exercício Python #037 - Conversor de Bases Numéricas
'''
Escreva um programa em Python que leia um número inteiro qualquer e
peça para o usuário escolher qual será a base de conversão: 1 para
binário, 2 para octal e 3 para hexadecimal.
'''

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{num} convertido para BINÁRIO é igual a \033[34m{bin(num) [2:]}\033[m')
elif opção == 2:
    print(f'{num} convertido para OCTAL é igual a \033[34m{oct(num) [2:]}\033[m')
elif opção == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a \033[33m{hex(num) [2:]}\033[m')
else:
    print('Opção invalida. Tente novamente.')

