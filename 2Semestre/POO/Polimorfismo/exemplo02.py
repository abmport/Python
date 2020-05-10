from abc import ABC, abstractmethod         # importar modulos

# classe abstrata (não pode ser instanciada)


class Conta(ABC):
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.saldo = 0

    @abstractmethod                         # metodo abstrato
    def sacar(self, valor):
        pass

    @abstractmethod                         # metodo abstrato
    def depositar(self, valor):
        pass

    def consultar_saldo(self):              # metodo concreto
        print("Saldo:", self.saldo)

# É obrigatorio implementar os metodos abstratos da classe mãe em todas as
# classes filhas


class Poupanca(Conta):
    def __init__(self, numero, titular):
        super().__init__(numero, titular)

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Erro: Saldo Insuficiente")

    def depositar(self, valor):
        self.saldo += valor


c = Poupanca(123, "Paulo")
c.depositar(100)
c.sacar(50)
c.consultar_saldo()
