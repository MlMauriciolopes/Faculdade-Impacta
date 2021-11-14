# Execução final (entregue)
def adicao(val1, val2):
    return val1 + val2

def subtracao(val1, val2):
    return val1 - val2

def multiplicacao(val1, val2):
    return val1 * val2

def divisao(val1, val2):
    return val1 // val2

print("Selecione o número da operação desejada: \n ")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("\nDigite a sua opção (1/2/3/4): "))

if opcao <= 0 or opcao > 4:
    print("\nOpção inválida!\n")

val1 = int(input("\nDigite o primeiro número: "))
val2 = int(input("\nDigite o segundo número: "))

if opcao == 1:
    print(val1, "+",  val2, "=", adicao(val1, val2))

elif opcao == 2:
    print(val1, "-",  val2, "=", subtracao(val1, val2))

elif opcao == 3:
    print(val1, "*",  val2, "=", multiplicacao(val1, val2))

elif opcao == 4:
    print(val1, "/",  val2, "=", divisao(val1, val2))