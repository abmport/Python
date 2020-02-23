# Atividade Contínua 01
# Aluno 01: Abner De Melo Porto
# Aluno 02: Amanda Conceição Gomes
# Aluno 03: Vinícius Tertuliano da Silva

def adicionar_aluno(alunos, nome, notas):
    if nome in alunos:
        return alunos
    else:
        alunos[nome]=notas
    return alunos

def remover_aluno(alunos, nome):
    if nome in alunos:
        alunos.pop(nome)    
    return alunos 

def pesquisar_aluno(alunos, nome):    
    if nome in alunos:
        print ("O nome aluno é: {}".format(nome))
        print ("As notas do {} são {}: ".format(nome, alunos[nome]))
    else:
        return print ([])
