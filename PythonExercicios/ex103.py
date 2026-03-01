def ficha(nome='<Desconhecido>',gol=0):

    print(f'O jogador {nome} fez {gol} gol(s).')


print('-'*30)
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol = g)
else:
    ficha(n, g)
