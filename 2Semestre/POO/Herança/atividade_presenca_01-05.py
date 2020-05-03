# Atividade Frequência 01.05 (Reposição)
# Herança


class Veiculo:
    def __init__(self, marca, modelo, rodas):
        self.marca = marca
        self.modelo = modelo
        self.rodas = rodas
        self.__velocidade = 0

    def set_velocidade(self, velocidade):
        self.__velocidade = velocidade

    def acelerar(self, valor):
        self.__velocidade += valor

    def frear(self, valor):
        self.__velocidade -= valor

    def get_velocidade(self):
        return self.__velocidade

    def imprimir_informacoes(self):
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Rodas: ", self.rodas)


class Carro(Veiculo):
    def __init__(self, marca, modelo, rodas, potencia):
        super().__init__(marca, modelo, rodas)
        self.potencia = potencia

    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print("Potencia: ", self.potencia)
        print("\n")


class Moto(Veiculo):
    def __init__(self, marca, modelo, rodas, partida_eletrica):
        super().__init__(marca, modelo, rodas)
        self.partida_eletrica = False

    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print("Partida Elétrica: ", self.partida_eletrica)
        print("\n")


class Bicicleta(Veiculo):
    def __init__(self, marca, modelo, rodas, marchas, bagageiro):
        super().__init__(marca, modelo, rodas)
        self.marchas = 0
        self.bagageiro = False

    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print("Marchas: ", self.marchas)
        print("Bagageiro", self.bagageiro)
        print("\n")


# Programa Principal

carro = Carro("Ford", "Ka", 4, 85.0)
moto = Moto("Honda", "Biz", 2, True)
bike = Bicicleta("Caloi", "Elite", 2, 18, True)

carro.acelerar(30)
carro.frear(10)
moto.acelerar(100)
moto.frear(20)
bike.acelerar(20)
bike.frear(5)

# imprime os valores de todos os atributos de cada Classe
carro.imprimir_informacoes()
bike.imprimir_informacoes()
moto.imprimir_informacoes()

# testar a velocidade atual
print("Velocidade atual do Carro:", carro.get_velocidade())       # 20
print("Velocidade atual da Moto:", moto.get_velocidade())         # 80
print("Velocidade atual da Bicicleta:", bike.get_velocidade())    # 15
