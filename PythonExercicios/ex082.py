c = 'S'
lista = []
listapar = []
listaimp = []
while c == 'S':
    n = int(input('Digite um valor: '))
    lista.append(n)
    c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('-='*30)
print(f'A lista completa é {lista}')
for cont in range(0, len(lista)):
    if lista[cont] % 2 == 0:
        listapar.append(lista[cont])
    else:
        listaimp.append(lista[cont])

print(f'A lista de pares é {listapar}')
print(f'A lista de impares é {listaimp}')

