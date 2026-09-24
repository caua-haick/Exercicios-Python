class Mae:
    def __init__(self, nome:str = "Mamãe"):
        self.nome = nome

    def fazer_pudim(self):
        print(f"{self.nome} faz pudim com leite condensado e calda")
    def fritar_coxinha(self):
        print(f"{self.nome} frita coxinha com óleo de soja")

class Filha(Mae):
    def fazer_pudim(self):
        print(f"{self.nome} faz pudim de leite ninho com nutella")

class Filho(Mae):
    def fritar_coxinha(self):
        print(f"{self.nome} faz coxinha na air fryer")