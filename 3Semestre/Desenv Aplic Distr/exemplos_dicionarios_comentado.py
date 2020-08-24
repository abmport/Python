dic = {
    "integrantes": {
        "beatles":['ringo','john','paul','george','pete'],
        "the_fellowship":['gandolfo',
                          'aragorn','gimli',
                          'legolas', 'boromir',
                          'frodo', 'sam',
                          'hobbit 3', 'hobbit 4'],
        "The_Vindicators":  ('Vance Maximus', 'Alan Rails',
                             'Crocubot',
                             'Million Ants', 'Morty Smith',
                             'Rick Sanchez', 'Lady Katana',
                             'Calypso', 'Diablo Verde'),
        'Alunos_distraidos_nesse_momento': [],
        },
    "jogos" : [
         {"nome":"CS go", "empresa":"valve", "estilo": "FPS"},
         {"nome":"PLANESCAPE:torment", "empresa":"Bioware",
           "estilo": "Jogo mais bem escrito da história"},
         {"nome":"The Witcher", "empresa":"CD Project Red",
           "estilo": "Open World RPG"},
        ],
    }

from pprint import pprint
#1; print(dic["jogos"][2]["nome"] == "The Witcher")
#2; print("CS go" == dic["jogos"][0])
#3; print("FPS" in dic["jogos"]["CS go"])
#tentei acessar a "posicao" "CS go" da lista dic['jogos'], mas
#as unicas "posicoes" que a lista tem sao inteiros dic['jogos'][0]
#ou slices dic['jogos'][0:2] (pega uma faixa de posicoes)

#4; print("Rick Sanchez" in dic.integrantes.The_Vindicators)
#dá pau. Essa sintaxe seria para acessar um atributo de um objeto.
#em python, as chaves de um dicionário não sao atributos do objeto correspondente,
# fazer dic["integrantes"] não é  mesmo que dic.integrantes
# print("Rick Sanchez" in dic["integrantes"]["The_Vindicators"])
#essa versao acima funciona
#curiosidade: em javascript funcionaria

#5; print(dic["integrantes"]["beatles"][3] == "paul")
#['ringo', 'john', 'paul', 'george', 'pete']
#pprint(dic['integrantes']['beatles'][3]) imprime o elemento de indice 3
#que é george

#6; print("valve" in dic["jogos"]["CS go"])
#vide item 3

#7; print("empresa" in dic["jogos"]["CS go"])
#vide item 3

#8; print("legolas" in dic["integrantes"]["the_fellowship"])
#true, a string "legolas" realmente é elemento dessa lista


#9; print("merlin" in dic["integrantes"]["The_Vindicators"])
#false, a string "merlin" não é elemento dessa


#10; print("Thor" in dic["filmes"]["Avengers"])
#ordem de execução:
# 1) consulto a chave "filmes" do dic (já deu pau!)
# Mas se nao tivesse dado pau...
# 2) consulto a chave avengers no "dicionário" dic["filmes"]
# (estamos imaginando que teria que ser um dicionário)
# 3) No objeto obtido no passo 2 (vamos chamar de obj), verifica
# se Thor in obj
# 4) Imprime o resultado do passo 3
# KeyError: 'filmes' -> voce quis consultar
# em algum dicionario a chave filmes, mas ele nao tinha essa chave

#11; print("Open World RPG" == dic["jogos"][1]["empresa"])
# consulta deu certo, mas a string consultada nao é a string desejada

#12; print(dic["jogos"][0]["estilo"] == "FPS")

#>>> pprint(dic['jogos'])
#[{'empresa': 'valve', 'estilo': 'FPS', 'nome': 'CS go'},
# {'empresa': 'Bioware',
#  'estilo': 'Jogo mais bem escrito da história',
#  'nome': 'PLANESCAPE:torment'},
# {'empresa': 'CD Project Red',
#  'estilo': 'Open World RPG',
#  'nome': 'The Witcher'}]
#>>> pprint(type(dic['jogos']))
#<class 'list'>
#>>> pprint(len(dic['jogos']))
#3
#>>> lista=[100,200,300]
#>>> lista[0]
#100
#>>> lista[1]
#200
#>>> lista[2]
#300
#>>> lista[3]

#13; print(dic["jogos"]["Bioware"] == "PLANESCAPE:torment")
#dic jogos é uma lista
#listas nao tem a "posicao" "Bioware", só 0,1,2,3...
#TypeError: list indices must be integers or slices, not str
#nao posso colocar a string "Bioware" na frente de uma lista
#e torcer pra ela achar um elemento

#14; print("pete" in dic["integrantes"]["beatles"])


#15; print(dic["integrantes"]["the_fellowship"][2] == "gimli")
# ['gandolfo', 'aragorn','gimli', 'legolas', 'boromir', 'frodo', 'sam', 'hobbit 3', 'hobbit 4']
#   pos 0         pos 1   pos 2    pos 3
# quando eu acessso a posicao 2 da lista dic["integrantes"]["the_fellowship"], realmente é "gimli"

16; print("CD Project Red" in dic["jogos"][2])
17; print("empresa" in dic["jogos"][2])
#>>> dic['jogos'][2]
#{'nome': 'The Witcher', 'empresa': 'CD Project Red', 'estilo': 'Open World RPG'}
# Mas o que é que o "in" faz no dicionário??
# a in dic -> true se a é chave, false se não é chave.
# "CD Project Red" não é chave. É valor, mas o python nao liga, e retorna False
# "empresa" é chave. retorna true
# "abacaxi" nao é chave nem valor. Entao, nao é chave. Entao retorna False
# em Estruturas de Dados, voces vao ver que a consulta da chave é muito rápida
# e a do valor, nao. Por isso ele faz assim



18; print(dic[dic] + dic[dic[dic]])


