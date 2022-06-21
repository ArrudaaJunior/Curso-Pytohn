from random import randint
from time import sleep
print('='*30)
print(' GAME: Pedra, Papel e Tesoura')
print('='*30)

itens = ('Pedra', 'Papel', 'Tesouro')
pc = randint(0, 2)
print('''Esolha entre: 
[ 0 ] - Pedra 
[ 1 ] - papel 
[ 2 ] - Tesoura''')
j1 = int(input('Qual você escolhe? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[j1]))
print('-=' * 11)

if pc == 0:
    if j1 == 0:
        print('EMPATE')
    elif j1 == 1:
        print('Jogadro Venceu')
    elif j1 == 2:
        print('Jogador Venceu')
    else:
        print('Jogada Invalida!')
elif pc == 1:
    if j1 == 0:
        print('Computador Venceu')
    elif j1 == 1:
        print('Empate')
    elif j1 == 2:
        print('Jogador Venceu')
    else:
        print('Jogada Invalida!')
elif pc == 2:
    if j1 == 0:
        print('Jogador Venceu!')
    elif j1 == 1:
        print('Computador Venceu!')
    elif j1 == 2:
        print('Empate')
    else:
        print('Jogada Invalida!')
else:
    print('Não existe essa escolha. Tente novamente!')
