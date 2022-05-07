nome = str(input('Qual é seu nome? ')).strip()
if nome.upper() == 'JUNIOR':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))

