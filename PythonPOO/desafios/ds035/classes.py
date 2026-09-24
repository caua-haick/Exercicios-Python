from abc import ABC, abstractmethod
class Arquivo(ABC):
    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho/1_000_000
        self._extensao = None
    @property
    def nome_completo(self):
        return f"{self.nome}.{self._extensao}"
    def abrir(self):
        pass

class PDF(Arquivo):
    def __init__(self, nome, tamanho):
        super().__init__(nome, tamanho)
        self._extensao = 'pdf'
    def abrir(self):
        print(f"Abrindo o arquivo '{self.nome_completo}'({self.tamanho}MB) no Adobe Reader")

class DOC(Arquivo):
    def __init__(self, nome, tamanho):
        super().__init__(nome, tamanho)
        self._extensao = 'docx'
    def abrir(self):
        print(f"Abrindo o arquivo '{self.nome_completo}'({self.tamanho}MB) no Microsoft Word")

def abrir_arquivo(arq):
    arq.abrir()

