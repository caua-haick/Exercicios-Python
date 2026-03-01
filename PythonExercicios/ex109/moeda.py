def aumentar(n=0,taxa=0, formato=False):
    return n + (n*taxa/100) if formato is False else moeda(n)

def diminuir(n=0,taxa=0, formato=False):
    return n - (n*taxa/100) if formato is False else moeda(n)

def dobro(n=0, formato=False):
    return n * 2 if formato is False else moeda(n)

def metade(n=0, formato=False):

    return n / 2 if formato is False else moeda(n)

def moeda(m = 0,p = 'R$'):
    return f'{p}{m:>.2f}'.replace('.', ',')