f = input('Digite uma frase: ')
fr = f.lower().strip()
print(""""A letra A aparece {} vezes na frase.
A primeira letra A apareceu na posição {}
A última letra A apareceu na posição {}"""
      .format(fr.count('a'), fr.find('a')+1,fr.rfind('a')+1 ))
#find é a posição do primeiro termo solicitado
# quando usado rfind ele começa a procurar o termo pela direita