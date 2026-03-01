from datetime import date

nasc = int(input('Digite o seu ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9: print('Classificação: Junior')
elif 18 > idade > 9: print('Classificação: Jovem')
elif idade >= 18: print('Classificação: Senior')