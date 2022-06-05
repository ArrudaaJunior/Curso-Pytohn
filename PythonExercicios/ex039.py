print('\n')
print('='*80)
print('Programa para saber se você esta na idade para se alistar no serviço militar')
print('='*80)

idade = int(input('Digite sua idade: '))
if idade < 17:
    print('Você ainda vai se alistar ao serviço militar.')
    idade = (idade - 17)*-1
    print('Falta {} anos para você poder se alistar'.format(idade))
elif idade == 17 or idade == 18:
    print('É a hora de você se alsitar!')
elif idade < 18:
    print('Já passou do tempo do alistamento')
    idade = idade - 18
    print('Passou {} anos da idade para se alistar'.format(idade))
