print("Contando a quantidade linhas no arquivo: \n")
cont = 0
arq = open('arquivo.txt', 'r')
for linha in arq:
    cont = cont + 1
print("Número de linhas no arquivo: ", cont)
arq.close
