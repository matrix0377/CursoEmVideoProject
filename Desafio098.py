# Exercício Python #098 - Função de Contador
'''
Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo. Seu
programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''
from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='') # se tiver muito delay acrescente depois do end='', flush=True
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='') # se tiver muito delay acrescente depois do end='', flush=True
            sleep(0.5)
            cont -= p
        print('FIM!')


# Programa Principal
contador(0, 100, 10)
print()
contador(10, 0, 2)
print('-=' * 30)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)


