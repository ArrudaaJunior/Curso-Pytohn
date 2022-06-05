nome = str(input('Digite seu nome: '))
if nome == 'Arruda':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Junior' or nome == 'Maria':
    print('Seu nome é bem usado no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Que belo nome feminino')
else:
    print('Seu nome é normal.')
print('Tenha um bom dia. {}!'.format(nome))
