from datetime import date

nasc = int(input('Insira o ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc,idade,atual))
if idade == 18: print('Seu alistamento é esse ano!')
elif idade < 18: print('Falta {} anos para seu alistamento'.format(18-idade))
elif idade > 18: print('Seu alistamento foi há {} anos'.format(atual - (18+nasc)))