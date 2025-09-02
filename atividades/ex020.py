#Leia o salario de um funcionario. Calcule e imprima o valor do novo salario, sabendo que ele recebeu um aumento de 25%

# Calcular aumento de salário

salario = float(input("Digite o salário atual: R$ "))
percentual = float(input("Digite o percentual de aumento (%): "))

aumento = salario * (percentual / 100)
novo_salario = salario + aumento

print(f"O aumento será de R$ {aumento:.2f}")
print(f"O novo salário será de R$ {novo_salario:.2f}")
