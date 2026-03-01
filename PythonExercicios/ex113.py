while True:
    try:
       i= int(input('Digite um número inteiro: '))
    except Exception as e:
        print('\033[0;30;41mERRO: por favor, digite um número inteiro válido.\033[m')
    else:
        break

while True:
    try:
       r= int(input('Digite um número Real: '))
    except Exception as e:
        print('\033[0;30;41mERRO: por favor, digite um número real válido.\033[m')
    else:
        break

print(f'O valor inteiro digitado foi {i} e o real foi {r:.1f}')