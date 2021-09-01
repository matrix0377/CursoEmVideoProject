# Exercício Python #040 - Aquele clássico da Média
'''
Crie um programa que leia duas notas de um aluno e calcule
 sua média, mostrando uma mensagem no final, de acordo
 com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Primeira nota: '))
média = (nota1 + nota2) / 2
print(f'Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {média:.1f}')
if média >= 5 and média < 7:    # ou poderia usar dessa forma no Python   7 > média >= 5:
    print('O aluno está em \033[33mRECUPERAÇÃO.\033[m')
elif média < 5:
    print('O aluno está \033[31mREPROVADO.\033[m')
elif média >= 7:
    print('O aluno está \033[34mAPROVADO.\033[m')



