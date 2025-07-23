# # 5. Contador de Vogais e Consoantes
# Peça ao usuário uma frase e conte:
# - Quantas letras (ignorando números e símbolos)
# - Quantas são vogais
# - Quantas são consoantes
import unicodedata
frase = input("Digite Uma Frase: ")
vogais = "aeiou"
letras = 0
qtd_vogais = 0
qtd_consoantes = 0

for caracteres in frase:
    caracteres_sem_acentos = unicodedata.normalize('NFD', caracteres)
    for c in caracteres_sem_acentos:
        if unicodedata.category(c) != 'Mn' and c.isalpha():
            letras += 1
            if c.lower() in vogais:
                qtd_vogais += 1
            else:
                qtd_consoantes += 1

print(f"A Frase tem um Total de {letras} Letras, {qtd_vogais} Vogais e {qtd_consoantes} Consoantes.")    