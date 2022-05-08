import time
salario = float(input('Qual é o salario do funcionário? R$'))
print('Processando...')
time.sleep(2)
if salario >= 1250:
    nsalario = (salario * 0.10) + salario
else:
    nsalario = (salario * 0.15) + salario
print('ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, nsalario))
