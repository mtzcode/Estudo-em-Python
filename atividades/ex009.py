# Leia uma velocidade em km/h e apresente-a em m/s.
# Fórmula: M = K / 3.6

velocidade_kmh = float(input("Informe a velocidade em km/h: "))
velocidade_ms = velocidade_kmh / 3.6

print(f"Velocidade: {velocidade_kmh:.2f} km/h")
print(f"Conversão: {velocidade_ms:.2f} m/s")
