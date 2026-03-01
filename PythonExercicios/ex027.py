nome = input('Digite seu nome completo: ')
n = nome.split()
print(""""Muito prazer em te conhecer!
Seu primeiro nome é {}
e o último é {} {}""".format(n[0], n[len(n)-1], n[-1]))