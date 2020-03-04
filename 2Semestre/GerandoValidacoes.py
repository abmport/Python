continua = True

while continua:
    try:
        n = int(input("Informe um nº inteiro positivo: \n"))
        if (n <= 0):
            raise TypeError
    except ValueError:
        print("O Valor informado não é do tipo inteiro.")
    except TypeError: 
        print("O número informado deve ser positivo:")
    except Exception:
        print("Ocorreu um erro! ")
    else:
        continua = False

print("O número informado é válido. \n")
print("O programa continua...")