'''
Implemente a classe chamada Aluno com três atributos PRIVADOS:
    ra
    nome
    notas
Implemente um construtor que inicialize os atributos.
O atributo notas deve ser inicializado com uma lista vazia.
Implemente um conjunto de métodos get para cada atributo.
    get_ra
    get_nome
    get_notas
Implemente os métodos:
    incluir_nota: recebe como parâmetro uma nota e a inclui na lista de notas.
    calcular_media: retorna a média aritmética do aluno.
'''


# { IMPLEMENTE SEU CÓDIGO AQUI


class Aluno:
    def __init__(self, ra, nome):
        self.__ra = ra
        self.__nome = nome
        self.__notas = []

    def get_ra(self):
        return self.__ra

    def get_nome(self):
        return self.__nome

    def get_notas(self):
        return self.__notas

    def incluir_nota(self, nota):
        return self.__notas.append(nota)

    def calcular_media(self):
        notas = self.__notas
        soma = sum(notas)
        qtd = len(notas)
        return soma / qtd


# }


aluno1 = Aluno(123456, 'Rahul')
aluno1.incluir_nota(10)
aluno1.incluir_nota(9)
aluno1.incluir_nota(5)

print("RA:", aluno1.get_ra())                # RA: 123456
print("Nome:", aluno1.get_nome())            # Nome: Rahul
print("Notas:", aluno1.get_notas())          # Notas: [10, 9, 5]
print("Média:", aluno1.calcular_media())     # Média: 8.0

aluno2 = Aluno(456789, 'Marya')
aluno2.incluir_nota(8)
aluno2.incluir_nota(9.5)
aluno2.incluir_nota(5)

print("RA:", aluno2.get_ra())                # RA: 456789
print("Nome:", aluno2.get_nome())            # Nome: Marya
print("Notas:", aluno2.get_notas())          # Notas: [8, 9.5, 5]
print("Média:", aluno2.calcular_media())     # Média: 7.5
