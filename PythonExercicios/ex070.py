print('-'* 30)
print('LOJA SUPER BARATÃO'.center(30))
print('-'* 30)
soma = 0
cont = 0
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    menor = preco
    soma += preco
    produto = ''
    if preco > 1000:
        cont += 1
    if preco <= menor:
        menor = preco
        produto = nome
    if continuar == 'N':
        break
print('-'* 10,'FIM DO PROGRAMA', '-'*10)
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {cont} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {produto} que custa R${menor:.2f}')





