from abc import ABC, abstractmethod
import locale

# Configurando a localização para formatar valores como moeda do Brasil (R$)
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class Pagamento(ABC):
    def __init__(self):
        self._valor = None

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        if valor > 0:
            self._valor = valor
        else:
            raise ValueError("O pagamento só pode ser efetuado para valores positivos.")

    @property
    def f_valor(self):
        # Utiliza o locale para formatar automaticamente com R$, pontos e vírgulas [00:10:07]
        return locale.currency(self._valor, grouping=True)

    @abstractmethod
    def pagar(self, valor: float):
        pass

class Boleto(Pagamento):
    def pagar(self, valor: float):
        try:
            self.valor = valor
            # Aqui iria o código real para processar o boleto
            return f"Pagamento confirmado de {self.f_valor} via Boleto"
        except Exception:
            return f"Falha no pagamento de {self.f_valor} via Boleto"

class Pix(Pagamento):
    def pagar(self, valor: float):
        try:
            self.valor = valor
            # Aqui iria o código real para processar o Pix
            return f"Pagamento confirmado de {self.f_valor} via Pix"
        except Exception:
            return f"Falha no pagamento de {self.f_valor} via Pix"

class CartaoCredito(Pagamento):
    def pagar(self, valor: float):
        try:
            self.valor = valor
            # Aqui iria o código real para processar o Cartão de Crédito
            return f"Pagamento confirmado de {self.f_valor} via Cartão de Crédito"
        except Exception:
            return f"Falha no pagamento de {self.f_valor} via Cartão de Crédito"


# Função de Duck Typing (Polimorfismo Pythônico) [00:15:12]
def finalizar_compra(tipo_pague: Pagamento, valor: float):
    print(tipo_pague.pagar(valor))