dezoito = 0
homens = 0
mulheres = 0

while True:
    print('-'* 30)
    print('CADASTRE UMA PESSOA'.center(30))
    print('-'* 30)
    n = int(input('Idade: '))
    s = input('Sexo: [M/F] ').upper()
    print('-' * 30)
    l = input('Quer continuar? [S/N] ').upper()
    if s == 'M': homens += 1
    if n >= 18: dezoito += 1
    if s == 'F' and n < 20: mulheres += 1
    if l == 'N' : break
print(f'Total de pessoas com mais de 18 anos : {dezoito}\n'
      f'Ao todo temos {homens} homens cadastrados\n'
      f'E temos {mulheres} mulheres com menos de 20 anos')




