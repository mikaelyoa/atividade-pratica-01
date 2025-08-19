numero_funcionario = int(input("Número do funcionário: "))
horas_trabalhadas = int(input("Horas trabalhadas: "))
valor_por_hora = float(input("Valor por hora: "))

salario = horas_trabalhadas * valor_por_hora

print("Número do funcionário =", numero_funcionario)
print("Salário = R$", format(salario, ".2f"))