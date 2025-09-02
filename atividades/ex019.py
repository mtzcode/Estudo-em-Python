# 19) Soma do sucessor do triplo com o antecessor do dobro
num = int(input("Digite um número inteiro: "))

sucessor_triplo = (num * 3) + 1
antecessor_dobro = (num * 2) - 1

resultado = sucessor_triplo + antecessor_dobro

print(f"Para n = {num}, sucessor do triplo = {sucessor_triplo}, antecessor do dobro = {antecessor_dobro}")
print(f"Resultado da soma = {resultado}")
