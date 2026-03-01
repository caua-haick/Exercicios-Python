
e = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
m = int(input('Digite um número entre 0 e 20: '))

if m < 0 or m > 20:
    while m < 0 or m > 20: m = int(input('Você colocou um valor fora do parâmetro! Por favor, digite um número entre 0 e 20: '))
print(f'Você digitou o número {e[m]}!')