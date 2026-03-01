n = int(input('Digite um número: '))
q = str(input('Quer continuar? [S/N] ')).upper()
p = 1
s = n
x = n
l = n
while q != 'N':
    n = int(input('Digite um número: '))
    q = str(input('Quer continuar? [S/N] ')).upper()
    p += 1
    s = s + n
    if n > x: x = n
    if n < l: l = n
m = (s / p)
print(f'Você digitou {p} números e a média entre eles foi {m} \n'
      f'O maior valor foi {x} e o menor valor foi {l}')