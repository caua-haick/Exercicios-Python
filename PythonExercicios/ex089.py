lista = []
c = 'S'
while c == 'S':
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    lista.append([nome,n1,n2])
    c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('-='*30)
print(f'{"Nº.":<4} {"NOME":<15} {"MÉDIA":>6}')
print('-'*30)
for cont in range(0, len(lista)):
    media = (lista[cont][1] + lista[cont][2]) / 2
    print(f'{cont:<4} {lista[cont][0]:<15} {media:>6.1f}')
n = 0
while n!= 999:
    n = int(input(f'Deseja ver as notas de qual aluno? (999 para parar) '))
    if n<0 or n >= len(lista):
        if n == 999:
            print('PROGRAMA ENCERRADO')
            print('<<< VOLTE SEMPRE >>>')
            break
        else:
            print('Digite um número correspondente a algum aluno cadastrado.')
            continue
    print(f'As notas de {lista[n][0]} são {lista[n][1]} e {lista[n][2]}')
