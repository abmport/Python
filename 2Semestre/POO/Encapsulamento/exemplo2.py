class Conta:
    def __init__(self, numero, titular, senha):
        self.numero = numero
        self.titular = titular
        self.__senha = senha
        self.__saldo = 0

    def depositar(self, valor, senha):
        if senha == self.__senha:
            self.__saldo += valor
        else:
            print("Senha Invalida")

    def sacar(self, valor, senha):
        if senha == self.__senha:
            self.__saldo -= valor
        else:
            print("Senha Invalida")

    def get_saldo(self, senha):
        if senha == self.__senha:
            return self.__saldo
        else:
            print("Senha Invalida")
            return None


conta1 = Conta(123, "Paulo", "123456")

valor = float(input("Valor do deposito: "))
senha = input('Informe a senha: ')
conta1.depositar(valor, senha)
print("Saldo: ", conta1.get_saldo(senha))

valor = float(input("Valor do saque: "))
senha = input('Informe a senha: ')
conta1.sacar(valor, senha)
print("Saldo: ", conta1.get_saldo(senha))
