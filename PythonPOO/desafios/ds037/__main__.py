from classes import *
def main():

    m1 = Mensagem("Esse curso é ótimo!")
    m1.mostrar()


    a1 = Alerta("Atenção, verifique seus dados!")
    a1.mostrar()

    Erro("Falha geral do sistema!").mostrar()

if __name__ == '__main__':
    main()