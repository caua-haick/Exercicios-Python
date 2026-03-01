n = 1
i = 0
p = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0: p += 1
        elif n % 2 ==1: i += 1
print('Você digitou números {} pares e {} impares'.format(p, i))