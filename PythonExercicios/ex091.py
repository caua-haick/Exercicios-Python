from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6),
}

ranking = dict()
print(f'Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
cont = 1
print('-='*30)
print(f'== {"Ranking dos jogos":^30} ==')
for k , v in ranking:
    print(f'{k} ficou em {cont}º lugar tirando {v} no dado.')
    cont += 1
    sleep(1)
