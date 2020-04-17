# importar módulo para ocultar digitação de senha
from getpass import getpass


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
            print("Senha invalida")

    def sacar(self, valor, senha):
        if senha == self.__senha:           # verifica a senha
            if valor <= self.__saldo:       # verifica se tem saldo suficiente
                self.__saldo -= valor
            else:
                print("Saldo insuficiente")
        else:
            print("Senha invalida")

    def get_saldo(self, senha):
        if senha == self.__senha:
            return self.__saldo
        else:
            print("Senha invalida")
            return None


conta1 = Conta(123, "Paulo", "123456")

valor = float(input("Valor de deposito: "))
# metodo getpass solicita a senha mas não exibe os caracteres digitados
senha = getpass("Digite a Senha: ")

conta1.depositar(valor, senha)
print("Saldo da conta: ", conta1.get_saldo(senha))

valor = float(input("Valor de saque: "))
# metodo getpass solicita a senha mas não exibe os caracteres digitados
senha = getpass("Digite a Senha: ")

conta1.sacar(valor, senha)
print("Saldo da conta: ", conta1.get_saldo(senha))
