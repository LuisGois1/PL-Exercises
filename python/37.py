# 7. Classificador de Dígitos
# Peça ao usuário um número inteiro. Para cada dígito:
# - Diga se é par ou ímpar
# - E se é maior que 5 ou não
# Exemplo: 238 → 2 = par/≤5, 3 = ímpar/≤5, 8 = par/>5
while True:
    try:
        entrada = input("Insira um número inteiro: ")
        int(entrada)
        break    
    except ValueError:
        print("Entrada inválida. Insira apenas números inteiros!\n")

for caractere in entrada:
    if caractere == "-":
        continue

    digito = int(caractere)

    if digito % 2 == 0:
        imp_par = "Par"
    else:
        imp_par = "Ímpar"

    if digito > 5:
        comparacao = "> 5"
    else:
        comparacao = "<= 5"

    print(f"{digito} = {imp_par}/{comparacao}")

