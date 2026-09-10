import random

numero_secreto = random.randint(1, 20)
acertou = False

print("Tente adivinhar o número secreto!")

while not acertou:
    chute = int(input("Digite seu chute: "))

    if chute == numero_secreto:
        print("Parabéns! Você acertou!")
        acertou = True
    elif chute < numero_secreto:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")