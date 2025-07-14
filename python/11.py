##Leia um número e diga se ele é positivo, negativo ou zero.
num1 = float(input("Digite um número: "))
if num1 == 0:
    print("O Número é Igual a Zero! ")
elif num1 < 0:
    print(f"O Número {num1} é Menor que zero! ") 
else:
    print(f"O Número {num1} é Maior que Zero! ")