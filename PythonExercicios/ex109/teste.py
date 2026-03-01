from ex109 import moeda


m = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(m)} é {moeda.metade(m,True)}')
print(f'O dobro de {moeda.moeda(m)} é {moeda.dobro(m,True)}')
print(f'Aumentando {moeda.moeda(m)} em 10%, temos {moeda.aumentar(m,10,True)}')
print(f'Diminuindo {moeda.moeda(m)} em 10%, temos {moeda.diminuir(m,10,True)}')


