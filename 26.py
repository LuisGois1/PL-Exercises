##Validação de Senha Simples: Pedir ao usuário para digitar uma senha. O programa deve continuar pedindo a senha até que a senha correta ("python123") seja digitada. Use um loop while.
senha = None
while senha != "python123":
    if senha:
        print("Senha Incorreta!")
    senha = input("Digite 'python123':") 
print("Acesso Concedido!")