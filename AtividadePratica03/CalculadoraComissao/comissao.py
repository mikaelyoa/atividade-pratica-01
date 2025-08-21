vendedor = input("Nome do vendedor: ")
salario_fixo = float(input("Salário fixo: "))
vendas = float(input("Total de vendas: "))

comissao = vendas * 0.15
total = salario_fixo + comissao

print("Total a receber = R$ {:.2f}".format(total))