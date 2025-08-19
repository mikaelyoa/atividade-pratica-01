valor_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

valor_dolar = round(valor_reais / taxa_dolar, 2)
valor_euro = round(valor_reais / taxa_euro, 2)

print("Valor em reais: R$", valor_reais)
print("Convertido para Dólares: $", valor_dolar)
print("Convertido para Euros: €", valor_euro)