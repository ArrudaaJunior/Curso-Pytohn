print('='*50)
print(' Programa que calcula o indice da massa corporal')
print('='*50)

peso = float(input('Digite o seu peso: '))
alt = float(input('Digite sua altura: '))
imc = peso/alt**2

print('Seu IMC é {:.2f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal!')
elif imc >=25 and imc < 30:
    print('Sobrepeso!')
elif imc >= 30 and imc < 40:
    print('Obesidade!')
elif imc > 40:
    print('Obesidade mórbida')
