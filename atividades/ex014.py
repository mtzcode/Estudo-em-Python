# Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três lidos.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
soma_quadrados = (num1 ** 2) + (num2 ** 2) + (num3 ** 2)

print(
    f"A soma dos quadrados de {num1:.2f}, {num2:.2f} e {num3:.2f} é: {soma_quadrados:.2f}")
