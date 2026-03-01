import random
n = random.choice([0,1,2,3,4,5])
m = int(input('Em qual número de 0 a 5 o computador está pensando? '))
if m == n: print('Parabéns! Você acertou!')
else: print('Você digitou {}, mas a resposta foi {}'.format(m, n))