class Produto:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor


class Cliente:
    def __init__(sel, nome):
        sel.nome = nome


class Carrinho:
    def __init__(self, cliente):
        self.cliente = cliente
        self.produtos = []

    def adicionar_produto(self, prod):
        self.produtos.append(prod)

    def listar_produtos(self):
        for prod in self.produtos:
            print(prod.descricao, prod.valor)

    def calcular_total(self):
        soma = 0
        for prod in self.produtos:
            soma += prod.valor
        return soma


cliente1 = Cliente("Abner")
prod1 = Produto("TV", 2500.0)
prod2 = Produto("Notebook", 3000.0)
prod3 = Produto("Pen Drive", 15.00)

carrinho = Carrinho(cliente1)
carrinho.adicionar_produto(prod1)
carrinho.adicionar_produto(prod2)
carrinho.adicionar_produto(prod3)
carrinho.listar_produtos()

print("Total: ", carrinho.calcular_total())
