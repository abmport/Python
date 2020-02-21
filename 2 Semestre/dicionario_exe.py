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

import calcular_media

cont=0

alunos={}

while cont<=2:
    aluno1=input("Digite o 1 º nome: ")
    n1=input("Digite a 1 nota: ")
    n2=input("Digite a 2 nota: ")
    cont+=1

print ("/n /n")

nome = input ("Digite o nome para calculo da media: ")
media = calcular_media (notas,nome)






