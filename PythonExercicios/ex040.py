n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Quem tirou {} e {} tem a média {}'.format(n1,n2,m))
if m >= 7: print('Aprovado!')
elif m < 7: print('Reprovado!')