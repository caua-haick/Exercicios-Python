class Numero:
    def __init__(self, valor=0):
        self.valor = valor

    def dobrar(self):
        self.valor *= 2

    def __str__(self):
        return f"Tenho o valor {self.valor} dentro do número."

class Texto:
    def __init__(self, txt=""):
        self.texto = txt

    def dobrar(self):
        self.texto = f"{self.texto} {self.texto}"

    def __str__(self):
        return f"Tenho o texto '{self.texto}' dentro do texto."

class Lista:
    def __init__(self, lst=None):
        self.valores = lst if lst is not None else []

    def dobrar(self):
        self.valores += self.valores

    def __str__(self):
        return f"Tenho os itens {self.valores} dentro da lista."

class Papel:
    def __init__(self):
        self.dobrado = False

    def dobrar(self):
        self.dobrado = True

    def __str__(self):
        estado = "dobrado" if self.dobrado else "novo"
        return f"O papel está {estado}."

class Casa:
    def __str__(self):
        return "Era uma casa muito engraçada."

# Método polimórfico pythônico (Duck Typing)
def tente_dobrar(obj):
    try:
        obj.dobrar()
    except AttributeError:
        print(f"Tive dificuldades para dobrar {obj.__class__.__name__}.")