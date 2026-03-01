a = (2,5,4)
b = (5,8,1,2)
c = a + b
print(c)
print(sorted(c)) #organizar o c em ordem
print(c.count(5)) #quantas vezes aparece o 5
print(c.index(8)) #qual a posição do número
print(c.index(5,2))

pessoa = ('Gustavo', 39, 'M', 99.88) #pode se ter elementos de tipos diferentes em uma mesma tupla
print(pessoa)
del(pessoa) #apagar a tupla