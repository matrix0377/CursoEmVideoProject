nome = input ('Qual é o seu nome? ')
idade = int(input('Quantos anos você tem? '))
peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura? '))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('{} você tem {} anos e pesa {:.2f} quilos'.format(nome, idade, peso))
imc = peso / (altura ** 2)
print('E o seu IMC é {:.2f}'.format(imc))
print('-=-=-=-=-=-=-=- ANÁLISE -=-=-=-=-=-=-=-=-=-=')
if imc <=18.5:
    print('Você está Abaixo do Peso')
elif imc >18.5 and imc <25:
    print('Peso normal, parabéns!!!')
elif imc >25 and imc <29.9:
    print('Você está com sobrepeso, cuidado!')
elif imc > 29.9 and imc <34.9:
    print('Você está com Obesidade Grau I, cuidado!')
elif imc > 34.9 and imc <39.9:
    print('Você está com Obesidade Grau II, cuidado!')
elif imc > 40:
    print('\nVocê está com Obesidade Grau III ou Mórbida, Você corre risco de morte!')
print('\n-=-=-=--=-=-=-  FIM  -=-=-=-=-=-=-=-=-=-=--')