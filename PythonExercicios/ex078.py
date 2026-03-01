valores = list()
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
print('=-'*30)
print(f'Você digitou os valores {valores}.')
maior = max(valores)
menor = min(valores)
print(f'O maior valor digitado foi {maior}.',end=' ')
print('Ele se encontra nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end=' ')
print(f'\nO menor valor digitado foi {menor}. ', end=' ')
print('Ele se encontra nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end=' ')