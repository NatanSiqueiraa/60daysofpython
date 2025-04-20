def contador_personalizado():
    try:
        limite = int(input("Digite o limite do contador: "))
        limite = limite + 1
        for i in range(limite):
            print(i)
            if i == limite:
              print("Você atingiu o limite")
              break
    except ValueError:
        print("Entrada ínvalida. Por favor insira um valor inteiro")
        
        
contador_personalizado()
        
           
        