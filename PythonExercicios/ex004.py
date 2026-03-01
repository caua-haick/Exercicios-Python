n = input('Digite algo: ')
print(n)
print('só tem espaços?',n.isspace())
print('é um número?',n.isnumeric())
print('é uma letra?',n.isalpha())
print('é alfanúmerico?',n.isalnum())
print('está em maiúscula',n.isupper())
print('está em minúscula?',n.islower())
print('está capitalizada?',n.istitle())#letras que estão alternando entre maiusculas e minusculas
