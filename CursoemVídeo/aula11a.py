#\033[m
# códigos de estilo 0: none ; 1: negrito, 4:sublinhado, 7: inverte as configurações de texto e fundo
#códigos de texto 30: branco ; 31: vermelho; 32: verde; 33: amarelo; 34: azul
# 35: roxo; 36: ciano; 37: cinza
#cores de fundo 40: branco ; 41: vermelho; 42: verde; 43: amarelo; 44: azul
# 45: roxo; 46: ciano; 47: cinza
#ex: \033[0;33;44m
print('\033[1;31;43m Olá, Mundo!\033[m')
print('\033[4;30;45m Olá, Mundo!')
print('\033[7;33;44m Olá, Mundo!\33[m')
a = 3
b = 5
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Os valores é {}{}{}!!!'.format(cores['amarelo'],a,cores['azul']))
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a,b))
print('Os valores é {}{}{}!!!'.format('\033[4;34m',a,'\033[m'))