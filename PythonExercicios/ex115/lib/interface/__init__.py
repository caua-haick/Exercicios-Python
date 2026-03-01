def leiaint(msg):
    while True:
        try:
            i = int(input(msg))
        except Exception as e:
            print('\033[0;30;41mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return i

def linha(tam=42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c=1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c+=1
    print(linha())
    opc = leiaint('\033[32mSua opção: \033[m')
    return opc
