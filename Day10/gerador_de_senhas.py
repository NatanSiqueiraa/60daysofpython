import random
import string
#string fornece um conjunto de caracteres prontos
#random fornece funcoes para gerar números aleatorios
#como letra1s maiusculas, numeros e simbolos

def gerador_de_senhas(tamanho):
    comprimento = tamanho
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha=''
    
    while len(senha) < comprimento:
        senha += random.choice(caracteres)
        
    print(f"A senha gerada é: {senha}")
    
gerador_de_senhas(30)