c = 'S'
lista = []
while c == 'S':
    n = int(input('Digite um valor: '))
    lista.append(n)
    c = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
print('=-'*30)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente são {lista}')
for cont in range(0, len(lista)):
    if lista[cont] == 5:
        print('O valor 5 está na lista!')
        m= 1
        break
    else:
        m = 0
if m == 0:
    print('O valor 5 não está na lista!')
