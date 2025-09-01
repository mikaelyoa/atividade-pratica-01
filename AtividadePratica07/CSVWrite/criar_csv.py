import csv

dados = [
    ["Nome", "Idade", "Cidade"],
    ["Alice", 25, "João Pessoa"],
    ["Bruno", 30, "Campina Grande"],
    ["Carla", 22, "Recife"]
]

with open("pessoas.csv", mode="w", newline="", encoding="utf-8") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerows(dados)

print("Arquivo CSV criado com sucesso!")