import requests

moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

try:
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        chave = f"{moeda}BRL"

        if chave in dados:
            info = dados[chave]
            print("Moeda:", moeda)
            print("Valor atual (R$):", info["bid"])
            print("Máximo (R$):", info["high"])
            print("Mínimo (R$):", info["low"])
            print("Data/Hora:", info["create_date"])
        else:
            print("Moeda não encontrada!")
    else:
        print("Erro ao acessar a API da AwesomeAPI!")
except Exception as e:
    print("Erro:", e)