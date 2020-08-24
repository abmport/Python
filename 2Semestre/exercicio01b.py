continua = True
while continua:
    try:
        x = int(input('Primeiro valor:'))
        y = int(input('Segundo valor:'))
    except ValueError:
        print('O valor informado deve ser um número inteiro')
    else:
        try:
            z = x / y
        except ZeroDivisionError:
            print('O segundo valor deve ser um número diferente de zero')
        else:
            continua = False
            print('O resultado da divisão é:', z)
