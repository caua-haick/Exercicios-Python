class Diario:
    def __init__(self, senha = "batman"):
        self.__senha = senha
        self.__conteudo=[]
    def escrever(self,conteudo):
        self.__conteudo.append(conteudo)
    def ler(self,senha):
        if self.__senha==senha.strip():
            for conteudo in self.__conteudo:
                print(f"- {conteudo}")
        else:
            print("Você não está autorizado a ler o diario!")


