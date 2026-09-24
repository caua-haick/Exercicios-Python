from abc import ABC, abstractmethod
from datetime import date

class Pessoa(ABC):
    def __init__(self, nome:str, nasc:int):
        self._nome = nome
        self._nascimento = None
        self.nascimento= nasc

    @property
    def nascimento(self):
        return self._nascimento
    @nascimento.setter
    def nascimento(self, ano):
        if 1900 <=ano<=  date.today().year:
            self._nascimento = ano
        else:
            raise ValueError(f"{ano} é invalido")
    @property
    def idade(self):
        return date.today().year-self._nascimento
    @idade.setter
    def idade(self, ano):
        raise PermissionError("Você não pode alterar a idade, altere o nascimento!")




class Aluno(Pessoa):
    cursos_oficiais= ["ADM","ADS","ENG","CONT"]
    def __init__(self, nome:str, nascimento:int,curso:str):
        super().__init__(nome, nascimento)
        self._curso = None
        self.curso = curso
    @property
    def curso(self):
        return self._curso
    @curso.setter
    def curso(self, curso):
        curso_fmt = curso.strip().upper()
        if curso_fmt in self.cursos_oficiais:
            self._curso = curso_fmt
        else:
            self._curso = None
            raise ValueError(f"O Curso {curso} não está na lista de cursos oficiais")

    @classmethod
    def add_curso(cls, curso: str):
        curso_formatado = curso.strip().upper()
        if 3 <= len(curso_formatado) <= 5:
            if curso_formatado not in cls.cursos_oficiais:
                cls.cursos_oficiais.append(curso_formatado)
        else:
            raise ValueError(f"Nome '{curso}' está fora do padrão para cursos (deve ter 3 a 5 letras)")