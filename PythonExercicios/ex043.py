print('='*50)
print(' Programa que calcula o indice da massa corporal')
print('='*50)

peso = float(input('Digite o seu peso: (Kg) '))
alt = float(input('Digite sua altura: (m) '))
imc = peso / (alt ** 2)

print('Seu IMC é {:.2f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso normal!')
elif 18.5 <= imc < 25:
    print('Peso ideal!')
elif 25 <= imc < 30:
    print('Sobrepeso!')
elif 30 <= imc < 40:
    print('Obesidade!')
elif imc > 40:
    print('Obesidade mórbida')
