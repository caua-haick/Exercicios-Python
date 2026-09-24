from classes import *
def main():
    x = Analisador()
    x.analisar(250.2)
    x.analisar(max([6,9.3,2]))
    x.analisar(len([6, 9.3, 2]))
    x.analisar(([6, 9.3, 2]))
if __name__ == '__main__':
    main()