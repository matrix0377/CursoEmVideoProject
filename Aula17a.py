# exercitando listas

# ou assim: valores = list()
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

#for v in valores:
#   print(f'{v}...', end='')

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

