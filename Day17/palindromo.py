def eh_palindromo(texto):
    """

    Verifica se um numero, texto ou palavra eh um palindromo
    :param texto: Palavra, texto ou numero
    :return: Uma mensagem se eh um palindromo ou nao
    """
    texto = str(texto).replace(" ", "").lower()
    
    if texto == texto[::-1]:
        return f"{texto} eh um palindromo"
    return f"{texto} não eh um palindromo"

text = input("Digite um texto para descobrir se ele é um palindromo: ")
print(eh_palindromo(text))
    