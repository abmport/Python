def adicionar_aluno(alunos, ra, nome):
    try:
        if ra in alunos:
            raise TypeError
        if ra < 1000000 or ra > 10000000:
            raise ValueError
    except TypeError:
        print('RA já existente')
    except ValueError:
        print('RA inválido')
    else:
        alunos[ra] = nome

def busca_aluno(alunos, ra):
    try:
        if ra not in alunos:
            raise KeyError
    except KeyError:
        print('RA Inexistente')
    else:
        return alunos[ra]

alunos = {}
adicionar_aluno(alunos, 1912541, 'Paulo')
adicionar_aluno(alunos, 1821125, 'João')
adicionar_aluno(alunos, 1912548, 'Ana')
print(busca_aluno(alunos, 1912541))
print(busca_aluno(alunos, 9999999))
