# 4. Verificador de Palíndromo (com frase completa)
# Peça ao usuário uma frase e verifique se ela é um palíndromo.
# Ignore espaços, acentos e letras maiúsculas.
import unicodedata

eh_palindromo = input("Digite uma Frase e Você Descobrirá se é Palíndromo ou Não: ")

frase_limpa = ''

for caracteres in eh_palindromo:
    caracteres_sem_acentos = unicodedata.normalize('NFD', caracteres)
    
    for letra in caracteres_sem_acentos:
        if unicodedata.category(letra)  != 'Mn' and letra.isalnum():
            frase_limpa += letra.lower()

if frase_limpa == frase_limpa[::-1]:
    print("A frase é um Palíndromo!")
else:
    print("A Frase Não é um Palíndromo!")

#Anotações Pertinentes:
# A função normalize padroniza como os caracteres são representados em Unicode.
# ex:"á" um caractere composto virará "a" e "´" , os transformando em caracteres separados.
# NFD = Normal Form Decomposed (Faz parte da função normalize)
# 'Mn' = Mark, Nonspacing
# A ideia é: se for 'Mn', é acento, então será removido.