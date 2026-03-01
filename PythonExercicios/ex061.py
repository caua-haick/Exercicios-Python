print('Gerador de pogresão aritmética: ')
print('-=' * 10)
p = int(input('Digite o primeiro termo: '))
r = int(input('Razão da PA: '))
t = p
c = 1
while c <= 10:
    print('{} --> '.format(t), end='')
    t = t + r
    c += 1
print('FIM')
