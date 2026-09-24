#Declaração de Classe
class Gafanhoto:
    """
    Essa classe cria um estudante do curso em vídeo, que é uma pessoa com nome e idade
    para criar uma nova pessoa:
    (variavel) = Ganhato((nome),(idade))
    """
    def __init__(self,n="(vazio)",i=0):#Método contrustor
        #Atributos de Instância
        self.nome = n
        self.idade = i

   #Métodos de Instâncias:
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f'{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade'

    def __str__(self):
        return f'Vou te mostrar uma coisa...'
    def __getstate__(self):
        return (f"Estado: nome = {self.nome}; idade = {self.idade}")
#Declaração de Objeto
g1 = Gafanhoto("Cauã",19)
g1.aniversario()
print(g1.mensagem())
print(g1.__doc__)
print(g1)
print(g1.__dict__)
print(g1.__getstate__())
print(g1.__class__)
