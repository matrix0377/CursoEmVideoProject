# Operações com Tuplas - Aula16

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print('Qual é o tamanho de C ?')
print(len(c))

# quantas vezes aparece o num 5 na tupla
print('Quantos vezes o 5 aparece  ?')
print(c.count(5))

# index de um número, em que posição está o 8
print('qual é o index de 8')
print(c.index(8))

# tuplas aceita dados de tipos diferentes
print('Tuplas aceita dados de tipos diferentes')
pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)

# Você pode apagar uma Tupla, ela é imutável, mas aceita apagá-la
# del(pessoa)



