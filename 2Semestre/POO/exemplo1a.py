'''
Crie uma classe Livro com os atributos:
- titulo
- autor
- preco
Crie o método:
- exibir_dados (exibe o titulo, nome do autor e preço do livro)
'''


class Livro:
    def __init__(self):
        self.titulo = None
        self.autor = None
        self.preco = 0

    def exibir_dados(self):
        print("Titulo: ", self.titulo)
        print("Autor: ", self.autor)
        print("Preço: ", self.preco)

    # exemplo de metodo para realizar cadastro dos atributos pelo usuário
    def cadastrar(self):
        t = input("Titulo do livro: ")
        a = input("Nome do autor: ")
        p = float(input("Preço do livro: "))
        self.titulo = t
        self.autor = a
        self.preco = p


# cria objeto
meu_livro = Livro()
meu_livro.cadastrar()
meu_livro.exibir_dados()

# cria outro objeto cadastrado pelo usuario
livro1 = Livro()
livro1.cadastrar()
