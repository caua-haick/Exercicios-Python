#Declaração de Classe
class Gafanhoto:
    def __init__(self):#Método contrustor
        #Atributos de Instância
        self.nome = ""
        self.idade = 0

   #Métodos de Instâncias:
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f'{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade'

#Declaração de Objeto
g1 = Gafanhoto()
g1.nome = "Luana"
g1.idade = 11
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Cauã"
g2.idade = 19
g2.aniversario()
print(g2.mensagem())