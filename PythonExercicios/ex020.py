import random
a = input('Nome do primeiro aluno: ')
b = input('Nome do segundo aluno: ')
c = input('Nome do terceiro aluno: ')
d = input('Nome do quarto aluno: ')
lista = [a,b,c,d] #precisa dos cochetes por ser string
random.shuffle(lista)
print('A ordem de apresentação será {}'.format(lista))