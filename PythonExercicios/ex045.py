import random
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
escolha = random.choice(itens)
nome = ''
print('Suas Opções: \n'
      '[ 0 ] Pedra \n'
      '[ 1 ] Papel \n'
      '[ 2 ] Tesoura \n')
res = int(input('Qual é a sua jogada? '))
if res == 0: nome = 'Pedra'
elif res == 1: nome = 'Papel'
elif res == 2: nome = 'Tesoura'
else: print('Opção invalida!')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(0.5)

if res == 0 and escolha == 'Tesoura' or res == 1 and escolha == 'Pedra' or res == 2 and escolha == 'Papel':
    print('Computador jogou {}\n'
          'Você jogou {}\n'
          'Você venceu!!!'.format(escolha,nome))
elif res == 1 and escolha == 'Tesoura' or res == 2 and escolha == 'Pedra' or res == 0 and escolha == 'Papel':
    print('Computador jogou {}\n'
          'Você jogou {}\n'
          'Você perdeu!!!'.format(escolha,nome))
elif res == 2 and escolha == 'Tesoura' or res == 0 and escolha == 'Pedra' or res == 1 and escolha == 'Papel':
    print('Computador jogou {}\n'
          'Você jogou {}\n'
          'Vocês empataram!!!'.format(escolha,nome))

