class Avaliacao:
    def __init__(self, nome, disciplina, nota):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

        #Métodos acessores
    def get_nota(self): #Método getter
        return self._nota

    def set_nota(self, valor): #Método setter
        if 0<= valor <= 10:
            self._nota = valor
        else:
            print('Nota invalida!')