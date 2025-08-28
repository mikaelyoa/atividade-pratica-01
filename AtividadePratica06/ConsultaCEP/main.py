import requests

cep = input("Digite o CEP: ").strip()

url = f"https://viacep.com.br/ws/{cep}/json/"

try:
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        if "erro" in dados:
            print("CEP não encontrado!")
        else:
            print("Logradouro:", dados.get("logradouro"))
            print("Bairro:", dados.get("bairro"))
            print("Cidade:", dados.get("localidade"))
            print("Estado:", dados.get("uf"))
    else:
        print("Erro ao acessar a API ViaCEP!")
except Exception as e:
    print("Erro:", e)