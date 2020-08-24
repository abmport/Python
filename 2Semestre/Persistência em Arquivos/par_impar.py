arquivo = open("pares.txt")

lista = []

for linha in arquivo:
    cont = 0
    lista.append(int(linha))
    par = lista[cont] % 2
    if par == 0:
        print(int(linha), "é par msm")
    cont = cont + 1
