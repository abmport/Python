# Atividade Contínua 01
# Aluno 01: Abner De Melo Porto
# Aluno 02: Amanda Conceição Gomes
# Aluno 03: Vinícius Tertuliano da Silva


def adicionar_aluno(alunos, nome, notas):
    if nome in alunos:
        return alunos
    else:
        alunos[nome] = notas
    return alunos


def remover_aluno(alunos, nome):
    if nome in alunos:
        alunos.pop(nome)
    return alunos


def pesquisar_aluno(alunos, nome):
    if nome in alunos:
        return alunos[nome]
    else:
        return []


def media(atividades):
     for a in atividades:
        med = 0
        for y in range(len(atividades[a])):
            med += atividades[a][y]
        med = med / len(atividades[a])
        return a, med

def calcular_media_turma(alunos):
    somaNotas = 0
    somaTnotas = 0
    for aluno in alunos:
        somaNotas += sum(alunos[aluno])
        somaTnotas += len(alunos[aluno])
    return '{:.1f}'.format(somaNotas/somaTnotas)

