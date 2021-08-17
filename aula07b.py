# Modo normal
print('Normal')
nome = input('Qual é seu nome? ')
print('Normal:')
print('Prazer em te conhecer {}!'.format(nome))
print('='*60)
# Em 20 caracteres
print('Em 20 caracteres:')
print('Prazer em te conhecer {:20}!'.format(nome))
print('='*60)
# Alinhamento a Direita
print('Alinhamento a Direita')
print('Prazer em te conhecer {:>20}!'.format(nome))
print('='*60)
# Alinhamento a Esquerda
print('Alinhamento a Esquerda')
print('Prazer em te conhecer {:<20}!'.format(nome))
print('='*60)
# Alinhamento Centralizado
print('Alinhamento Centralizado')
print('Prazer em te conhecer {:^20}!'.format(nome))
print('='*60)
# Centralizado iguais em Volta
print('Centralizado iguais em volta')
print('Prazer em te conhecer {:=^20}!'.format(nome))
print('='*60)