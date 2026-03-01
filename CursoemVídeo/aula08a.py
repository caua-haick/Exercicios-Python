import math
import random
import emoji

#from math import ceil, sqrt (exemplo)
# floor (arredonda pra baixo) ceil(arredonda pra cima) sqrt(raiz)
num = int(input('Digite um número: '))
n = random.randint(1,10)
print(n)
raiz = math.sqrt(num)
print('A raiz de {} é {} de forma arredondada é {}'.format(num,raiz,math.ceil(raiz)))
# em python.org posso ver todas as bibliotecas disponíveis
print(emoji.emojize('olá, mundo :earth_americas:',use_aliases=True))
