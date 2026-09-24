from abc import ABC, abstractmethod
class Funcionario(ABC):
    def __init__(self, nome, salario):
        self.nome = nome
        self._salario = salario

    @property
    def salario(self):
        return self._salario

    # Setter para proteger o salário de reduções
    @salario.setter
    def salario(self, novo_salario):
        if novo_salario < self._salario:
            print("Erro: Você não pode reduzir o salário de um funcionário!")
        else:
            self._salario = novo_salario

    @abstractmethod
    def calcular_bonus(self):
        pass
    def __str__(self):
        return f"{self.nome} recebe R${self._salario:.2f} e por ser {self.__class__.__name__} ganha R${self.calcular_bonus():.2f} de bônus"


class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
        self.bonus = 0.15
    def calcular_bonus(self):
        return self.bonus*self._salario


class Desing(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
        self.bonus = 0.08

    def calcular_bonus(self):
        return self.bonus * self._salario



class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
        self.bonus = 0.10

    def calcular_bonus(self):
        return self.bonus * self._salario


