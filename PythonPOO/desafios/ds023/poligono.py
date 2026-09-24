from abc import ABC, abstractmethod
from rich import print
class Poligono(ABC):
    def __init__(self,lado):
        self.lado = lado
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetro(self):
        pass
class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(lado)

    def area(self):
        print(f'A área do quadrado é [cyan]{(self.lado*self.lado):.2f}[/]')
    def perimetro(self):
        print(f'O perímetro do quadrado é [cyan]{(self.lado*4):.2f}[/]')

class Circulo(Poligono):
    def __init__(self, lado):
        super().__init__(lado)

    def area(self):
        print(f'A área do circulo é [cyan]{float(self.lado*self.lado*3.14):.2f}[/]')
    def perimetro(self):
        print(f'O perímetro do circulo é [cyan]{float(self.lado*2*3.14):.2f}[/]')