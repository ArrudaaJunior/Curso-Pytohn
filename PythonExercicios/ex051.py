primeiro = int(input('Digite o nímero do primeiro termo: '))
razao = int(input('Digite o número da razão da PA: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end='-> ')
print('FIM')