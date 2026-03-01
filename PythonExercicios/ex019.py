import random
a = input('Nome do primeiro aluno: ')
b = input('Nome do segundo aluno: ')
c = input('Nome do terceiro aluno: ')
d = input('Nome do quarto aluno: ')
e = '{} , {} , {} e {}'.format(a,b,c,d)
alunos = a,b,c,d
#n = random.choice(['oi', 'olá','hi'] ) para strings usar cochetes
n = random.choice(alunos)
print('Entre os alunos {}, o aluno {} irá apagar o quadro para o professor!'.format(e,n))
