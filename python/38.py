# 8. Primo Dentro do Intervalo
# Peça dois números e exiba quantos primos existem entre eles, inclusive.
# Evite usar funções prontas; use for com verificação de divisores.
while True:
    try:
        inicio = int(input("Digite o Número Inicial do Intervalo: "))
        fim = int(input("Digite o Número Final do intervalo: "))
        break
    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros!\n")

if inicio > fim:
    inicio, fim = fim, inicio

contador = 0

for num in range(inicio, fim + 1):
    if num < 2:
        continue
    eh_primo = True
    for divisor in range(2, num):
        if num % divisor == 0:
            eh_primo = False
            break
    if eh_primo:
        contador += 1

print(f"Existem {contador} Números Primos entre {inicio} e {fim}!")
