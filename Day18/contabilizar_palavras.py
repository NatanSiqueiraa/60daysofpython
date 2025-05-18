def contar_palavras(texto):
    """
    Contar palavras em uma string
    :param texto: String de entrada
    :return: numero de palavras
    :len(): contabiliza palavras em uma lista
    :split(): contabiliza itens em uma string 
    """
    palavras = texto.split()
    
    return len(palavras)

contar = input("Digite uma frase: ")
print(f"A frase possui:{contar_palavras(contar)} palavras ")
print()