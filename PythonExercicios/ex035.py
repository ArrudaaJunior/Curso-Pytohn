import time
print('-=' * 13)
print('Analisandor de Triângulos')
print('-=' * 13)

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
print('\nAnalisando....')
time.sleep(1)
if s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2:
    print('\nOs segmentos acima PODEM FORMAR um triângulo!')
else:
    print('\nOs segmentos acima NÃO PODEM FORMA um triângulo!')
