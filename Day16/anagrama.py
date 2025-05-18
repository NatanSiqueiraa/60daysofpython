def anagrama(palavra1, palavra2):
    """
    Verrificar se duas palavras sao um anagrama ou nao
    :param palavra 1: Primeira palavra
    :param palavra 2: Segunda palavra
    :return: True se as palavras forem um anagrama
    """
    palavra1 = palavra1.replace(" ", "").lower()
    palavra2  = palavra2.replace(" ", "").lower()
    
    if sorted(palavra1) == sorted(palavra2):
        return f"Essas palavras são anagramas"
    return f"Essas palavras não são anagramas"

x = input("Digite a primeira palavra: ")
y = input("Digite a segunda palavra: ")
z = anagrama(x, y)

print(z)