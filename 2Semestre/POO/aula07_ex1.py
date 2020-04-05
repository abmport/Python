class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Livro:
    def __init__(self, titulo, paginas, autor):
        self.titulo = titulo
        self.paginas = paginas
        self.autor = autor

    def exibir_dados(self):
        print("Titulo: ", self.titulo)
        print("Paginas: ", self.paginas)
        print("Autor: ", self.autor.nome)
        print("Idade do autor", self.autor.idade)


pessoa1 = Pessoa("J. K. Rowling", 56)
book = Livro("Harry Potter", 350, pessoa1)

book.exibir_dados()
