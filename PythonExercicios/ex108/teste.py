from ex108 import moeda


m = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(m)} é {moeda.moeda(moeda.metade(m))}')
print(f'O dobro de {moeda.moeda(m)} é {moeda.moeda(moeda.dobro(m))}')
print(f'Aumentando {moeda.moeda(m)} em 10%, temos {moeda.moeda(moeda.aumentar(m,10))}')

