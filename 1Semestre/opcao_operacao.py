n1=int(input("Digite o 1º número: "))
n2=int(input("Digite o 2º número: "))

escolha=int(input("Escolha uma operação: \n 1 - Média entre os números digitados \n 2 - Diferença do maior pelo menor \n 3 - Produto entre os números digitados \n"))

media=(n1+n2)/2

if n1>n2: diferenca=n1-n2
else: diferenca=n2-n1

produto=n1*n2

if escolha==1: print ("A media é: ",media)
elif escolha==2: print ("A diferenca é: ",diferenca)
elif escolha==3: print ("O produto é: ",produto)
else: print ("Escolha uma das opções de 1 a 3! ")

input()
