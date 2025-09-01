# Leia uma velocidade em m/s (metro por segundo) e apresente-a convertida em km/h (quilometro por hora). A formula de conversão é: K = M * 3.6, sendo K a velocidade em km/h e M em m/s

metros_segundos = float(input("Informe metros_segundos:"))
velocidade = metros_segundos * 3.6

print(f"Metros por segundo:{metros_segundos:.2f}")
print(f"Conversão quilometro por hora:{velocidade:.2f}")
