# Atividade Contínua 01
# Aluno 01: Abner De Melo Porto
# Aluno 02: Amanda Conceição Gomes
# Aluno 03: Vinícius Tertuliano da Silva


def adicionar_aluno(alunos, nome, notas):
    '''
    Essa função acrescenta os dados de um novo aluno no dicionário
    Entrada:
        alunos: dicionario com os dados dos alunos
        nome: nome do aluno (chave)
        notas: lista com as notas de um aluno (valor)
    Retorno:
        A função deve retornar o dicionário com as modificações realizadas
    Observação:
        Caso a chave já exista no dicionário,
        deve retornar o dicionário sem nenhuma alteração.
    '''


def remover_aluno(alunos, nome):
    '''
    Essa função exclui os dados de um aluno do dicionário.
    Entrada:
        alunos: dicionario com os dados dos alunos
        nome: nome do aluno (chave)
    Retorno:
        A função deve retornar o dicionário com as modificações realizadas
    Observação:
        Caso a chave não exista no dicionário,
        deve retornar o dicionário sem nenhuma alteração.
    '''


def pesquisar_aluno(alunos, nome):
    '''
    Essa função deve retornar a lista com as notas de um aluno.
    Entrada:
        alunos: dicionario com os dados dos alunos
        nome: nome do aluno (chave)
    Retorno:
        A função deve retornar uma lista com as notas do aluno
    Observação:
        Caso a chave não exista, deve retornar uma lista vazia
    '''


def calcular_media(alunos, nome):
    
    if nome in alunos:
        media = sum(alunos[nome]) / len(alunos[nome])
        return media
    else:
        return 0
    
    '''
    Essa função retorna a média de um aluno.
    Entrada:
        alunos: dicionario com os dados dos alunos
        nome: nome do aluno (chave)
    Retorno:
        A função deve retornar a média do aluno
    Observação:
        Caso a chave não exista, deve retornar zero
    '''


def calcular_media_turma(alunos):
    '''
    Essa função retorna a média geral da turma
    (soma de todas as notas dividida pela quantidade de todas as notas)
    Entrada:
        alunos: dicionario com os dados dos alunos
    Retorno:
        A função deve retornar a média geral da turma
    '''
