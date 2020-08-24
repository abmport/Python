try:
    a = int(input("Digite o 1º número: \n"))
    b = int(input("Digite o 2º número: \n"))
    c = a/b
except ZeroDivisionError:
    print ("Ops, O segundo nº não poder ser 0! :)")
except ValueError:
    print ("Ops, Você não informou o número! :)")
except Exception:
    print ("Ops, Algo deu errado :(")
else:
    print (c)