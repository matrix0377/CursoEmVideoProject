# Exercício Python #071 - Simulador de Caixa Eletrônico - Aula15

print('=' * 35)
print('{:^30}'.format('BANCO CEV'))
print('=' * 35)
valor = int(input('Que valor você que sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced:>} cédula(s) de R$ {ced:<}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 35)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')

