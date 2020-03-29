'''
Crie uma classe Livro com os atributos:
- titulo
- autor
- preco
Crie o método:
- exibir_dados (exibe o titulo, nome do autor e preço do livro)
'''


class Livro:
    # construtor recebe valores iniciais que serão atribuidos aos atributos
    def __init__(self, titulo, autor, preco):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco

    def exibir_dados(self):
        print("Titulo: ", self.titulo)
        print("Autor: ", self.autor)
        print("Preço: ", self.preco)


# cria objeto
outro_livro = Livro("Titulo do Livro", "Nome do autor do livro", 50.0)
outro_livro.exibir_dados()

# cria outro objeto
livro1 = Livro("Titulo", "nome do autor", 30)
# modifica o preço
livro1.preco = 29.90
livro1.exibir_dados()
