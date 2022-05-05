d = int(input('Quantos dias alugados? '))
km = float(input('Qunatos Km rodados? '))
precodia = d * 60
precokm = km * 0.15
precototal = precodia + precokm

print('O total a pagar é de R${:.2f}'.format(precototal))
