def transpor_matriz(matriz):
    """
    Gerar uma matriz transposta de 3x3
    Substitui colunas horizontais por verticais
    
    arg: Matriz que sao lista de 3 números na horizontal e vertical
    return: Matriz transposta
    raise: Value error se a matriz nao for 3x3

    """
    if len(matriz) != 3 or not all(len(linha) == 3 for linha in matriz):
        raise ValueError("A matriz não tem 3x3")
    
    
    transposta = [[matriz[j][i] for j in range(3)] for i in range(3)]
    
    return transposta

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for linha in transpor_matriz(matriz):
    print(linha)


    