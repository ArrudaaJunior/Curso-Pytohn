from datetime import date
print('='*60)
print(' Programa que determina a cadegoria dos atletas de natação')
print('='*60)

atual = date.today().year
nasc = int(input('Digite seu ano de nascimento: '))
idade = atual - nasc
print('Idade do atelta: {}'.format(idade))
if idade <= 9:
    print('Categoria: MIRIN')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria JUNIOR')
elif idade <= 25:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')

