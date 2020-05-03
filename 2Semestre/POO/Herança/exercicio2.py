class Animal:
    def __init__(self, nome, cor, numero_patas):
        self.nome = nome
        self.cor = cor
        self.numero_patas = numero_patas

    def exibir_dados(self):
        print("Nome: ", self.nome)
        print("Cor: ", self.cor)
        print("Patas: ", self.numero_patas)


class Cachorro(Animal):
    def __init__(self, nome, cor, numero_patas, raca):
        super().__init__(nome, cor, numero_patas)
        self.raca = raca

    def exibir_dados(self):
        super().exibir_dados()
        print("Raça:", self.raca)


a = Animal("Nome", "Branca", 4)
c = Cachorro("Rex", "Marrom", 4, "Vira Lata")


a.exibir_dados()
print("--------------------")
c.exibir_dados()

