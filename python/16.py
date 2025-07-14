##Verifique se um ano é bissexto.
ano = int(input("Escolha um ano e Você Saberá se é Bissexto:"))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f"O ano de {ano} é Bissexto")
else:
    print(f"O ano de {ano} Não é Bissexto")     