n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print('     [ 1 ] somar\n'
      '     [ 2 ] multiplicar\n'
      '     [ 3 ] maior\n'
      '     [ 4 ] novos números\n'
      '     [ 5 ] sair do programa')
n = int(input('Qual é a sua opção? '))
while n != 5:
    if n == 1: print(f'A soma entre {n1} + {n2} = {n1 + n2}')
    elif n == 2: print(f'A multiplicação entre {n1} x {n2} = {n1 * n2}')
    elif n == 3:
        if n1 > n2: print(f'{n1} é maior que {n2}')
        elif n2 > n1: print(f'{n2} é maior que {n1}')
        else: print('Os valores são iguais!')
    elif n == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    print('\n     [ 1 ] somar\n'
          '     [ 2 ] multiplicar\n'
          '     [ 3 ] maior\n'
          '     [ 4 ] novos números\n'
          '     [ 5 ] sair do programa')
    n = int(input('Qual é a sua próxima opção? '))
print('Programa finalizado!')
