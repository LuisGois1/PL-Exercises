# 3. Contador de Dígitos Sem String
# Peça ao usuário para digitar um número inteiro positivo. 
# Conte quantos dígitos ele possui, sem converter para string e sem usar listas.
while True:
    num_inteiro = int(input("Insira um Numero Inteiro Positivo:"))
    if num_inteiro >= 0:
         break
    else:
        print(f"O número {num_inteiro} é invalido. Insira um inteiro positivo!" )

contador = 0
ni = num_inteiro
if ni == 0:
        contador = 1
else:
    while ni > 0:
        ni = ni // 10
        contador +=1    
print(f"O Número {num_inteiro} contém {contador} dígito(s)!")
