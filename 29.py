##Sequência de Fibonacci: Gerar os primeiros N termos da sequência de Fibonacci, onde N é um número fornecido pelo usuário. A sequência de Fibonacci começa com 0 e 1, e cada termo subsequente é a soma dos dois anteriores (0,1,1,2,3,5,8,...).
fibonnaci = int(input("Digite um Número e Será feita a Sequência de Fibbonnaci: "))
anterior = 0
proximo = 1
for ondascerebrais in range(fibonnaci):
   atual =  anterior + proximo
   anterior = proximo
   proximo = atual  
   print(atual)