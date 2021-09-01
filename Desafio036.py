# Exercício Python #036 - Aprovando Empréstimo
'''
Escreva um programa para aprovar o empréstimo bancário para
a compra de uma casa. Pergunte o valor da casa, o salário do
 comprador e em quantos anos ele vai pagar. A prestação mensal
  não pode exceder 30% do salário ou então o empréstimo será negado.
'''

casa = float(input('Valor da casa: R$ '))
salário = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print(f'Para pagar uma casa de R$ {casa:.2f} em {anos} anos ', end='')
print(f'a prestação será de R$ {prestação:.2f}')
if prestação <= mínimo:
    print('\033[32mEmpréstimo pode ser CONCEDIDO!\033[m')
else:
    print('\033[31mEmpréstimo NEGADO!\033[m')

