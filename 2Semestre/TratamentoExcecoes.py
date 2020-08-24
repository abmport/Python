try:
    a = int(input("Digite um nº positivo: "))

    if a <= 0:
        raise ValueError
except ValueError:
    print ("Erro: Digite apenas números positivos!!!")
except Exception:
    print ("Algum outro erro aconteceu.")