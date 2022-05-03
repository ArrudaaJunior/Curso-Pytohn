salario = float(input('Digite o salário R$:  '))
# aumento = salario * 1.15
# print('O novo salario com o adicional de 15% é: {:.2f}'.format(aumento))

novo = salario + (salario * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a recerber R${:.2f}'.format(salario, novo))
