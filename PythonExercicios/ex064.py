n = int(input('Digite um número [999 para parar]: '))
q = 0
s = 0
while n != 999:
    q = q + 1
    s += n
    n = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {q} e a soma entre eles foi {s}')


