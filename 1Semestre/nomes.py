print ("CONTADOR DE LETRAS: \n")
palavras=input("Digite uma palavra: \n")
letras=input("Digite a letra que deseja contar: \n")
letras_2=letras
guardar_letras=[]

contador=0
contador2=0
contador3=0

print("\n")
for letras in palavras:
    if letras==letras_2:
        contador2=contador2+1
    if letras==letras:
        guardar_letras.append(letras)
        print("\n",guardar_letras[contador])
        contador=contador+1
    if letras==0:
        contador3=contador3+1

print ("\n")        
print ("A palavra ou frase digitada possui: ",contador,"letras")
print ("A palavra ou frase digitada possui: ",contador2,"letras",letras_2)
print ("A palavra ou frase digitada possui: ",contador3,"espaços")
input()
