print("Teste de abertura de arquivos em Python")
print("Testando abrir um arquivo de texto armazenado no PC \n")

manipulador = open('arquivo.txt', 'r')
for linha in manipulador:
    linha = linha.rstrip()
    print(linha)
manipulador.close
