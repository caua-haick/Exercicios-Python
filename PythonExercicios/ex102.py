def fatorial(n,show=False):
    """
    
    :param n: O número a ser calculado 
    :param show: Mostrar ou não a conta (opcional)
    :return: O valor fatorial de um número n
    """""
    f = 1
    for c in range(n, 0, -1):
        if show==True:
            print(f'{c}', end='')
            if c>1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c

    return f

print(fatorial(5, show=True))
help(fatorial)