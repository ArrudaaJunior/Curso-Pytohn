from random import randint
from time import sleep
computador = randint(0, 5) # Faz o sorteio entre o numero 0 e 5.
print('-=-' * 19)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 19)
jogador = int(input('Em que número eu pensei? ')) # Jogador digita tentando adivinhar.
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('\nPARABÉNS! Você acertou o numero escolhido foi {}'.format(computador))
else:
    print('\nErrou! o número sorteado foi {} e não {}!'.format(computador, jogador))
    print('Tente de novo na proxima vez kkkkk')
print('\nAté a proxima!')
