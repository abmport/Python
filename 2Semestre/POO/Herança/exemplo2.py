class Conta:                            # classe mãe
    def __init__(self, agencia, numero, titular):
        self.agencia = agencia
        self.numero = numero
        self.titular = titular
        self.__saldo = 0  # atributo privado não é herdado pelas classes filhas

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        self.__saldo += valor

    def __teste(self):                      # metodos privados não são herdados
        print("Teste")


class ContaEspecial(Conta):
    def __init__(self, agencia, numero, titular, limite):
        super().__init__(agencia, numero, titular)
        self.limite = limite

    def calcular_juros(self):
        saldo = self.get_saldo()
        self.set_saldo(saldo * 1.10)        # adiciona 10% no saldo


c = ContaEspecial(123, 35463, "Paulo", 500)
c.depositar(300)
# c.__teste()             # ERRO - metodo privado não é herdado
c.calcular_juros()
print(c.get_saldo())
