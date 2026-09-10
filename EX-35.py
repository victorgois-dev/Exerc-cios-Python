produtos = {
    "Caderno": 10,
    "Caneta": 50,
    "Borracha": 25
}
print("Produtos cadastrados:")
for produto, quantidade in produtos.items():
    print(f"{produto}: {quantidade} unidades")