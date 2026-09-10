import random

numero_sorteado = random.randint(1, 10)
chute = int(input("Adivinhe um número entre 1 e 10: "))

if chute == numero_sorteado:
    print("Parabéns, você acertou!")
else:
    print(f"Que pena, você errou! O número era {numero_sorteado}.")