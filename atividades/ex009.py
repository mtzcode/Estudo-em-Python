#Leia uma velocidade em km/h (quilometros por hora) e apresente-a convertida em m/s (metros por segundo). A formula de conversão é: M = K/3.6, sendo K a velocidade em km/h e M em m/s

velocidade = float(input("Informe velocidade em km/h:" ))
metros_segundos = velocidade / 3.6

print(f"Velocidade:{velocidade:.2f}")
print(f"Conversão em metros por segundo:{metros_segundos:.2f}")