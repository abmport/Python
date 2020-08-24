continua = True
while continua:
    try:
        x = int(input('Primeiro valor:'))
        y = int(input('Segundo valor:'))
        z = x / y
    except ZeroDivisionError:
        print('O segundo valor deve ser diferente de zero')
    except ValueError:
        print('O valor informado deve ser um número inteiro')
    except Exception:
        print('Algum outro erro ocorreu')
    else:
        print('Valores corretos')
        print('O resultado da divisão é:', z)
        continua = False
