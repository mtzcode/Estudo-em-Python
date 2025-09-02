# Leia uma velocidade em m/s e apresente-a em km/h.
# Fórmula: K = M * 3.6

velocidade_ms = float(input("Informe a velocidade em m/s: "))
velocidade_kmh = velocidade_ms * 3.6

print(f"Metros por segundo: {velocidade_ms:.2f} m/s")
print(f"Conversão: {velocidade_kmh:.2f} km/h")
