from time import sleep
def maior(*num):
    print('-='*30)
    m= 0
    cont = 0
    tam = len(num)
    for n in num:
        if cont == 0:
            m = n
        if n>m:
            m = n
        cont +=1
    print(f'Analisando os valores passados...')
    for n in num:
        print(n, end=' ')
        sleep(0.5)
    print(f'foram informados {tam} valores.')
    print(f'O maior valor informado foi {m}.')


n1 = [2,9,4,5,7,1]
n2 =[4,7,0]
n3 = [1,2]
n4 = [6]
n5 = []
maior(*n1)
maior(*n2)
maior(*n3)
maior(*n4)
maior(*n5)