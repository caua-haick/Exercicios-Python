valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor {cont}: ')))
for c,v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Fim da lista')
print(valores)