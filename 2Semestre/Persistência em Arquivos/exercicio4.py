print("Retornando apenas as linha que possuem a palavra Python\n")
arq = open('arquivo.txt', 'r')
cont = 0
for linha in arq:
    linha = linha.rstrip()
    if 'Python' in linha:
        cont = cont + 1
        print(linha)
