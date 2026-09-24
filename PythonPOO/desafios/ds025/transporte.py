from abc import ABC, abstractmethod
from rich import print
class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
    @abstractmethod
    def calc_frete(self):
        pass
class Moto(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
    def calc_frete(self):
        fator = 0.50
        return f"R$ {float(fator*self.distancia):.2f}"


class Caminhao(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
    def calc_frete(self):
        fator = 1.20
        if self.distancia > 50:
            return f"R$ {float(fator*self.distancia):.2f}"
        else:
            return "Raio mínimo de 50km"


class Drone(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
    def calc_frete(self):
        fator = 9.50
        if self.distancia < 10:
            return f"R$ {float(fator*self.distancia):.2f}"
        else:
            return "Raio máximo de 10km"