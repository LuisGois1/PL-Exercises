##Receba um número e verifique se ele está entre 1 e 100.
intervalo = float(input("Insira Um Número e Você Saberá se Ele Está entre 1 e 100: "))
if intervalo <= 100 and intervalo >= 1:
    print(f"O Número {intervalo} está dentro do Intervalo!")
else:
    print(f"O Número {intervalo} Não está dentro do Intervalo") 