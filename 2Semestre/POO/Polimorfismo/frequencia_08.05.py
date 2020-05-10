from abc import ABC, abstractmethod


class Operacao(ABC):
    @abstractmethod
    def calcular(self, x, y):
        pass


class Soma(Operacao):
    def calcular(self, x, y):
        soma = self.soma = x + y
        return soma


class Subtracao(Operacao):
    def calcular(self, x, y):
        sub = self.sub = x - y
        return sub


class Multiplicacao(Operacao):
    def calcular(self, x, y):
        multi = self.multi = x * y
        return multi


class Divisao(Operacao):
    def calcular(self, x, y):
        div = self.div = x / y
        return div

# Programa Principal


soma = Soma()
sub = Subtracao()
div = Divisao()
mult = Multiplicacao()

print(soma.calcular(10, 5))      # 15
print(sub.calcular(10, 5))       # 5
print(div.calcular(10, 5))       # 2.0
print(mult.calcular(10, 5))      # 50
