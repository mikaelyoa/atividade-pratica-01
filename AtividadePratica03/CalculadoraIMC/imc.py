peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

print("IMC = {:.2f}".format(imc))
print("Classificação:", classificacao)