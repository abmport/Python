def calcular_media(notas, nome):
    if nome in notas:
        media = sum(notas[nome]) / len(notas[nome])
        return media
    else:
        return 0