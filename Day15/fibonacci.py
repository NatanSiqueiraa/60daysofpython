fibonacci = [0, 1] # a sequ~encia sempre começa com 0 e 1

for i in range(8): # repete 8 vezes
    proximo_numero = fibonacci[-1] + fibonacci[-2] # soma 1 + 0 
    fibonacci.append(proximo_numero)
    
print(fibonacci)