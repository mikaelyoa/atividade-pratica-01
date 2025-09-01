import json

pessoa = {
    "nome": "Alice",
    "idade": 25,
    "cidade": "João Pessoa"
}

with open("pessoa.json", "w", encoding="utf-8") as arquivo_json:
    json.dump(pessoa, arquivo_json, ensure_ascii=False, indent=4)

with open("pessoa.json", "r", encoding="utf-8") as arquivo_json:
    dados = json.load(arquivo_json)
    print(dados)