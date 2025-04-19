def pode_dirigir(idade):
    if idade >= 18:
        return print("Você pode dirigir")
    else:
        return print("Você não pode dirigir")
    
input_user = int(input("Digite a idade do usuário para saber se ele pode dirigir: "))
try:
    print(pode_dirigir(input_user))
except ValueError:
    print("digite um valor válido")
    