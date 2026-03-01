print('Gerador de pogresão aritmética: ')
print('-=' * 10)
p = int(input('Digite o primeiro termo: '))
r = int(input('Razão da PA: '))
termo = p
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} -> '.format(termo), end='')
        termo = termo + r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com o total de {total} termos mostrados.')
