matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sp = 0
maior =0
st = 0
for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = (int(input(f'Digite um valor para [{i}][{j}]: ')))

print('-='*30)
for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]:^5}]', end='')
        if i ==1 and j == 0:
            maior = matriz[2][j]
        if  j == 2:
            st += matriz[i][j]
        if matriz[i][j] % 2 == 0:
            sp += matriz[i][j]
        if matriz[1][j] > maior:
            maior = matriz[i][j]
    print('')
print('-='*30)
print(f'A soma dos valores pares é {sp}')
print(f'A soma dos valores da terceira coluna é {st}')
print(f'O maior valor da segunda linha é {maior}')


