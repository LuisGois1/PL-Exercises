# 2. Soma de Múltiplos com Intervalo Dinâmico
# Solicite dois números inteiros (início e fim). Some todos os múltiplos de 3 ou 5 entre eles (inclusive os limites). 
# Valide para que o número de início seja menor que o de fim.
inicio = 1
fim = 0
soma_total = 0
while inicio > fim:
    inicio = int(input("Insira Um Número Inteiro Inicial (Deve ser Menor que o Final): "))
    fim = int(input("Agora Insira o Número Inteiro Final (Deve ser Maior que o Inicial): "))
    if inicio > fim:
        print("O Número Inicial é Menor que o Final!")

for numero_atual_do_loop in range(inicio, fim +1):
    if numero_atual_do_loop % 3 == 0 or numero_atual_do_loop % 5 == 0:
        soma_total += numero_atual_do_loop
print(f"A Soma de Todos os Múltiplos entre 3 ou 5 é igual a: {soma_total}!")    
