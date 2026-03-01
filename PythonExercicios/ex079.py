valores = list()
c = 'S'


while c == 'S':
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso!')

    else:
        print('Valor Duplicado! Não vou adicionar...')

    c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

print(f'Você digitou os valores {valores}.')

