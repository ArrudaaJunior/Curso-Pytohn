larg = float(input('Digite a largura em metros da parede: '))
alt = float(input('Digite a altura em metros da parede: '))

area = larg * alt
tinta= area / 2

print('A área da parede é {}m² e é necessarios {} litros para pintala'.format(area, tinta))
