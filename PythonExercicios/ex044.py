print('='*30)
print('  Gerenciador de pagemento ')
print('='*30)

vlproduto = float(input('Digite o valor do produto R$: '))
print('\nForma de pagamento:\n \n[ 1 ] - Á vista Dinheiro/Cheque \n[ 2 ] - Á vista Cartão '
      '\n[ 3 ] - 2x no cartão \n[ 4 ] - 3x ou mais no cartão\n')
print('='*30)

condicao = int(input('\nEscolha a forma de pagaemnto: '))

if condicao == 1:
    novovalor = vlproduto - (vlproduto * 0.10)
    print('10% de descconto aplicado - Valor a pagar R${:.2f}'.format(novovalor))
elif condicao == 2:
    novovalor = vlproduto - (vlproduto * 0.05)
    print('5% de desconto aplicado - valor a pagar R${:.2f}.'.format(novovalor))
elif condicao == 3:
    print('Valor normal R${:.2f}'.format(vlproduto))
elif condicao == 4:
    novovalor = vlproduto + (vlproduto * 0.2)
    print('20% de juros aplicado - valor a pagar R${:.2f}'.format(novovalor))
else:
    total = vlproduto
    print('Opção inválida de pagemneto. Tente novamente!')
