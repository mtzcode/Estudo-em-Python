#Leia a temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
# A formula de conversão é: F= C*(9.0/5.0)+32, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius

temp_celsius = float(input("Informe a temperatura em Graus Celsius: "))
conversao_fahrenheit = temp_celsius * (9.0 / 5.0) + 32

print(f"Graus Celsius: {temp_celsius} ºC")
print(f"Graus em Fahrenheit: {conversao_fahrenheit} °F")
