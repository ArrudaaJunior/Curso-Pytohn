print('Programa de conversão de bases numériacas')

num = int(input('\nDigite um número inteiro: '))

print('\nPara qual base você quer converter o número? \n[ 1 ] - Binário \n[ 2 ] - Octal \n[ 3 ] - Hexadecimal')
base = int(input('Escolha entre os tres: '))

if base == 1:
    numb = bin(num)
    print('{} em Binario é : {}'.format(num, numb[2:]))
elif base == 2:
    numo = oct(num)
    print('{} em Octal é: {}'.format(num, numo[2:]))
elif base == 3:
    numh = hex(num)
    print('{} em hexadecimal é: {}'.format(num, numh[2:]))
else:
    print('Você escolheu uma opção que não existe, tente novamente.')
print('Obrigado, volte sempre!')
