from funcionario import *

def main():
    f1 = FuncionarioHorista("Paulo",12,200)
    f1.calc_sal()
    f1.analisar()

    f2 = FuncionarioMensalista("Amanda",9500)
    f2.calc_sal()
    f2.analisar()
if __name__ == "__main__":
    main()