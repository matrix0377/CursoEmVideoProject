# Exercício Python #083 - Validando expressões matemáticas
'''
Crie um programa onde o usuário digite uma expressão qualquer
 que use parênteses. Seu aplicativo deverá analisar se a
 expressão passada está com os parênteses abertos e fechados
 na ordem correta.
'''

expr = str(input('Digite a expressão: '))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb ==')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('sua expressão está válida!')
else:
    print('sua expressão está errada!')