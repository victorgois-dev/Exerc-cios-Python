matriz = [
    [12, 45, 23],
    [67, 89, 34],
    [10, 56, 78]
]
maior = matriz[0][0]

for linha in matriz:
    for elemento in linha:
        if elemento > maior:
            maior = elemento

print(f"O maior valor na matriz é: {maior}")