def funcao():
    """
    --> Variável local
    """
    n1 = 4
    print(f'N1 dentro vale {n1}')

# variável global
n1 = 2
funcao()
print(f'N1 fora vale {n1}')

