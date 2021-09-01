# Exercício Python #039 - Alistamento Militar
'''
 Faça um programa que leia o ano de nascimento de um jovem e informe,
 de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
 se é a hora exata de se alistar ou se já passou do tempo do alistamento.
 Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')
if idade == 18:
    print('Você tem que se alistar \033[31mIMEDIATAMENTE!\033[m')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento')
    ano = atual + saldo
    print(f'Seu alistamento será em \033[32m{ano}.\033[m')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há \033[33m{saldo} anos.\033[m')
    ano = atual - saldo
    print(f'Seu alistamento foi em \033[31m{ano}.\033[m')

