print('10 TERMOS DE UMA PA')
n1 = int(input('Digite o primeiro termo: '))
R = int(input('Razão: '))
for c in range(0,10,1):
    print('{} --> '.format(n1 + c * R), end='' )
print('ACABOU')