# conte a quantidade de letras no texto e também a quantidade de letras repetidas.
#
frase = input("Digite a frase a ser contada: ")

contador = {}

for letra in frase.lower():
    if letra not in contador:
        contador[letra] = 1
    else:
        contador[letra] += 1

for k, v in contador.items():
    print("{}: {}".format(k, v))