# A partir dos conhecimento em sala de aula crie uma calculadora. Ela deverá receber dois valores. Após isso executar os metodos:
# soma
# sub
# multiplicacao
# divisao
# Lembre-se na divisão testar o zero.
# exemplo de como chamar a classe:
# class MyClass:
#   x = 5

# p1 = MyClass()
# print(p1.x)

# def soma(valor1, valor2):
#     return valor1 + valor2

# def subtracao(valor1, valor2):
#     return valor1 - valor2

# def multiplicacao(valor1, valor2):
#     return valor1 * valor2

# def divisao(valor1, valor2):
#     return valor1 / valor2

# def calculadora(valor1, valor2):
#     valor1 = float(input('Digite o primeiro valor: '))
#     valor2 = float(input('Digite o segundo valor: '))

# print(soma)
# print(subtracao)
# print(multiplicacao)
# print(divisao)

def calculadora():
    valor1 = float(input('Digite um valor: '))
    valor2 = float(input('Digite o segundo valor: '))

    soma = valor1 + valor2
    subtracao = valor1 - valor2
    multiplicacao = valor1 * valor2
    divisao = valor1 / valor2

    if valor1 + valor2:
        print(soma)
    elif valor1 - valor2:
        print(subtracao)
    elif valor1 * valor2:
        print(multiplicacao)
    elif valor1 / valor2:
        print(divisao)
    else: 
        print('Valor inválido')

def calculadora(valor1,valor2):
    soma = valor1 + valor2 
    print(soma)

# def calculadora():
#     valor1 = float(input('Digite um valor: '))
#     valor2 = float(input('Digite o segundo valor: '))

# def calculadora(valor1, valor2):
#     soma = valor1 + valor2
#     return soma