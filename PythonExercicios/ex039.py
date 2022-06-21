from datetime import date

print('\n')
print('='*80)
print('Programa para saber se você esta na idade para se alistar no serviço militar')
print('='*80)

atual = date.today().year
print('[ 1 ] - MASCULINO \n[ 2 ] FEMENINO ')
sx = int(input('Selecione seu Sexo: '))
if sx == 1:
    nasc = int(input('Ano de nasciemnto: '))
    idade = atual - nasc
    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
    if idade == 18:
        print('Alistamento IMEDIATO!')
    elif idade < 18:
        saldo = 18 - idade
        ano = atual + saldo
        print('Faltam {} anos para o alistamento'.format(saldo))
        print('O alistamento será no ano {}'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        ano = atual - saldo
        print('Já PASSOU {} anos do alistamento!'.format(saldo))
        print('O alistamento foi no ano {}'.format(ano))
elif sx == 2:
    print('Alistamento não obricatorio.')
else:
    print('Você diigtou errado! tente novamente.')


'''idade = int(input('Digite sua idade: '))
if idade < 17:
    print('Você ainda vai se alistar ao serviço militar.')
    idade = (idade - 17)*-1
    print('Falta {} anos para você poder se alistar'.format(idade))
elif idade == 17 or idade == 18:
    print('É a hora de você se alsitar!')
elif idade < 18:
    print('Já passou do tempo do alistamento')
    idade = idade - 18
    print('Passou {} anos da idade para se alistar'.format(idade))'''