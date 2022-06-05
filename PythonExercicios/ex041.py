print('='*60)
print(' Programa que determina a cadegoria dos atletas de natação')
print('='*60)

ano = int(input('Digite seu ano de nascimento: '))
ano = 2022 - ano

if ano <= 9:
    print('Categoria: MIRIN')
elif ano > 9 and ano <= 14:
    print('Categoria: INFANTIL')
elif ano > 14 and ano <= 19:
    print('Categoria JUNIOR')
elif ano > 19 and ano == 20:
    print('Categoria: SÊNIOR')
elif ano > 20:
    print('Categoria: MASTER')

