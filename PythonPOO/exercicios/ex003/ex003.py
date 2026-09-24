class ContaBancaria:
    """
    Cria uma conta bancaria que permite saques e depositos.
    """
    def __init__(self, id, nome, saldo):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {self.id} criada com sucesso! Conta bancaria com saldo R${self.saldo:,.2f}')
    def __str__(self):
        return f'A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo'
    def depositar(self, valor):
        self.saldo += valor
        print(f'Deposito autorizado de R${valor:,.2f} autorizado na conta {self.id}')
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque autorizado de R${valor:,.2f} autorizado na conta {self.id}')

        else:
            print(f'Saque de {valor:,.2f} NEGADO na conta {self.id}, SALDO INSUFICIENTE')



c1 = ContaBancaria(112, 'Gustavo', 3000)
c1.depositar(500)
c1.sacar(2000)
print(c1)