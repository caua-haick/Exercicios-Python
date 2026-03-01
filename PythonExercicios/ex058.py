import random
t = 1
escolha = random.randint(0, 10)
print('Sou seu computador...\n'
      'Acabei de pensar em um número entre 0 e 10.\n'
      'Será que você consegue advinhar qual foi?')
n = int(input('Qual é seu palpite? '))
if n > escolha: print('Menos... Tente mais uma vez')
if n < escolha: print('Mais... Tente mais uma vez')
if n == escolha: print('Parabéns! Você acertou com apenas uma tentativa!')
while n != escolha:
    n = int(input('Qual é seu palpite? '))
    if n > escolha: print('Menos... Tente mais uma vez')
    if n < escolha: print('Mais... Tente mais uma vez')
    t += 1
if n == escolha: print('Parabéns! Você acertou com {} tentativas'.format(t))
