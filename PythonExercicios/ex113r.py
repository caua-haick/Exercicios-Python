def leiaint(msg):
    while True:
        try:
            i = int(input(msg))
        except Exception as e:
            print('\033[0;30;41mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return i
def leiafloat(msg):
    while True:
        try:
            r = float(input(msg))
        except Exception as e:
            print('\033[0;30;41mERRO: por favor, digite um número real válido.\033[m')
            continue
        else:
            return r

inteiro = leiaint('Digite um número inteiro: ')
real = leiafloat('Digite um número real: ')

print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')