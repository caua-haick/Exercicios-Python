from rich import print
from rich.panel import Panel
class Churrasco:
    def __init__(self,titulo,quantidade):
        self.titulo = titulo
        self.quantidade = quantidade
    def analisar(self):
        carne = 0.4*self.quantidade
        custot = carne*82.40
        cont = f"Analisando [green]{self.titulo}[/] com [blue]{self.quantidade} convidados[/]\n"
        cont += f"Cada participante comerá 0.4Kg e cada Kg custa R$82.40\n"
        cont += f"Recomendo [blue]comprar {carne:.3f}Kg[/] de carne\n"
        cont += f"O custo total será de [green]R${custot:,.2f}[/]\n"
        cont += f"Cada pessoa pagará [yellow]R${custot/self.quantidade:,.2f}[/] para participar"
        etiqueta = Panel(cont, title=self.titulo, width=70)
        print(etiqueta)

c1 = Churrasco("Churras dos Amigos",15)
c1.analisar()