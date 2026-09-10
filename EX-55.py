disciplinas = ("Matemática", "Português")

estudantes = {}
qtd = int(input("Quantos estudantes deseja cadastrar? "))

for _ in range(qtd):
    nome = input("\nNome do estudante: ")
    nota_mat = float(input("Nota de Matemática: "))
    nota_port = float(input("Nota de Português: "))
    estudantes[nome] = [nota_mat, nota_port]

print("\n--- Resultados ---")
print(f"Disciplinas cadastradas: {disciplinas}")

for nome, notas in estudantes.items():
    media = (notas[0] + notas[1]) / 2
    situacao = "Aprovado" if media >= 7.0 else "Reprovado"
    print(f"Aluno: {nome} | Média: {media:.2f} | Situação: {situacao}")