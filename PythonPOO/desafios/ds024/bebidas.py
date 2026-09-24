from abc import ABC, abstractmethod
from rich import print
class Bebida_quente(ABC):

    def ferver_agua(self):
        print(f"1. Fervendo água a 100ºC.")
    @abstractmethod
    def misturar(self):
        pass
    @abstractmethod
    def servir(self):
        pass
    def preparar(self):
        print(f"--- Iniciando o Preparo ---")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("--- Bebida Pronta! ---")
class Leite(Bebida_quente):
    def misturar(self):
        print(f"2. Passando vapor pressurizado pelo bico do leite.")
    def servir(self):
        print(f"3. Servindo na caneca grande, já com café.")

class Cafe(Bebida_quente):
    def misturar(self):
        print(f"2. Passando a água pressurizada pelo pó de café moído.")
    def servir(self):
        print(f"3. Servindo em xícara pequena.")

class Cha(Bebida_quente):
    def misturar(self):
        print(f"2. Mergulhando o sachê de ervas na água.")
    def servir(self):
        print(f"3. Servindo na caneca de porcelana com limão.")
