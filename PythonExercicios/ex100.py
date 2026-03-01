from random import randint
from time import sleep
def sorteia(lista):
    print(f'Sorteando os valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.5)
    print('PRONTO!')


def somapar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares da lista temos {soma}.')


numero = list()
sorteia(numero)
somapar(numero)
