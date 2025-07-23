# Validador de Números Positivos
# Peça que o usuário digite 10 números. Se algum número for negativo, peça outro no lugar (não conte esse). No final, informe:
# Quantos eram pares
# Quantos eram ímpares
# Quantos eram múltiplos de 5
numerosPares = 0
numerosImpares = 0
multiplosDeCinco = 0
contador = 0
while contador < 10:
   num = float(input("Digite 10 números Positivos (1 por linha): "))
   if num < 0:
      print("Número não aceito, digite apenas positivos. ")
      continue
   if num % 2 == 0:
      numerosPares += 1
   else:   
      numerosImpares += 1
   if num % 5 == 0:
      multiplosDeCinco += 1  
   contador += 1 
print(f"Você Inseriu {numerosPares} Números Pares.")
print(f"Você Inseriu {numerosImpares} Números Ímpares")   
print(f"Você Inseriu {multiplosDeCinco} Números Múltiplos de Cinco")
   
