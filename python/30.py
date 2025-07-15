##Média de Notas (com parada): Receber notas do usuário e calcular a média. O usuário pode digitar '-1' para parar de inserir notas. Use um loop while e tratamento para divisão por zero.
soma_notas = 0.0 
quantidade = 0      
while True:
        try:
            entrada = float(input("Digite uma nota (ou -1 para encerrar): "))
        except ValueError:
            print("Valor inválido! Tente novamente.\n")
            continue
        if entrada == -1:
            break
        soma_notas += entrada
        quantidade += 1
if quantidade != 0:        
    media = soma_notas / quantidade
    print(f"\nForam inseridas {quantidade} notas.")
    print(f"Média das notas: {media:.2f}") 
else:
    print("\nNenhuma nota foi inserida! Média não pode ser calculada.")