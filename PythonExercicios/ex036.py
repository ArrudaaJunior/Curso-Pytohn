import time

print('='*35)
print('Bem vindo. \nEmpréstimo bancário do Arruda')
print('='*35)


casavalor = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o seu salário: R$'))
anos = int(input('Em quantos anos deseja pagar? '))

print('\nProcessando...')
time.sleep(2)

parcelamensal = (casavalor/(anos*12))
print('valor da prestação mensal: {:.2f}'.format(parcelamensal))

print('\nProcessando...')
time.sleep(2)

if parcelamensal <= salario * 0.3:
    print('Emprestimo aprovado!')
else:
    print('Desculpe, emprestimo negado.')
print('\nTenha um bom dia.')
