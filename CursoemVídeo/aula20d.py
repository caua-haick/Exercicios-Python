def soma(*num):
    s=0
    for v in num:
        s=s+v
    print(f'Somando os valores de {num} tem {s}')

soma(2,3,4,5)
soma(5,6,7)
soma(8,9)