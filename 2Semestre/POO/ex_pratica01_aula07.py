class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.carro = None

    def comprar_carro(self, carro):
        self.carro = carro


class Carro:
    def __init__(self, marca, modelo, placa, ano):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano


meucarro = Carro("VW", "Gol", "AAA-0000", 2015)
eu = Pessoa("Abner", 25)
eu.comprar_carro(meucarro)
print("Meu nome: ", eu.nome)
print("Modelo do meu carro: ", eu.carro.modelo)
print("Placa do meu carro: ", eu.carro.placa)
