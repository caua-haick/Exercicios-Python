n = list()
dado = list()
for cont in range(0,7):
    dado.append(int(input(f'Digite o {cont+1}º valor: ')))
    n.append(dado[:])
    dado.clear()
n.sort()
print(f'Os valores pares digitados foram: [', end='')
for p in n:
    if p[0] % 2 == 0:
        print(f'{p[0]},', end=' ')
print(']')
print(f'Os valores impares digitados foram: [', end='')
for p in n:
    if p[0] % 2 != 0:
        print(f'{p[0]},', end=' ')
print(']')