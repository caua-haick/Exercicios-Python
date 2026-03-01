import random
print('=-'*30)
print('VAMOS JOGAR ÍMPAR OU PAR')
print('=-'*30)
while True:
    n = random.randint(0, 10)
    p = int(input('Digite um valor: '))
    o = (input('Par ou Ímpar? [P/I] ')).upper()
    s = n + p
    l = ''
    if n % 2 == 0: l = 'PAR'
    elif n % 2 == 1: l = 'IMPAR'
    if o == 'P' and s % 2 == 0 or o == 'I' and s % 2 == 1:
        print(f'Seu oponente colocou {n} e você {p}, somados dão {s} que é {l}. Você venceu!')
    if o == 'P' and s % 2 == 1 or o == 'I' and s % 2 == 0:
        print(f'Seu oponente colocou {n} e você {p}, somados dão {s} que é {l}. Você perdeu!')
        break

