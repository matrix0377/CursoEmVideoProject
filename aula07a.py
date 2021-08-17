# Aula07a
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}'.format(n1+n2))
# outra forma
print('Outra forma: ')
print('A soma é {}, o Produto é {} e a divisão é {:.3f}'.format(s, m, d))
print('Divisão inteira {} e Potência {}'.format(di, e))
# outra forma
print('='*80)
print('Em uma linha só: ')
print('A soma é {}, o Produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e Potência {}'.format(di, e))
print('='*80)
# Com quebra de linha
print('Com quebra de linha')
print('A soma é {}, \n o Produto é {} e a \n divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e Potência {}'.format(di, e))
print('='*70)
# Com preenchimento no end
print('Com preenchimento no end >>')
print('A soma é {}, \n o Produto é {} e a \n divisão é {:.2f}'.format(s, m, d), end=' >>>> '*2)
print('Divisão inteira {} e \n Potência {}'.format(di, e))


