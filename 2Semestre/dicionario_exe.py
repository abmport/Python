print ("Exercicio Aula 03 - Dicionários \n \n")

produtos={}

produtos["Nescau"]=4.50
produtos["Toddy"]=5.90
produtos["Leite"]=2.50
produtos["Jack-Daniels"]=99.90
produtos["Ventilador"]=169.90

for item in produtos:
    if produtos[item]>50.00:
        print (item, produtos[item])

print ("2º Exercicio Python - Dicionário \n \n")


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



