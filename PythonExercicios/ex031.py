d = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(d))

'''cobrar = d * 0.50 if d <= 200 else d * 0.45''' # forma simplificado de se fazer o if e eslse

if d <= 200:
    cobrar = d * 0.50
    '''print('E o preço da sua passagem será de R${:.2f}'.format(cobrar))'''
else:
    cobrar = d * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(cobrar))
