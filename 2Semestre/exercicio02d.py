try:
    def funcao_1():
        print('Início da função 1')
        try:
            funcao_2()
        except IndexError:
            print('Acesso a indice inexixtente')
        print('Fim da função 1')


    def funcao_2():
        print('Início da função 2')
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for i in range(15):
            print(lista[i])
        print('Fim da função 2')


    print('Início do programa')
    funcao_1()
    print('Fim do programa')


