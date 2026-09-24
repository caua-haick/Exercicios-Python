
from pessoa import *


def main():
    a = Aluno("Marcia", 2010,"adm")
    a.add_curso("inf")
    a.curso = "inf"
    a.add_curso("Moda")

    print(a.cursos_oficiais)
    print(a.__dict__)


if __name__ == "__main__":
    main()