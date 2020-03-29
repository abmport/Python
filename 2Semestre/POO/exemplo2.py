'''
Classe Aluno
Atributos:
 - RA
 - nome
 - disciplinas (lista com as dsciplinas que o aluno cursa)
Métodos:
 - adicionar_disciplina (recebe o nome da disciplina e adiciona na lista)
'''


class Aluno:
    def __init__(self, ra, nome):
        self.ra = ra
        self.nome = nome
        self.lista_disciplinas = []

    def adicionar_disciplina(self, disc):
        self.lista_disciplinas.append(disc)

    def exibir(self):
        print("RA: ", self.ra)
        print("Nome: ", self.nome)
        print("Disciplinas: ", self.lista_disciplinas)


aluno1 = Aluno(9999999, "Paulo")
aluno1.adicionar_disciplina("Linguagem de Programação II")
aluno1.adicionar_disciplina("Banco de Dados")
aluno1.exibir()
