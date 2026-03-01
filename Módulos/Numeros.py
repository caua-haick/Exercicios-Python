from uteis import numeros
#from uteis import fatorial,dobro,triplo --> permite usar as funções de forma direta sem o "uteis.x"
num = int(input('Digite um número: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é igual a {fat}')
print(f'O dobro de {num} é igual a {numeros.dobro(num)}')
print(f'O triplo de {num} é igual a {numeros.triplo(num)}')
