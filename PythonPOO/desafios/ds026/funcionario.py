from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel
class Funcionario(ABC):
    sal_min = 1612
    inss = 7.5
    def __init__(self,nome):
        self.nome = nome
    @abstractmethod
    def calc_sal(self):
        pass
    @abstractmethod
    def analisar(self):
        pass
class FuncionarioHorista(Funcionario):
    def __init__(self,nome,valor_hora,quant_horas):
        super().__init__(nome)
        self.salario = 0
        self.valor_hora = valor_hora
        self.quant_horas = quant_horas
    def calc_sal(self):
        self.salario = self.valor_hora*self.quant_horas*(100-Funcionario.inss)/100
        return f"R${self.salario:.2f}"
    def analisar(self):
        conteudo = f"O salário de [blue]{self.nome}[/] [purple]({FuncionarioHorista.__name__})[/] é de [green]{self.calc_sal()}[/] e corresponde a [yellow]{self.salario/Funcionario.sal_min:.1f} salários mínimos.[/]"
        ficha = Panel(conteudo,title="Análise de Salário", width=50)
        print(ficha)

class FuncionarioMensalista(Funcionario):
    def __init__(self,nome,sal_bruto):
        super().__init__(nome)
        self.salario = 0
        self.sal_bruto = sal_bruto
    def calc_sal(self):
        self.salario = self.sal_bruto*(100-Funcionario.inss)/100
        return f"R${self.salario:.2f}"
    def analisar(self):
        conteudo = f"O salário de [blue]{self.nome}[/] [purple]({FuncionarioMensalista.__name__})[/] é de [green]{self.calc_sal()}[/] e corresponde a [yellow]{self.salario/Funcionario.sal_min:.1f} salários mínimos.[/]"
        ficha = Panel(conteudo,title="Análise de Salário", width=50)
        print(ficha)