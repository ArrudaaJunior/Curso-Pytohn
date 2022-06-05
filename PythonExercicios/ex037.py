print('Programa de conversão de bases numériacas')

num = int(input('\nDigite um numero inteiro: '))

print('\nPara qual base você quer converter o número? \n1 - Binário \n2 - Octal \n3 - Hexadecimal')
base = int(input('Escolha entre os tres: '))

if base == 1:
    numb = num % 2
    print('{} em Binario é : {}'.format(num, numb))
elif base == 2:
    numo = num % 8
    print('{} em Octal é: {}'.format(num, numo))
elif base == 3:
    numh = num % 16
    print('{} em hexadecimal é: {}'.format(num, numh))
else:
    print('Você escolheu uma opção que não existe, tente novamente.')
print('Obrigado, volte sempre!')
