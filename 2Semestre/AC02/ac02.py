# ABNER DE MELO PORTO - RA: 1800074
# JOSÉ ALVES DE OLIVEIRA - RA: 1902135


def calculo_salario(lista):
    for i in lista:
        if i == 'DESENVOLVEDOR':
            if lista[2] >= 3000:
                desconto = lista[2]*0.2
            else:
                desconto = lista[2]*0.1
        if i == 'ANALISTA':
            if lista[2] >= 2000:
                desconto = lista[2]*0.25
            else:
                desconto = lista[2]*0.15
        if i == 'GERENTE':
            if lista[2] >= 5000:
                desconto = lista[2]*0.30
            else:
                desconto = lista[2]*0.20
    return lista[2]-desconto
