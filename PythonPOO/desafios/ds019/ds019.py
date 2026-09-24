from rich import print



class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.contador = 1
        print(f"[blue]Você acabou de abrir o livro '[red]{self.titulo}[/]' que tem [green]{self.paginas} páginas[/] no total. Você agora está na [yellow]Página 1[/][/]")

    def avancar(self, pag):

        destino = self.contador + pag
        if destino > self.paginas:
            destino = self.paginas
        for pagina in range(self.contador + 1, destino + 1):
            print(f"Pág{pagina}->", end="")

        self.contador = destino
        print(f"[blue]Você avançou {pag} paginas e agora está na [yellow]Página {self.contador}[/][/]\n")
        if destino == self.paginas:
            print(f":stop_sign:[red]Você chegou ao final do livro '{self.titulo}'[/]:stop_sign:")


l1 = Livro("10 coisas que aprendi", 20)
l1.avancar(5)
l1.avancar(10)
l1.avancar(20)
l1.avancar(20)