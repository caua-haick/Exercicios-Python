import math
ca = float(input('Qual o valor do cateto adjacente?'))
co = float(input('Qual o valor do cateto oposto?'))
h = ca**2 + co**2
hi = h**(1/2)
print('Considerando {} e {} a hipotenusa do triângulo é {}'.format(ca,co,hi) )

#math.hypot(ca,co)