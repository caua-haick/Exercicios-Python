from rich import print
from rich.panel import Panel

class Mensagem:
    def __init__(self, msg: str = "", tipo: str = "aviso", icone: str = ":speech_balloon:"):
        self._mensagem = msg
        self._tipo = tipo
        self._icone = icone

    def mostrar(self):
        msg = Panel(
            self._mensagem,
            title=f"{self._icone} {self._tipo.upper()} {self._icone}",
            style="white on #000000",  # Letra branca no fundo preto
            width=50
        )
        print(msg)


class Alerta(Mensagem):
    def __init__(self, msg: str = ""):
        super().__init__(msg, tipo="alerta", icone=":warning:")

    def mostrar(self):
        msg = Panel(
            self._mensagem,
            title=f"{self._icone} {self._tipo.upper()} {self._icone}",
            style="#000000 on #ffc107",  # Letra preta no fundo amarelo
            width=50
        )
        print(msg)


class Erro(Mensagem):
    def __init__(self, msg: str = ""):
        super().__init__(msg, tipo="erro", icone=":prohibited:")

    def mostrar(self):
        msg = Panel(
            self._mensagem,
            title=f"{self._icone} {self._tipo.upper()} {self._icone}",
            style="#ffff00 on #880000",  # Letra amarela no fundo vermelho escuro
            width=50
        )
        print(msg)