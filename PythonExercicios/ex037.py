import math
n = int(input('Digite um número inteiro:'))
print('Escolha uma das bases para conversão: \n'
      '[ 1 ] converter para binário\n'
      '[ 2 ] converter para octal\n'
      '[ 3 ] converter para hexadecimal')
res = int(input('Sua opção: '))
if res == 1: print('{} convertido para binário é igual a {}'.format(n,bin(n)[2:]))
elif res == 2: print('{} convertido para octal é igual a {}'.format(n,oct(n)[2:]))
elif res == 3: print('{} convertido para hexadecimal é igual a {}'.format(n,hex(n)[2:]))
else: print('Opção invalida!')
