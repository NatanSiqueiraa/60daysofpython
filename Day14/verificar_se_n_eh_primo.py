num = int(input("Digit um número para verificar se ele é primo: "))

primo = True

if primo <= 0:
    primo = False
    
for i in range(2, int(num ** 0.5) + 1):
    if i == 0:
        break
    
if primo:
    print(f"{num} é um número primo")
else:
    print(f"{num}não é um número primo")
    
