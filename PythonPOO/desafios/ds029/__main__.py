from rich import print, inspect
from diario import *

def main():
    d=Diario("Gafanhoto")

    d.escrever("Primeira mensagem!")
    d.escrever("Você é uma pessoa simpática!")
    d.escrever("Você gosta de Python!")

    d.ler("Gafanhoto")
if __name__ == '__main__':
    main()