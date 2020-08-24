class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.saldo = 0

    def consultar_saldo(self):
        print("Saldo: ", self.saldo)

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")


class ContaCorrente(Conta):
    def __init__(self, numero, titular):
        super().__init__(numero, titular)
        self.limite = 500

    def sacar(self, valor):                     # sobrescrita de método
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
        else:
            print("Erro na operação de saque")


contacorrente = ContaCorrente(1234, "Paulo")
contacorrente.depositar(0)                    # executa metodo da classe mãe
# executa metodo da classe ContaCorrente
contacorrente.sacar(500)
contacorrente.consultar_saldo()                 # executa metodo da classe mãe
