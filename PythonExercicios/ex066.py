n = int(input('Digite um valor (999 para parar): '))
q = 0
s = 0
while True:
    s = n + s
    q = q + 1
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999: break
print(f'A soma dos {q} valores é igual a {s}.')