#Leia a temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
# A formula de conversão é: C = (F - 32) * 5.0 / 9.0, sendo C a temperatura em Celsius e F a temperatura em Fahrenheit

temp_fahrenheit = float(input("Informe a temperatura em Graus Celsius: "))
conversao_celsius= (temp_fahrenheit - 32) * 5 / 9

print(f"Graus em Fahrenheit: {temp_fahrenheit} °F")
print(f"Graus em Celsius: {conversao_celsius} °C")