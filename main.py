print("=== CALCULADORA DE DESCONTO ===")
produto = input("Nome do produto: ")
preco = float(input("Preço: R$ "))
desconto = float(input("Desconto (%): "))

valor_desconto = preco * (desconto / 100)
preco_final = preco - valor desconto

print(f"\nProduto: {produto}")
print(f"Preço Original: R$ {valor_desconto:.2f}")
print(f"Desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")