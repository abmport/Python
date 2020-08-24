# ABNER DE MELO PORTO - RA: 1800074
# JOSÉ ALVES DE OLIVEIRA - RA: 1902135

import ac02

desenv_maior = ["Marcílio dos Santos",
                "marcilio@email.com", 5000.00, "DESENVOLVEDOR"]
analista_maior = ["Abner de Melo Porto",
                  "abner@email.com", 2000.00, "ANALISTA"]
gerente_maior = ["José Alves de Oliveira",
                 "jose@email.com", 5500.00, "GERENTE"]
desenv_menor = ["Joaquim dos Santos",
                "joaquim@email.com", 2000.00, "DESENVOLVEDOR"]
analista_menor = ["Abner de Melo Porto", "abner@email.com", 550.00, "ANALISTA"]
gerente_menor = ["José Alves de Oliveira",
                 "jose@email.com", 2500.00, "GERENTE"]

try:
    salario = ac02.calculo_salario(desenv_maior)
    assert salario == 4000
    print("Salário Liquido DESENVOLVEDOR Correto,", salario)
except AssertionError:
    print("Salário Liquido DESENVOLVEDOR Incorreto")
    print(salario)

try:
    salario = ac02.calculo_salario(analista_maior)
    assert salario == 1500
    print("Salário Liquido ANALISTA Correto,", salario)
except AssertionError:
    print("Salário Liquido ANALISTA Incorreto")
    print("Salário esperado eh:", salario)

try:
    salario = ac02.calculo_salario(gerente_maior)
    assert salario == 3850
    print("Salário Liquido GERENTE Correto,", salario)
except AssertionError:
    print("Salário Liquido GERENTE Incorreto")
    print(salario)

try:
    salario = ac02.calculo_salario(desenv_menor)
    assert salario == 1800
    print("Salário Liquido DESENVOLVEDOR Correto,", salario)
except AssertionError:
    print("Salário Liquido DESENVOLVEDOR Incorreto")
    print("Salário esperado eh:", salario)

try:
    salario = ac02.calculo_salario(analista_menor)
    assert salario == 467.5
    print("Salário Liquido ANALISTA Correto,", salario)
except AssertionError:
    print("Salário Liquido ANALISTA Incorreto")
    print("Salário esperado eh:", salario)

try:
    salario = ac02.calculo_salario(gerente_menor)
    assert salario == 2000
    print("Salário Liquido GERENTE Correto,", salario)
except AssertionError:
    print("Salário Liquido GERENTE Incorreto")
    print("Salário esperado eh:", salario)
