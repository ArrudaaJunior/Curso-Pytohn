larg = float(input('Digite a largura em metros da parede: '))
alt = float(input('Digite a altura em metros da parede: '))

area = alt * larg
tintalitro = 2 ** 2
pinturametro = area * tintalitro

print('A área da parede é {} e é necessarios {} litros para pintala'.format(area, pinturametro))

