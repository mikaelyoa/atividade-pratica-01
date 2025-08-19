distancia = 300
combustivel = 25

consumo_medio = round(distancia / combustivel, 2)

print("Distância percorrida:", distancia, "km")
print("Combustível gasto:", combustivel, "litros")
print("Consumo médio: {:.2f} km/l".format(consumo_medio))