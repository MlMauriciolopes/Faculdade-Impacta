# # Exemplo1
# fruts = ["laranja", "maçã", "abacate", "limão", "banana"]
# for fruta in fruts:
#     print(fruta)

# # Exemplo
# valor = 0
# while valor != 9:
#     print(valor)
#     valor = valor -1

# contador = 1

# nota = [9,6,7,3,8,8,"oito", "A", "C"]

# soma = 0

# for in numeros:
#     soma = soma + n
# print('media', round(soma/total,4))

ref_arquivo = open("C:/Users/mlsil/Downloads/texto.txt","r")
linha = ref_arquivo.readline()
while linha:
    valores = linha.split()
    print(valores)
    linha = ref_arquivo.readline()

ref_arquivo.close()


try:
    nome_arquivo = input('Qual arquivo procura:')
    arquivo = open("C:/Users/mlsil/Downloads/texto.txt"'r+')
    linha = arquivo.readline()
    while linha:
        print(linha)
        linha = arquivo.readline()
except FileNotFoundError:
    arquivo = open(nome_arquivo, 'w+')
    arquivo.writelines(u'Arquivo criado pois nao existia')
arquivo.close()
