##Tabuada: Gerar a tabuada de um número escolhido pelo usuário (por exemplo, 7), imprimindo de 1 a 10. Use um loop for.
num = float(input("Insira um Número e a Tabuada do Mesmo Será Feita: "))
for count in range(1,11):
    product = num * count
    print(f"{num} x {count} = {"{:.0f}".format(product)}")