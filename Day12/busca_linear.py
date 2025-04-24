def busca_linear(lista, numero_procurado):
    for i, numero in enumerate(lista):
        if numero == numero_procurado:
            return i
    return -1

lista = [1,2,3,4,5,6,7,8.9,10]
numero_procurado = 7

buscar_numero = busca_linear(lista, numero_procurado)

if buscar_numero != 1:
    print(f"O numero se encontra no indice: {buscar_numero}")
else:
    print("numero nao encontrado")

