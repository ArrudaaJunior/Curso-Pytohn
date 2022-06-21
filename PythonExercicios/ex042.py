print('='*30)
print(' Analisando Triângulos v2.0')
print('='*30)

s1 = float(input('Digite o primeiro segmento: '))
s2 = float(input('Digite o segundo segmento: '))
s3 = float(input('Digite o terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if s1 == s2 == s3:
        print('EQUILÁTERO!')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Não é um triângulo.')

