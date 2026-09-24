
class Retangulo:
    def __init__(self, base=1, altura=1):
        self._base = base
        self._altura = altura
        if self._base < 0 or self._altura < 0:
            raise ValueError("Valor invalido inserido! Tente novamente")
        self._area = self._base * self._altura
        self._medidas = f"base: {self._base}\naltura: {self._altura}\narea: {self._area}"
    @property
    def base(self):
        return self._base
    @base.setter
    def base(self, base):
        if base < 0:
            raise ValueError("Valor invalido inserido! Tente novamente")
        self._base = base
        self._area = self._base * self._altura
        self._medidas = f"base: {self._base}\naltura: {self._altura}\narea: {self._area}"
    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        if altura < 0:
            raise ValueError("Valor invalido inserido! Tente novamente")
        self._altura = altura
        self._area = self._base * self._altura
        self._medidas = f"base: {self._base}\naltura: {self._altura}\narea: {self._area}"

    @property
    def area(self):
        return self._area
    @area.setter
    def area(self):
        raise PermissionError("A Área não pode ser alterada dessa forma!")

    @property
    def medidas(self):
        return f"base: {self._base}\naltura: {self._altura}\narea: {self._area}"
    @medidas.setter
    def medidas(self, valores:tuple):
        if type(valores) != tuple:
            raise TypeError("As medidas devem ser informadas dentro de uma tupla")
        if len(valores) != 2:
            raise SyntaxError("Informa uma tupla com 2 valores numéricos")
        if isinstance(valores[0], int) or isinstance(valores[0], float):
            self._base = valores[0]
        else:
            raise TypeError("A Base deve ser um número")
        if isinstance(valores[1], int) or isinstance(valores[1], float):
            self._altura = valores[1]
        else:
            raise TypeError("A Altura deve ser um número")
        self._area = self._base * self._altura