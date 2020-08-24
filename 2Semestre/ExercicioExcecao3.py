def inserir_nome(lista_nomes, nome):
    lista_nomes.append(nome)

def busca_nome(lista_nomes, indice):
    try:
        if indice >= len(lista_nomes):
            raise IndexError
    except IndexError:
        return "Indice inexistente!"
    else:
        return lista_nomes[indice]

lista_nomes = []
inserir_nome(lista_nomes, 'Paulo')
inserir_nome(lista_nomes, 'João')

nome = busca_nome(lista_nomes, 1)

print (nome)