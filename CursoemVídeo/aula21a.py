#help() --> usar essa função trás explicações de comandos, como help(print)
#print(input.__doc__) --> trás mais informações sobre o comando
def contador(i, f, p):
    """ 
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Gustavo Guanabara do canal CursoemVídeo.
    """ # esses 3 " servem para colocar explicações dentro do programa que eu criei, para eu usar o help
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


help(contador)