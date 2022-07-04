from datetime import date
atual = date.today().year
cont1 = 0
cont2 = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade = atual - ano
    if idade >= 21:
        cont1 += 1
    else:
        cont2 += 1
print('\n\nTem {} maiores de idade'.format(cont1))
print('Tem {} menores de idade'.format(cont2))


