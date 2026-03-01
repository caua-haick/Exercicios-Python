from random import randint
from time import sleep
cont = 0
cont2= 1
lista = []
print('-='*20)
print('           JOGA NA MEGA SENA          ')
print('-='*20)
quant = int(input('Quantos jogos deseja gerar? '))
for p in range(0,quant):
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
            if cont >= 6:
                break
    lista.sort()
    if cont2 == 1:
        print(f'-=-=-= SORTEANDO {quant} JOGOS -=-=-=')
    print(f'Jogo {cont2}: {lista}',)
    sleep(1)
    lista.clear()
    cont = 0
    cont2 = cont2 + 1
print('-='*5,'< BOA SORTE! >', '-='*5)
