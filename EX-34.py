notas = {
    "Ana": 8.5,
    "João": 7.0,
    "Maria": 9.2
}

nome = input("Digite o nome do aluno: ")

if nome in notas:
    print(f"A nota de {nome} é: {notas[nome]}")
else:
    print("Aluno não encontrado.")