class Conta:
    def __init__(self, numero, titular, senha):
        self.numero = numero
        self.titular = titular
        self.__senha = senha
        self.__saldo = 0

    def depositar(self, valor, senha):
        if senha == self.__senha:
            self.__saldo += valor
            return True
        else:
            print("Senha invalida")
            return False

    def sacar(self, valor, senha):
        if senha == self.__senha:
            if valor <= self.__saldo:
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

# PErmite tres tentativas para acertar a senha
tentativas = 0
while tentativas < 3:
    valor = float(input("Valor de deposito: "))
    senha = input("Senha: ")

    if conta1.depositar(valor, senha) is False:
        tentativas += 1
    else:
        print("Saldo da conta: ", conta1.get_saldo(senha))
        break
