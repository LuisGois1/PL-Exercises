#Verifique se um triângulo é equilátero, isósceles ou escaleno com base em seus lados.
lado1 = float(input("Insira o Valor do Primeiro Lado do Triângulo: "))
lado2 = float(input("Insira o Valor do Segundo Lado do Triângulo: "))
lado3 = float(input("Insira o Valor do Terceiro Lado do Triângulo: "))
if lado1 == lado2 and lado2 == lado3:
    print("Esse Triângulo é Equilátero")
elif lado1 == lado2 and lado2 != lado3 or lado2 == lado3 and lado3 != lado1 or lado3 == lado1 and lado1 != lado2: 
    print("Esse Triângulo é Isósceles")
elif lado1 != lado2 and lado2 != lado3:
    print("Esse Triângulo é Escaleno")