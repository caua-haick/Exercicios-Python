lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
#Tuplas são imutáveis
print('Nossas opções de lanche são: ',lanche)
print(len(lanche))
for pos,c in enumerate(lanche):
    print(f'Eu vou comer {c} na posição {pos}')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
    print(sorted(lanche))