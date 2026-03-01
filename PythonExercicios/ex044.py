print('====== LOJA DO HAICK ======')
preco = float(input('Qual o valor da compra? R$'))
print('FOMAS DE PAGAMENTO \n'
      '[ 1 ] à vista dinheiro/cheque\n'
      '[ 2 ] à vista cartão\n'
      '[ 3 ] 2x no cartão \n'
      '[ 4 ] 3x ou mais no cartão')
res = int(input('Qual é a opção?' ))
if res == 1: print('Você recebeu um desconto! Sua compra deu R${:.2f}'.format(preco*0.90))
elif res == 2: print('Sua compra foi R${:.2f}'.format(preco))
elif res== 3: print('Por conta da taxa sua compra foi R${:.2f}'.format(preco*1.05))
elif res== 4: print('Por conta da taxa e dos mais de 2 parcelamentos sua compra foi R${:.2f}'.format(preco*1.10))
else: print('Opção inválida!')

