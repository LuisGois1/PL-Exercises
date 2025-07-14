##Jogo de Adivinhação: Gerar um número aleatório entre 1 e 100. O usuário deve tentar adivinhar o número. O programa deve dizer se o palpite é muito alto, muito baixo ou correto, e contar quantas tentativas foram necessárias.
import random
num = None
contador = 0
aleatorio = random.randint(1, 100)
while num != aleatorio:
    contador += 1 
    num = int(input("Advinhe um Número Entre 1 e 100:"))
    if num > aleatorio:
        print(f"O Número {num} Alto demais!")
    elif num < aleatorio:
        print(f"O Número {num} é Baixo demais!")    
print(f"O Número {num} está Correto! Você Advinhou em {contador} tentativas!")
