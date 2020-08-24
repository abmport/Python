class Filme:
    def __init__(self, titulo, genero):
        self.__titulo = titulo
        self.__genero = genero

    # Métodos Get
    def get_titulo(self):
        return self.__titulo

    def get_genero(self):
        return self.__genero

    # Métodos Set
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_genero(self, genero):
        self.__genero = genero


lista_filmes = []

for i in range(3):
    titulo = input("Digite o Titulo: ")
    genero = input("Digite o Genêro: ")
    filme = Filme(titulo, genero)
    lista_filmes.append(filme)

for i in lista_filmes:
    print("Título: ", i.get_titulo())
    print("Genêro: ", i.get_genero())
