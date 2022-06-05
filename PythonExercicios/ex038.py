print('Programa para comparar dois números inteiros e ver qual é o maior.\n')

v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))

if v1 > v2:
    print('\nO primeiro valor é maior!')
elif v2 > v1:
    print('\nO segundo valor é maior!')
elif v1 == v2:
    print('\nNão existe valor maior, os dois são iquais!')
print('\nvolte sempre!')
