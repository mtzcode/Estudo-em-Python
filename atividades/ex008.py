#Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A formula de conversão é: C = K - 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin

temp_kelvin = float(input("Digite e temperatura em Kelvin:"))
converte_celsius = temp_kelvin - 273.15

print(f"Temperatura em Kelvin:{temp_kelvin:.2f}°K")
print(f"Temperatura em Celsius:{converte_celsius:.2f}°C")