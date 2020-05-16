file1 = open("pares.txt", "r")
file2 = open("impares.txt", "r")

lista = []

for i in file1:
    lista.append(int(i))

for i in file2:
    lista.append(int(i))

lista.sort()

file3 = open("numeros.txt", "w")

for i in lista:
    file3.write(str(i) + "\n")

file1.close()
file2.close()
file3.close()
