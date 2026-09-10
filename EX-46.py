matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

soma_diagonal = 0
for i in range(3):
    soma_diagonal += matriz[i][i]

print(f"Soma dos elementos da diagonal principal: {soma_diagonal}")