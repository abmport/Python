try:
    nota = float(input("Informe uma nota: "))
    if nota < 0.00 or nota > 10.00:
        raise ValueError
except ValueError:
    print ("Erro: A nota é inválida!!! ")
else: 
    if nota >= 6:
        print ("Aprovado.")
    else: 
        print ("Reprovado.")