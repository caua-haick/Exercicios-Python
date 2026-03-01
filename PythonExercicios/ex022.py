n = input('Digite seu nome completo: ')
m = n.split()
print(""""Analisando seu nome...
Seu nome em maiúsculas é {}
Seu nome em minúsculas é {}
Seu nome tem ao todo {} letras
Seu primeiro nome é {} e ele tem {} letras
""".format(n.upper(),n.lower(), len(n) - n.count(' '),m[0],len(m[0])))