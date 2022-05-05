from math import radians, sin, cos, tan
angulo = float(input('Digite o ângolo que você deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem COSSENO de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {} tem TANGENTE de {:.2f}'.format(angulo, tangente))

