jogador={'nome': input('Nome do jogador: ')}
partidas = int(input('Partidas jogadas: '))
gp = list()
for cont in range(0,partidas):
    gp.append(int(input(f'Quantos gols na partida {cont}? ')))
jogador['gols'] = gp[:]
tot = 0
for k in jogador['gols']:
    tot += k
jogador['total'] = tot
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f' - O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f' - Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
