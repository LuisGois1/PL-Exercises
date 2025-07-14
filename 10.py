##Calcule o IMC (peso / altura²) a partir do peso e da altura.
peso = float(input("Insira seu Peso: "))
altura = float(input("Insira sua Altura (Ex: 1.75): "))
IMC = peso/(altura*altura) 
print(f"O seu IMC é: {IMC}")