
n = str(input('Informe seu sexo: [M/F] ')).upper()
while n != 'M' and n != 'F':
    n = input('Dados inválidos. Por favor, informe seu sexo: [M/F] ').upper()
print(f'Sexo {n} registrado com sucesso!')
