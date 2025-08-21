temp = float(input("Digite a temperatura: "))
unidade_origem = input("Unidade de origem (C/F/K): ").upper()
unidade_destino = input("Unidade para converter (C/F/K): ").upper()

# Converter para Celsius primeiro
if unidade_origem == "C":
    temp_c = temp
elif unidade_origem == "F":
    temp_c = (temp - 32) * 5/9
elif unidade_origem == "K":
    temp_c = temp - 273.15

# Converter de Celsius para destino
if unidade_destino == "C":
    temp_final = temp_c
elif unidade_destino == "F":
    temp_final = temp_c * 9/5 + 32
elif unidade_destino == "K":
    temp_final = temp_c + 273.15

print("Temperatura convertida: {:.2f} {}".format(temp_final, unidade_destino))