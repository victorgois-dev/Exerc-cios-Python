estoque = {}

print("=== Cadastro de Medicamentos ===")
for i in range(5):
    nome = input(f"Nome do medicamento {i+1}: ")
    qtd = int(input(f"Quantidade do medicamento {i+1}: "))
    estoque[nome] = qtd

busca = input("\nDigite o nome do medicamento para consultar: ")

if busca in estoque:
    print(f"Quantidade em estoque de {busca}: {estoque[busca]}")
else:
    print("Medicamento não encontrado no sistema.")