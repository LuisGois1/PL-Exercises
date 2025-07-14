##Fatorial: Calcular o fatorial de um número fornecido pelo usuário. O fatorial de um número inteiro positivo n (representado por n!) é o produto de todos os inteiros positivos menores ou iguais a n. Ex: 5!=5∗4∗3∗2∗1=120.
num = int(input("Digite um Número e Será Calculado o Seu Fatorial: "))
conta = num
while num > 1:
    num -= 1
    conta = conta * num 
print(conta)