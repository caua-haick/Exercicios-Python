galera = list()
jogador = dict()
gp = list()
while True:
    jogador.clear()
    gp.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for cont in range(0, partidas):
        gp.append(int(input(f'Quantos gols na partida {cont+1}? ')))
    jogador['gols'] = gp[:]
    tot = 0
    for k in jogador['gols']:
        tot += k
    jogador['total'] = tot
    galera.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"Codº.":<4} {"NOME":<15} {"GOLS":15} {"TOTAL":>6}')
print('-'*60)
for cont in range(0, len(galera)):
    print(f'{cont:<4} ', end='')
    print(f'{galera[cont]["nome"]:<15} ', end='')
    print(f'{str(galera[cont]["gols"]):<15} ', end='')
    print(f'{galera[cont]["total"]:>6}')
    
n = 0
while n!=999:
    n = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if n<0 or n>=len(galera):
        if n == 999:
            print('PROGRAMA ENCERRADO')
            print('<<< VOLTE SEMPRE >>>')
            break
        else:
            print('Digite um número correspondente a algum jogador cadastrado.')
            continue
    for cont in range(0, len(galera[n]["gols"])):
        if cont ==0:
            print(f'-- Levantamento do jogador {galera[n]["nome"]}')
        print(f'No jogo {cont+1} fez {galera[n]["gols"][cont]} gols.')




