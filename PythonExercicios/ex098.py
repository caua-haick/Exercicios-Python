from time import sleep
def contador(inicio, fim, passo):
    print('-='*30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}: ')
    for c in range(inicio,fim+passo,passo):
        print(c, end=' ')
        sleep(0.5)
    print('FIM!')




contador(1,10,1)
contador(10,0,-2)
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i,f,p)