def area(a, b):
    c = a * b
    print(f'A área de um terreno {a:.1f} x {b:.1f} é de {c:.1f}m²')


print('CONTROLE DE TERRENOS')
print('-'*30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)