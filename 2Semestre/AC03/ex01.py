# Atividade Contínua 03
# Abner de Melo Porto
# Vinicius Tertuliano
# Laura Tazue
# Tratativas Pendentes: ValueError - Gerador que não existe
# Combustivel < 50 nao liga -
# Os geradores só liga se o G1 estiver ligado

import sys
import gerador


def buscar_gerador(nome):
    if nome == "G1":
        nome = gerador.Gerador("G1", "100", "5000", "500")
    if nome == "G2":
        nome = gerador.Gerador("G2", "80", "4000", "400")
    if nome == "G3":
        nome = gerador.Gerador("G3", "70", "3000", "350")
    if nome == "G4":
        nome = gerador.Gerador("G4", "60", "2000", "300")
    return nome


def exibir_menu():
    print("1 - Acionamento manual de gerador")
    print("2 - Status dos geradores")
    print("3 - Status dos tanques de combustível")
    print("4 - Abastecer tanque de combustível")
    print("5 - Detalhes do gerador")
    print("6 - Sair")
    opcao_menu = int(input("Escolha uma opção: "))
    if opcao_menu <= 6 and opcao_menu >= 1:
        if opcao_menu == 1:
            acionamento_gerador()
        if opcao_menu == 2:
            return status_gerador(opcao_menu)
        if opcao_menu == 3:
            return status_tanque(opcao_menu)
        if opcao_menu == 4:
            return abastacer(opcao_menu)
        if opcao_menu == 5:
            return detalhes_gerador()
        if opcao_menu == 6:
            return print("Encerrado com exito"), sys.exit
    else:
        return print("Opção Incorreta, digite novamente!"), exibir_menu()


def acionamento_gerador():
    nomeG = input("Informe o Nome do Gerador: ")
    if buscar_gerador(nomeG).get_status:
        print(nomeG, "está Desligado. Deseja Ligar? \n 1 - Sim \n 2 - Não")
        op = int(input())
        if op == 1:
            buscar_gerador(nomeG).ligar_gerador()
            print(buscar_gerador(nomeG).get_nome(),
                  " foi ligado com sucesso. ")
            exibir_menu()
        elif op == 2:
            exibir_menu()
    else:
        print(nomeG, "está Ligado. Deseja Desligar? \n 1 - Sim \n 2 - Não")
        op = int(input())
        if op == 1:
            buscar_gerador(nomeG).desligar_gerador()
            print(buscar_gerador(nomeG).get_nome(),
                  " foi desligado com sucesso. ")
            exibir_menu()
        elif op == 2:
            exibir_menu()


def status_gerador(opcao_menu):
    '''
        Status dos Geradores
        G1 - Ligado
        G2 - Ligado
        G3 - Desligado
        G4 – Ligado
    '''
    return print(opcao_menu, "entrou 2")


def status_tanque(self):
    print("Status dos Tanques:")
    '''
        40/500 litros (ABASTECER)
        250/400 litros
        30/400 litros (ABSTECER)
        850/850 litros
    '''
    return print("entrou 3")


def abastacer(opcao_menu):
    return print(opcao_menu, "entrou 4")


def detalhes_gerador():
    nomeG = input("Informe o Nome do Gerador:")
    print("Nome:", buscar_gerador(nomeG).get_nome())
    print("Potência:", buscar_gerador(nomeG).get_potencia())
    print("Capacidade:", buscar_gerador(nomeG).get_capacidade())
    print("Tanque:", buscar_gerador(nomeG).get_tanque())
    print("Status:", buscar_gerador(nomeG).get_status())
    exibir_menu()


exibir_menu()
