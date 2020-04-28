# Atividade Contínua 03
# Abner de Melo Porto
# Vinicius Tertuliano
# Laura Tazue

import sys
import gerador

gerador1 = gerador.Gerador("G1", "100", "5000", 500)
gerador2 = gerador.Gerador("G2", "80", "4000", 40)
gerador3 = gerador.Gerador("G3", "70", "3000", 350)
gerador4 = gerador.Gerador("G4", "60", "2000", 300)


def exibir_menu():
    print("1 - Acionamento manual de gerador")
    print("2 - Status dos geradores")
    print("3 - Status dos tanques de combustível")
    print("4 - Abastecer tanque de combustível")
    print("5 - Detalhes do gerador")
    print("6 - Sair \n")
    opcao_menu = int(input("Escolha uma opção: "))

    if opcao_menu <= 6 and opcao_menu >= 1:
        if opcao_menu == 1:
            acionamento_gerador()
        if opcao_menu == 2:
            return status_gerador()
        if opcao_menu == 3:
            return status_tanque()
        if opcao_menu == 4:
            return abastacer()
        if opcao_menu == 5:
            return detalhes_gerador()
        if opcao_menu == 6:
            return print("Encerrado com exito"), sys.exit
    else:
        return print("Opção Incorreta, digite novamente!"), exibir_menu()


def acionamento_gerador():
    nomeG = input("Informe o Nome do Gerador: ")
    # Verificações do gerador 1
    if nomeG == gerador1.get_nome():
        # validar se o gerador esta ligado
        if 'Desligado' == gerador1.get_status():
            print(nomeG, "está desligado. Deseja ligar? \n 1 - Sim \n 2 - Não")
            op = int(input())
            if op == 1:
                if gerador1.get_combustivel() >= 50:
                    gerador1.ligar_gerador()
                    print("{} foi {} com sucesso. ".format(
                        gerador1.get_nome(),
                        gerador1.get_status()))
                    exibir_menu()
                else:
                    print('{} Não pode ser ligado por falta de combustivel'
                          .format(gerador1.get_nome()))
                    exibir_menu()
            elif op == 2:
                exibir_menu()
        else:
            print(nomeG, "está Ligado. Deseja Desligar? \n 1 - Sim \n 2 - Não")
            op = int(input())
            if op == 1:
                gerador1.desligar_gerador()
                print("{} foi {} com sucesso. ".format(
                    gerador1.get_nome(), gerador1.get_status()))
                exibir_menu()
            elif op == 2:
                exibir_menu()
    # Verificações do gerador 2
    elif nomeG == gerador2.get_nome():
        if 'Desligado' == gerador2.get_status():
            print(nomeG, "está Desligado. Deseja ligar? \n 1 - Sim \n 2 - Não")
            op = int(input())
            if op == 1:
                if 'Ligado' == gerador1.get_status():
                    if gerador2.get_combustivel() >= 50:
                        gerador2.ligar_gerador()
                        print("{} foi {} com sucesso. ".format(
                            gerador2.get_nome(),
                            gerador2.get_status()))
                        exibir_menu()
                    else:
                        print('{} Não pode ser ligado por falta de combustivel'
                              .format(gerador2.get_nome()))
                        exibir_menu()
                else:
                    print("{} Não pode ser ligado por que {} está {}".format(
                        gerador2.get_nome(),
                        gerador1.get_nome(),
                        gerador1.get_status()))
                    exibir_menu()
            elif op == 2:
                exibir_menu()
        else:
            print(nomeG, "está Ligado. Deseja Desligar? \n 1 - Sim \n 2 - Não")
            op = int(input())
            if op == 1:
                gerador2.desligar_gerador()
                print("{} foi {} com sucesso. ".format(
                    gerador2.get_nome(), gerador2.get_status()))
                exibir_menu()
            elif op == 2:
                exibir_menu()
    # Verificações do gerador 3
    elif nomeG == gerador3.get_nome():
        if 'Desligado' == gerador3.get_status():
            print(nomeG, "está Desligado. Deseja ligar? \n 1 - Sim \n 2 - Não")
            op = int(input())
            if op == 1:
                if 'Ligado' == gerador1.get_status():
                    if gerador3.get_combustivel() >= 50:
                        gerador3.ligar_gerador()
                        print("{} foi {} com sucesso. ".format(
                            gerador3.get_nome(),
                            gerador3.get_status()))
                        exibir_menu()
                    else:
                        print('{} Não pode ser ligado por falta de combustivel'
                              .format(gerador3.get_nome()))
                        exibir_menu()
                else:
                    print("{} Não pode ser ligado por que {} está {}".format(
                        gerador3.get_nome(),
                        gerador1.get_nome(),
                        gerador1.get_status()))
                    exibir_menu()
            elif op == 2:
                exibir_menu()
        else:
            print(nomeG, "está Ligado. Deseja Desligar? \n 1 - Sim \n 2 - Não")
            op = int(input())
            if op == 1:
                gerador3.desligar_gerador()
                print("{} foi {} com sucesso. ".format(
                    gerador3.get_nome(), gerador3.get_status()))
                exibir_menu()
            elif op == 2:
                exibir_menu()
    # Verificações do gerador 4
    elif nomeG == gerador4.get_nome():
        if 'Desligado' == gerador4.get_status():
            print(nomeG, "está Desligado. Deseja ligar? \n 1 - Sim \n 2 - Não")
            op = int(input())
            if op == 1:
                if 'Ligado' == gerador1.get_status():
                    if gerador4.get_combustivel() >= 50:
                        gerador4.ligar_gerador()
                        print("{} foi {} com sucesso. ".format(
                            gerador4.get_nome(),
                            gerador4.get_status()))
                        exibir_menu()
                    else:
                        print('{} Não pode ser ligado por falta de combustivel'
                              .format(gerador4.get_nome()))
                        exibir_menu()
                else:
                    print("{} Não pode ser ligado por que {} está {}".format(
                        gerador2.get_nome(),
                        gerador1.get_nome(),
                        gerador1.get_status()))
                    exibir_menu()
            elif op == 2:
                exibir_menu()
        else:
            print(nomeG, "está Ligado. Deseja Desligar? \n 1 - Sim \n 2 - Não")
            op = int(input())
            if op == 1:
                gerador4.desligar_gerador()
                print("{} foi {} com sucesso. ".format(
                    gerador4.get_nome(), gerador4.get_status()))
                exibir_menu()
            elif op == 2:
                exibir_menu()


def status_gerador():
    print("Status dos Geradores: ")
    print(gerador1.get_nome(), gerador1.get_status())
    print(gerador2.get_nome(), gerador2.get_status())
    print(gerador3.get_nome(), gerador3.get_status())
    print(gerador4.get_nome(), gerador4.get_status())
    exibir_menu()


def status_tanque():
    print("Status dos Tanques:")
    if gerador1.get_combustivel() < (20 * gerador1.get_tanque())/100:
        print("{} - {} / {} (ABASTECER)".format(gerador1.get_nome(),
                                                gerador1.get_combustivel(),
                                                gerador1.get_tanque()))
    else:
        print("{} - {} / {} ".format(gerador1.get_nome(),
                                     gerador1.get_combustivel(),
                                     gerador1.get_tanque()))

    if gerador2.get_combustivel() < (20 * gerador2.get_tanque())/100:
        print("{} - {} / {} (ABASTECER)".format(gerador2.get_nome(),
                                                gerador2.get_combustivel(),
                                                gerador2.get_tanque()))
    else:
        print("{} - {} / {} ".format(gerador2.get_nome(),
                                     gerador2.get_combustivel(),
                                     gerador2.get_tanque()))

    if gerador3.get_combustivel() < (20 * gerador3.get_tanque())/100:
        print("{} - {} / {} (ABASTECER)".format(gerador3.get_nome(),
                                                gerador3.get_combustivel(),
                                                gerador3.get_tanque()))
    else:
        print("{} - {} / {} ".format(gerador3.get_nome(),
                                     gerador3.get_combustivel(),
                                     gerador3.get_tanque()))

    if gerador4.get_combustivel() < (20 * gerador4.get_tanque())/100:
        print("{} - {} / {} (ABASTECER)".format(gerador4.get_nome(),
                                                gerador4.get_combustivel(),
                                                gerador4.get_tanque()))
    else:
        print("{} - {} / {} ".format(gerador4.get_nome(),
                                     gerador4.get_combustivel(),
                                     gerador4.get_tanque()))
    exibir_menu()


def abastacer():
    nomeG = input("Informe o Nome do Gerador: ")
    quant = int(input("Quantidade de litros de combustível: "))
    if nomeG == gerador1.get_nome():
        if quant < gerador1.get_tanque():
            gerador1.abastecer_tanque(quant)
            print("Tanque foi abastecido com sucesso.")
            exibir_menu()
        else:
            print("Quantidade de combustível excede o tamanho do tanque.")
            exibir_menu()

    elif nomeG == gerador2.get_nome():
        if quant < gerador2.get_tanque():
            gerador2.abastecer_tanque(quant)
            print("Tanque foi abastecido com sucesso.")
            exibir_menu()
        else:
            print("Quantidade de combustível excede o tamanho do tanque.")
            exibir_menu()
    elif nomeG == gerador3.get_nome():
        if quant < gerador3.get_tanque():
            gerador3.abastecer_tanque(quant)
            print("Tanque foi abastecido com sucesso.")
            exibir_menu()
        else:
            print("Quantidade de combustível excede o tamanho do tanque.")
            exibir_menu()
    elif nomeG == gerador4.get_nome():
        if quant < gerador4.get_tanque():
            gerador4.abastecer_tanque(quant)
            print("Tanque foi abastecido com sucesso.")
            exibir_menu()
        else:
            print("Quantidade de combustível excede o tamanho do tanque.")
            exibir_menu()


def detalhes_gerador():
    nomeG = input("Informe o Nome do Gerador:")
    if nomeG == gerador4.get_nome():
        print("Nome: ", gerador1.get_nome())
        print("Potência: ", gerador1.get_potencia())
        print("Capacidade: ", gerador1.get_capacidade())
        print("Tanque: ", gerador1.get_combustivel())
        print("Status: ", gerador1.get_status())
        exibir_menu()
    elif nomeG == gerador2.get_nome():
        print("Nome: ", gerador2.get_nome())
        print("Potência: ", gerador2.get_potencia())
        print("Capacidade: ", gerador2.get_capacidade())
        print("Tanque: ", gerador2.get_combustivel())
        print("Status: ", gerador2.get_status())
        exibir_menu()
    elif nomeG == gerador3.get_nome():
        print("Nome: ", gerador3.get_nome())
        print("Potência: ", gerador3.get_potencia())
        print("Capacidade: ", gerador3.get_capacidade())
        print("Tanque: ", gerador3.get_combustivel())
        print("Status: ", gerador3.get_status())
        exibir_menu()
    elif nomeG == gerador4.get_nome():
        print("Nome: ", gerador4.get_nome())
        print("Potência: ", gerador4.get_potencia())
        print("Capacidade: ", gerador4.get_capacidade())
        print("Tanque: ", gerador4.get_combustivel())
        print("Status: ", gerador4.get_status())
        exibir_menu()


exibir_menu()
