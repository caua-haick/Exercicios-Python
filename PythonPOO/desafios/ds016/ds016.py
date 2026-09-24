from rich import print
class Funcionario:
    def __init__(self,nome,setor,cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        print('Funcionário criado!')
    def apresentar(self):
        return f':handshake:Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa'

n = input('Qual o nome do funcionário? ')
s = input('Qual o setor que ele trabalha? ')
c = input('Qual o cargo que ele ocupa? ')
f = Funcionario(n,s,c)
print(f.apresentar())