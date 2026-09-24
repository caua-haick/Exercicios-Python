from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = []  # Lista para armazenar os jogos

    def add_favoritos(self, jogo):
        self.favoritos.append(jogo)

    def ficha(self):
        conteudo = f"Nome real: [bold black on blue]{self.nome}[/]\nJogos favoritos:"

        for jogo in sorted(self.favoritos):
            conteudo += f"\n:video_game:[blue] {jogo}[/]"

        ficha = Panel(conteudo, title=f"Jogador <{self.nick}>", width=50)
        print(ficha)

j1 = Gamer("Fabricio da Silva", "detonador2025")
j1.add_favoritos("Fortnite")
j1.add_favoritos("God of War")
j1.add_favoritos("Bloodborne")
j1.ficha()