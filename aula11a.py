a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))
print('-==-'*15)
print('Os valores são \033[0;37;40m{}\033[m e \033[0;31;40m{}\033[m!!!'.format(a, b))
print('-==-'*15)
# ou
# nome = 'Davi Augusto'
# print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format('\033[4;34m', nome, '\033[m'))
nome = 'Adriana Amaral'
cores = {'limpa':'\033[m',
         'azul': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format(cores['azul'], nome, cores['limpa']))


