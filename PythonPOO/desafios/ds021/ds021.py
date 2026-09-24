from rich import print

class Caneta:
    def __init__(self,cor = "azul"):
        match cor.lower().strip():
            case "azul":
                escolha= "[blue]"
            case "vermelho" | "vermelha":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case _:
                escolha = "[white]"
        self.cor = escolha
        self.tampa = False
    def destampar(self):
        self.tampa = True
    def escrever(self, frase):
        if self.tampa:
            print(f"{self.cor}{frase}[/]", end=" ")
        else:
            print(f":stop_sign: A {self.cor}caneta[/] está tampada!")
    def quebrar_linha(self,linha):
        n = 1
        while n<linha:
            print("\n")
            n+=1
c1 = Caneta("Azul")
c2 = Caneta("Vermelha")
c3 = Caneta("Verde")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem?")
c1.quebrar_linha(2)
c2.escrever("Olá, gafanhoto!")
c3.escrever("Vamos exercitar!")