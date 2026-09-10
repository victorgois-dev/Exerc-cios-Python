matriz = [
    [1200, 850, 1100],
    [950,  700, 1300],
    [1050, 600, 900]
]

menor = matriz[0][0]

for linha in matriz:
    for elemento in linha:
        if elemento < menor:
            menor = elemento

print(f"O menor custo registrado é: {menor}")