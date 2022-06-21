print('='*40)
print('Programa que calcula a média do aluno')
print('='*40)

n1 = float(input('\nDigite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = ((n1 + n2)/2)

if media < 5:
    print('Sua media foi {:.2f}'.format(media))
    print('Situação: REPROVADO')
elif 7 > media >= 5:
    print('Sua media foi {:.2f}'.format(media))
    print('Situação: RECUPERAÇÃO')
elif media >= 7:
    print('Sua media foi {:.2f}'.format(media))
    print('Situação: APROVADO')
