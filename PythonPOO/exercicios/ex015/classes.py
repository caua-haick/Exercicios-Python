class Porta:
    def abrir(self):
        print("Girando a maçaneta e empurrando/puxando a porta.")

class Empresa:
    def abrir(self):
        print("Vá ao portal do empreendedor com a documentação para abrir o CNPJ.")

class Ovo:
    def abrir(self):
        print("Quebre a casca com um garfo e separe as partes sobre a frigideira.")

class Pedra:
    pass

# Método polimórfico pythônico (Duck Typing)
def tentar_abrir(obj):
    try:
        obj.abrir()
    except AttributeError:
        print(f"Encontrei problemas ao tentar abrir um objeto do tipo {obj.__class__.__name__}.")