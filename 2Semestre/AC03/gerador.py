# Atividade Contínua 03
# Abner de Melo Porto
# Vinicius Tertuliano
# Laura Tazue


class Gerador:
    def __init__(self, nome, potencia, capacidade, tanque):
        self.__nome = nome                # nome
        self.__potencia = potencia        # Potencia do gerador
        self.__capacidade = capacidade    # o quanto pode gerar de energia
        self.__combustivel = tanque       # Armazena o tanque de combustevel
        self.__tanque = tanque            # quanto de combustivel o tanque tem
        self.__status = 'Desligado'             # Ligado / Desligado

    def get_nome(self):
        return self.__nome

    def set_titulo(self, nome):
        self.__nome = nome

    def get_potencia(self):
        return self.__potencia

    def set_potencia(self, potencia):
        self.__potencia = potencia

    def get_capacidade(self):
        return self.__capacidade

    def set_capacidade(self, capacidade):
        self.__capacidade = capacidade

    def get_combustivel(self):
        return self.__combustivel

    def set_combustivel(self, combustivel):
        self.__combustivel = combustivel

    def get_tanque(self):
        return self.__tanque

    def set_tanque(self, tanque):
        self.__tanque = tanque

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def ligar_gerador(self):
        self.__combustivel -= 50
        return self.set_status('Ligado')

    def desligar_gerador(self):
        return self.set_status('Desligado')

    def abastecer_tanque(self, quantidade):
        q = quantidade
        self.__combustivel += q
        return self.__combustivel
