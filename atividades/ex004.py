# Leia um número real e imprima o resultado do quadrado desse número.

num = float(input("Digite um número real (com casas decimais): "))
resultado_quadrado = num ** 2  # mais comum usar ** para potência

print(f"O resultado de {num} elevado ao quadrado é: {resultado_quadrado:.2f}")
