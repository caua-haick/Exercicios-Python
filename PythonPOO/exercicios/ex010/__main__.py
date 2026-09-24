from avaliacao import *
from rich import print, inspect
def main():
    av1 = Avaliacao("Pedro", "Matemática", 9.5)
    av1.nota = 5
    print(f"{av1.nome} tirou nota {av1.nota} na prova de {av1.disciplina}")
    #inspect(av1, private=True)
if __name__ == '__main__':
    main()