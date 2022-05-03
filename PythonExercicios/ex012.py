preco = float(input('Digite o preço do produto? R$:  '))
# desconto = preco * 0.05
# newpreco = preco - desconto

novo = preco - (preco * 5 / 100)

print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f} '.format(preco, novo))
