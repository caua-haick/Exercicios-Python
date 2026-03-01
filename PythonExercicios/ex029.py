vel = int(input("Qual a sua velocidade? "))
if vel <= 80: print('Tudo ok')
else: print('Você foi multado em {} reais'.format((vel-80)*7))