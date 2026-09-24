from classe030 import *
from rich import print,inspect

def main():
    c = Credencial()
    c.senha = input("Digite sua senha: ")
    print(c.senha)

    c.validar("Teste123")
    c.validar("Batman")
if __name__ == '__main__':
    main()