# Leia a temperatura em graus Fahrenheit e apresente-a em graus Celsius.
# Fórmula: C = (F - 32) * 5/9

temp_fahrenheit = float(input("Informe a temperatura em graus Fahrenheit: "))
temp_celsius = (temp_fahrenheit - 32) * 5 / 9

print(f"Fahrenheit: {temp_fahrenheit:.2f} °F")
print(f"Celsius: {temp_celsius:.2f} °C")
