#Exercicio Aula 03 - Dicionários
'''
produtos={}

produtos["Nescau"]=4.50
produtos["Toddy"]=5.90
produtos["Leite"]=2.50
produtos["Jack-Daniels"]=99.90
produtos["Ventilador"]=169.90

for item in produtos:
    if produtos[item]>50.00:
        print (item, produtos[item])

#("2º Exercicio Python - Dicionário \n \n")


def calcular_media(notas, nome):
    if nome in notas:
        media = sum(notas[nome]) / len(notas[nome])
        return media
    else:
        return 0

notas = {}

for i in range(3):
    nome = input("Nome: ")
    nota1 = float(input("Primeira Nota: "))
    nota2 = float(input("Segunda Nota: "))
    notas[nome] = [nota1, nota2]

print(notas)

nome = input("Digite o nome de um aluno: ")
media = calcular_media(notas, nome)

print ("Média do aluno: ", media)


#AC01
#Função para Pesquisar Aluno


def pesquisar_aluno(alunos, nome):
    if nome in alunos:
        print ("O nome aluno é: {}".format(nome))
        print ("As notas do {} são {}: ".format(nome, alunos[nome]))
    else:
        return print ([])

nome = "sdds"
pesquisa = pesquisar_aluno(notas, nome)
'''
#Função para calcular media turma

alunos={}

alunos["Abner"]=[4.50]
alunos["Mandy"]=[5.90]
alunos["Vinicius"]=[2.50]


def calcular_media_turma(alunos):
    s=0
    for x in alunos:
        s=s+float(alunos[x])/len(alunos)
    return s

'''
def calcular_media_turma(alunos):
    somaNotas = 0
    somaTnotas = 0
    for aluno in alunos:
        somaNotas += sum(alunos[aluno])
        somaTnotas += len(alunos[aluno])
    return '{:.1f}'.format(somaNotas/somaTnotas)
'''

print(calcular_media_turma(alunos))

