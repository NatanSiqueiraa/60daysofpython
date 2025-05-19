def calcular_media_notas(notas):
    """
    Calculando media de notas a partir de uma lista de notas

    Args:
        notas (lista)
    
    Return:
    float media de notas
    """
    media = sum(notas) / len(notas)
    
    #round arredonda a média
    return round(media, 2)

print(calcular_media_notas([3, 3, 3, 3]))