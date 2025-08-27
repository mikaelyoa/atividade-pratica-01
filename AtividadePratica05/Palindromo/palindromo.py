texto = input("Digite uma palavra: ").replace(" ", "").lower()
if texto == texto[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")