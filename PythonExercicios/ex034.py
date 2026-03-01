sal = float(input('Qual é o seu salário? '))
if sal<=1250: print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'. format(sal,sal*1.15))
else: print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'. format(sal,sal*1.10))