import random
from rich import print
from abc import ABC,abstractmethod
class Personagem(ABC):
    def __init__(self,nome,vida):
        self.nome = nome
        self.vida = vida
        self.golpes= []
    def atacar(self,alvo,forca=100):
        if self.vida> 0 and alvo.vida >0:
            golpe = self.golpes[random.randrange(0,len(self.golpes))]

            print(f"[green]{self.nome}[/]({self.vida}) atacou [red]{alvo.nome}[/]({alvo.vida}) com um [blue]{golpe}[/]")
            alvo.receber_dano(forca)

        else:
            print(f"O Ataque {self.nome} ---> {alvo.nome} não pode acontecer")
    def receber_dano(self, dano):
        fator = random.randint(0,dano)
        self.vida = self.vida - fator
        if self.vida <= 0:
            self.vida = 0
        print(f"[blue]{self.nome}[/] recebeu [red]dano de {fator}[/]!")

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self,nome,vida):
        super().__init__(nome,vida)
        self.golpes= ["Soco","Golpe de Machado","Chute Giratório"]
    def curar(self):
        fator = random.randint(0,100)
        self.vida = self.vida + fator
        print(f"[blue]{self.nome}[/] enrolou uma atadura e [green]recuperou {fator} pontos[/] de vida ({self.vida})")


class Mago(Personagem):
    def __init__(self,nome,vida):
        super().__init__(nome,vida)
        self.golpes = ["Bola de Fogo", "Raio de luz", "Magia Estática"]
    def curar(self):
        fator = random.randint(0, 100)
        self.vida = self.vida + fator
        print(f"[blue]{self.nome}[/] fez uma magia de cura e [green]curou {fator} pontos[/] de vida ({self.vida})")


