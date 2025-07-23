# 6. Fatorial com Verificação
# Solicite um número e:
# - Verifique se ele é inteiro e não-negativo
# - Calcule seu fatorial com while
# - Se o número for maior que 20, mostre uma mensagem de aviso antes de calcular (por risco de overflow)

while True:
    num = int(input("Digite um número inteiro não-negativo para calcular o fatorial: "))
    try:
        if num < 0:
            print("O número não pode ser negativo. Tente novamente!\n")
        else:
            break
    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros!\n")

if num > 20:
    print("Aviso: O número é muito grande. O fatorial pode ultrapassar o limite de inteiros.")

fatorial = 1
contador = num

while contador > 1:
    fatorial *= contador
    contador -= 1

print(f"O Fatorial de {num} é {fatorial}.")
