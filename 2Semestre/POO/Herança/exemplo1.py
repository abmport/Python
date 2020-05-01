class Pessoa:                               # Classe mãe
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def exibir(self):
        print("Nome:", self.nome)
        print("CPF:", self.cpf)
        print("Email:", self.email)


class Aluno(Pessoa):                        # Classe filha
    def __init__(self, nome, cpf, email, ra):
        super().__init__(nome, cpf, email)      # chama construtor da classe mãe
        self.ra = ra

    def exibir(self):
        super().exibir()                        # chama exibir da classe mãe
        print("RA:", self.ra)
    
    def calcular_media(self, n1, n2):
        media = (n1+n2)/2
        return media

class Monitor(Aluno):
    def __init__(self, nome, cpf, email, ra, disciplina):
        super().__init__(nome, cpf, email, ra)
        self.disciplina = disciplina

    def exibir(self):
        super().exibir()
        print("Disciplina", self.disciplina)


aluno = Aluno("Maria", 12345, "email", 2034543)
aluno.exibir()
print(aluno.calcular_media(10, 7))

print("----------------------------")
m = Monitor("Joao", 23456, "emailmonitor", 2343, "Programação")
m.exibir()
