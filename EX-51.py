temperaturas = []

for i in range(5):
    temp = float(input(f"Digite a temperatura do dia {i+1}: "))
    temperaturas.append(temp)

media = sum(temperaturas) / len(temperaturas)

print(f"\nTemperaturas cadastradas: {temperaturas}")
print(f"Média das temperaturas: {media:.2f}°C")

if 18 <= media <= 28:
    print("A média está DENTRO da faixa ideal de cultivo.")
else:
    print("A média está FORA da faixa ideal de cultivo.")