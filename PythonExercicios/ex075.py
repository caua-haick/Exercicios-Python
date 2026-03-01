m = (int(input('Digite um número: ')),int(input('Digite outro número: ')),int(input('Digite mais um número: ')),int(input('Digite o último número: ')) )

print(f'Você digitou os valores {m}')
print(f'O valor 9 apareceu {m.count(9)} vezes')
if 3 in m: print(f'O valor 3 apareceu na {m.index(3)+1}ª posição')
else: print('O valor 3 não foi digitado')
print('Valores pares digitados: ', end='')
for n in m:
    if n % 2 == 0:
        print(n, end=' ')