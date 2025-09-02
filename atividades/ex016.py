#Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente em dólares

moeda_real = float(input("Informe o valor em Real(BR): R$"))
cotacao_dolar = float(input("Informe a cotação do Dólar atual: U$"))
convercao_dolar = moeda_real / cotacao_dolar

print(f"Valor em Real informado: R${moeda_real:.2f}")
print(f"Cotação do Dólar: U${cotacao_dolar:.2f}")
print(f"Conversão em Dólar: U${convercao_dolar:.2f}")
