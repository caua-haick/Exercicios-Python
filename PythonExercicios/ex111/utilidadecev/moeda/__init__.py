def aumentar(n=0,taxa=0, formato=False):
    res = n + (n * taxa / 100)
    return res if formato is False else moeda(res)

def diminuir(n=0,taxa=0, formato=False):
    res = n - (n*taxa/100)
    return res if formato is False else moeda(res)

def dobro(n=0, formato=False):
    res = n *2
    return res if formato is False else moeda(res)

def metade(n=0, formato=False):
    res = n/2
    return res if formato is False else moeda(res)

def moeda(m = 0,p = 'R$'):
    return f'{p}{m:>.2f}'.replace('.', ',')

def resumo(m=0, taxaa=10, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t\t{moeda(m)}')
    print(f'Dobro do preço: \t\t{dobro(m,True)}')
    print(f'Metade do preço: \t\t{metade(m,True)}')
    print(f'Com {taxaa}% de aumentar: \t{aumentar(m,taxaa,True)}')
    print(f'Com {taxar}% de redução: \t{diminuir(m,taxar,True)}')
    print('-'*30)