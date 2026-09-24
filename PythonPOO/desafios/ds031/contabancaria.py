from hashlib import sha256
from pwinput import pwinput
class ContaBancaria:
    """
    Cria uma conta bancaria que permite saques e depositos.
    """
    def __init__(self, id, nome, saldo,senha=None):
        self.id = id #Público
        self._titular = nome #Protegido
        self.__saldo = saldo #Privado
        if senha is None:
            senha = pwinput('Digite sua senha: ', mask='*')
            self.__hash = sha256(senha.encode('utf-8')).hexdigest()
        else:
            self.__hash =sha256(senha.encode('utf-8')).hexdigest()
        print(f'Conta {self.id} criada com sucesso! Conta bancaria com saldo R${self.__saldo:,.2f}')
    def __str__(self):
        return f'A conta {self.id} de {self._titular} tem R${self.__saldo:,.2f} de saldo'
    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f'Deposito autorizado de R${valor:,.2f} autorizado na conta {self.id}')
    def sacar(self, valor):
        verificar = pwinput('Senha: ', mask='*')
        if sha256(verificar.encode('utf-8')).hexdigest() == self.__hash:
            valor = abs(valor)
            if valor <= self.__saldo:
                self.__saldo -= valor
                print(f'Saque autorizado de R${valor:,.2f} autorizado na conta {self.id}')

            else:
                print(f'Saque de {valor:,.2f} NEGADO na conta {self.id}, SALDO INSUFICIENTE')
        else:
            print("Senha invalida, não é possivel sacar!")



