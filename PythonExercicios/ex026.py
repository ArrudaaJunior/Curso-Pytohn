frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aprece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na possição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na possição {}'.format(frase.rfind('A')+1))
