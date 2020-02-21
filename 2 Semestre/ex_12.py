'''
produtos = {"notbook": 2000.00,
            "monitor": 60.00,
            "mouse": 35.00,
            "teclado": 40.00,
            "gabinete": 70.00}
'''

produtos = {}

for x in range(5):
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o valor do produto: "))
    produtos[nome] = preco

for i in produtos:
    if produtos[i] > 50.00:
        print("O produto {} tem o valor de R${}".format(i, produtos[i]))
