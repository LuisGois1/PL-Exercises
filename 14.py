##Receba dois números e informe qual é o maior.
num1 = float(input("Digite um Número: "))
num2 = float(input("Digite outro Número: "))
if num1 > num2:
    print(f"O número {num1} é Maior que o Número {num2}!")
elif num1 == num2:
    print(f"Os Números são Idênticos!")
else:
    print(f"O número {num2} é Maior que o Número {num1}!")