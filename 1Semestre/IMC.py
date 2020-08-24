peso=float(input())
altura=float(input())
imc=peso/(altura*altura)

if imc<20:
    print ("Abaixo do Peso")
else:
    if imc<=25:
        print ("Normal")
    elif imc<=30:
        print ("Excesso de peso")
    elif imc<=35:
        print ("Obesidade")
    else: print ("Obesidade Mórbida")
