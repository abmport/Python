list = []
for i in range(10):
    list.append(int(input("Infortme o valor da posição {}: ".format(i))))

# Maior numero da lista
maximo = max(list)
print("Maior valor da lista:", maximo)
# Menor valor da lista
minimo = min(list)
print("Menor valor da lista:", minimo)
# Media dos valores da lista
media = sum(list)/len(list)
print("Media dos valores da lista: ", media)

# verificando qual valor e menor que a media
for i in list:
    if i < media:
        print("valores menores que a media da lista: ", i)
