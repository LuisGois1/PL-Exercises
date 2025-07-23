# 9. Sequência Inversa com Condição
# Peça ao usuário para digitar números até que ele digite 0.
# Depois, imprima os números digitados na ordem inversa, mas apenas os ímpares.
numeros = []
while True:
    try:
        entrada = int(input("Digite um número (0 para parar): "))
        if entrada == 0 and len(numeros) == 0:
            print("Digite ao Menos um Número Diferente de 0 Antes de Finalizar!\n")
            continue
        if entrada == 0:
            break
        numeros.append(entrada)
    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros!\n")

print(f"Números ímpares em ordem inversa:")
for num in reversed(numeros):
    if num % 2 != 0:
        print(num)

