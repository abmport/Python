atividades = {}
nota = [0, 0]


def media(atividades):

    for a in atividades:
        med = 0
        for y in range(len(atividades[a])):
            med += atividades[a][y]
        med = med / len(atividades[a])
        print("O aluno {} tem a média de {}".format(a, med))


for i in range(3):
    nome = input("Digite seu nome: ")
    for x in range(2):
        nota[x] = float(input("Digite sua nota: "))
    atividades[nome] = nota

media(atividades)
