print("Retornando as palavras definida pelo usuario \n")
palavra = input("Qual palavra deseja buscar? \n")
arq = open('arquivo.txt', 'r')
cont = 0

for linha in arq:
    linha = linha.rstrip()
    if palavra in linha:
        cont = cont + 1
        print(linha)
if cont == 0:
    print("\nPalavra não encontrada!!!")
else:
    print("\nEncontrado", cont, "linhas")
