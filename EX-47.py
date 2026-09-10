matriz = [
    [-5, 12,  0],
    [ 8, -3, 15],
    [-1,  4, -9]
]
positivos = 0
for linha in matriz:
    for valor in linha:
        if valor > 0:
            positivos += 1
print(f"Quantidade de valores positivos: {positivos}")