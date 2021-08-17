# Curso Python #16 - Tuplas
# As Tuplas são imutáveis

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)

# print(lanche[1]) fazer fatiamento, mostra o elemento com índice 1
# print(lanche[3])
# print(lanche[-2])
# print(lanche[1:3]) desconsidera o último elemento mostra de [1:2]
# print(lanche[2:]) 2 até o final
# print(lanche[:2]) início até o elemento 2 - desconsidera o último elemento
# print(lanche[-2:]) vai da pizza até o final
# print(lanche[-3:]) suco até o final
# Se a programação estiver parada, posso mudar manualmente

# for cont in range(0, len(lanche)):
#      print(lanche[cont])

# outro jeito de enumerar
# for pos, comida in enumerate(lanche):
#   print(f'Eu vou comer {comida} na posição {pos}')

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

# print(sorted(lanche)) --> ordenar na ordem (não muda a tupla, mas pode mostrar em ordem
# print(lanche)

