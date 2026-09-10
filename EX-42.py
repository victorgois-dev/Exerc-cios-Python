matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

soma = 0
for linha in matriz:
    for elemento in linha:
        soma += elemento
print(f"A soma de todos os valores é: {soma}")