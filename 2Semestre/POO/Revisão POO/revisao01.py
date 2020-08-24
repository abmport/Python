# construtor __init__
# definir atributos
# self Utilizado para acessar os atributos
'''

métodos é representado por uma função, ou seja, ações ou
comportamentos do objeto.

'''


class Livro:
    def __init__(self):
        self.titulo = None
        self.autor = None
        self.preco = 0

    def exibir_dados(self):
        print("O título do livro é: {} ".format(self.titulo))
        print("O autor do livro é: {}".format(self.autor))
        print("O preço do livro é: {}".format(self.preco))

# Método para o usuário cadastrar os atributos

    def cadastrar(self):
        t = input("Titulo do Livro: ")
        a = input("Nome do autor: ")
        p = float(input("Preço do Livro: "))
        self.titulo = t
        self.autor = a
        self.preco = p


meu_livro = Livro()
meu_livro.cadastrar()

meu_livro.exibir_dados()

'''
# Alteração do Preço
meu_livro.preco = 39.9
meu_livro.exibir_dados()
'''
