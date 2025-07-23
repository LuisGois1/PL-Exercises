# 10. Contador de Letras por Tipo
# Peça uma frase ao usuário e diga:
# - Quantas letras maiúsculas
# - Quantas minúsculas
# - Quantos números
# - Quantos caracteres especiais (pontuação, símbolos)
# Use apenas ifs e loops — sem bibliotecas externas como re.
frase = input("Digite uma frase: ")

maiusculas = 0
minusculas = 0
numeros = 0
especiais = 0

for caractere in frase:
    if caractere == " ":
        continue

    if 'A' <= caractere <= 'Z':
        maiusculas += 1
    elif 'a' <= caractere <= 'z':
        minusculas += 1
    elif caractere.isdigit():
        numeros += 1
    else:
        especiais += 1

print(f"A frase tem {maiusculas} letras maiúsculas, {minusculas} letras minúsculas, {numeros} números e {especiais} caracteres especiais!")
