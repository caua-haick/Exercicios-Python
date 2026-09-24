from rich import print,inspect
from classes import Aluno,Professor,Funcionario


a1=Aluno("José",17,"informática","T01")
a1.fazer_aniversario()
a1.fazer_matricula()
#inspect(a1,methods=True)

p1=Professor("Samuel",37,"Biologia","Mestre")
p1.dar_aula()
p1.fazer_aniversario()
#inspect(p1,methods=True)

f1 = Funcionario("Claúdia",27,"Secretária","Secretaria")
f1.fazer_aniversario()
f1.bater_ponto()
#inspect(f1,methods=True)

a1.estudar()
p1.estudar()
f1.estudar()