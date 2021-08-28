# Curso Python #23 - Tratamento de Erros e Exceções
'''
Nessa aula, vamos ver como o Python permite tratar erros
 e criar respostas a essas exceções. Aprenda como usar
  a estrutura try except no Python de uma forma simples.
'''

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou. ')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero! ')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados! ')
except Exception as erro:
    print('O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r}')
finally:
    print('volte sempre! Muito obrigado!')



