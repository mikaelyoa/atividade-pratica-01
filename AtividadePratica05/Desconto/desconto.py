preco = float(input("Digite o preço do produto: R$ "))
desconto = preco * 0.15
novo_preco = preco - desconto
print(f"Desconto: R$ {desconto:.2f}")
print(f"Preço com desconto: R$ {novo_preco:.2f}")