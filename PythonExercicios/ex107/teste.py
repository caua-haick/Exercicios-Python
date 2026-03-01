from ex107 import moeda

m = float(input('Digite um preço: R$'))
print(f'A metade de R${m} é R${moeda.metade(m)}')
print(f'O dobro de R${m} é R${moeda.dobro(m)}')
print(f'Aumentando R${m} em 10%, temos R${moeda.aumentar(m,10)}')
