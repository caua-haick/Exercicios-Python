somaidade = 0
mediaidade = 0
maioriadadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range (1,5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioriadadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioriadadehomem:
        maioriadadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioriadadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))

