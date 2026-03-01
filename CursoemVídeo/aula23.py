try: #Comando principal
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
#except Exception as erro: #Se der errado
#   print(f'Problema encontrado foi {erro.__class__}')
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados digitados.')
except ZeroDivisionError:
    print('Não é possível dividir por zero')
except KeyboardInterrupt:
    print('O usuário preferiu não digitar os dados')


else: #Se der certo
    print(f'O resultado é {r:.1f}')
finally: #Acontecerá independente de ter dado certo ou errado
    print('Volte sempre!')
