##Peça três números e diga qual é o maior e qual é o menor.
num1 = float(input("Digite o Primeiro Número: "))
num2 =  float(input("Digite o Segundo Número: "))
num3 = float(input("Digite o Terceiro Número: "))
if num1 > num2 and num2 > num3: 
    print(f"O Número {num1} é o Maior e o Número {num3} é o Menor!") 
elif num1 > num2 and num3 > num2 and num1 > num3:
    print(f"O Númeor {num1} é o Maior e o Número {num2} é o Menor!")
elif num2 > num3 and num3 > num1:
    print(f"O Número {num2} é o Maior e o Número {num1} é o Menor!")
elif num2 > num3 and num1 > num3 and num2 > num1:
    print(f"O Número {num2} é o Maior e o Número {num3} é o Menor!")
elif num3 > num2 and num2 > num1:
    print(f"O Número {num3} é o Maior e o Número {num1} é o Menor!")
elif num1 > num2 and num3 > num2 and num3 > num1:
    print(f"O Número {num3} é o Maior e o Número {num2} é o Menor!")
elif num1 > num2 and num2 == num3:
    print(f"O Número {num1} é o Maior e os Outros Dois são Idênticos")
elif num2 > num1 and num1 == num3:
     print(f"O Número {num2} é o Maior e os Outros Dois são Idênticos")
elif num3 > num1 and num1 == num2:
     print(f"O Número {num3} é o Maior e os Outros Dois são Idênticos")
elif num1 == num2 and num2 == num3:
    print("Os Números são Idênticos")

    #Método Decente
    # a = 50
    # b = 11
    # c = 20
    # maior_numero = a
    # menor_numero = a
    # for num in [b,c]:
    #   if num < menor_numero:
    #     menor_numero = num
    # if num > maior_numero:
    #     maior_numero = num
    # print(menor_numero, maior_numero) 