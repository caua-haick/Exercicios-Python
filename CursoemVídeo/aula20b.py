def soma(a,b):
    s= a + b
    print(f'A soma de {a} + {b} = {s}')
    print(s)



soma(4,5)
soma(b=2,a=1)
print()
print()

def contador(*num):
    print(num)
    print('Números que estão dentro: ')
    for valor in num:
        print(valor, end=' ')
    print()
    print('Quantidade de números dentro: ', end='')
    tam = len(num)
    print(tam)

contador(1, 2, 3,4,5,6,7,7)
contador(1, 2)