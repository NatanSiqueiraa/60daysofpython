def fatorial(n):
    if n < 0:
        raise ValueError("O numero deve ser positivo")
    
    if n == 0 or n == 1:
        return 1
    
    return n * fatorial(n - 1)

fatorar = int(input("Digite um numero para fatorar ele: "))
print(fatorial(fatorar))