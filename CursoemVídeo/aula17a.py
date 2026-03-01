num = [2,5,9,1] #lista / num = () tupla
num[2] = 3 #muda um número
num.append(7) #adiciona um número
num.sort(reverse=False) #ajeita a ordem. reverse true inverte a ordem
num.insert(2, 0 ) #Na posição dois adicionou o número 0
#num.pop() #dependendo do valor de dentro do parenteses vai eliminar o número da respectiva posição, se não houver nada será o último
#num.remove(3) #se houver dois do mesmo valor, só será removido o primeiro
if 4 in num: num.remove(4)
else: print('O valor 4 não está na lista')
print(num)
print(f'Essa lista tem {len(num)} elementos')


